from parser import parse_command
from commands import execute_command
from config import parse_arguments, get_configuration
from vfs import VFS
VFS_NAME = "my_vfs"

def run_command(command_line, vfs):
    command, args = parse_command(command_line)
    
    if command == "exit":
        return False
    
    execute_command(command, args,vfs)

    return True

def run_script(script_path, vfs):
    try:
        with open(script_path, "r", encoding="utf-8") as file:
            for line in file:
                command_line = line.strip()

                if not command_line or command_line.startswith("#"):
                    continue

                print(f"{VFS_NAME}> {command_line}")


                try:
                    should_continue = run_command(command_line,vfs)

                except ValueError as error:
                    print(f"Ошибка: {error}")
                    return

                if not should_continue:
                    return

    except FileNotFoundError:
        print(f"Ошибка: стартовый скрипт не найден: {script_path}")      
            

def main():
    try:
        args = parse_arguments()
        config = get_configuration(args)

    except ValueError as error:
        print(f"Ошибка: {error}")
        return
    
    print("Параметры запуска:")
    print("VFS", config["vfs_path"])
    print("Стартовый скрипт:", config["startup_script"])
    print("Конфигурационный файл", config["config_path"])

    if config["vfs_path"] is None:
        print("Ошибка: путь к VFS не задан")
        return

    vfs = VFS(config["vfs_path"])

    if config["startup_script"]:
        run_script(config["startup_script"], vfs)

    while True:
        try:
            user_input = input(f"{VFS_NAME}> ")

            if not user_input.strip():
                continue

            if not run_command(user_input, vfs):
                break
            
        except ValueError as error:
            print(f"Ошибка: {error}")

if __name__ == "__main__":
    main()
