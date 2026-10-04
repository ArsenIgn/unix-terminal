from parser import parse_command
from commands import execute_command
VFS_NAME = "my_vfs"
def main():
    while True:
        try:
            user_input = input(f"{VFS_NAME}> ")

            if not user_input.strip():
                continue

            command, args = parse_command(user_input)

            if command == "exit":
                break

            execute_command(command, args)
        except ValueError as error:
            print(f"Ошибка: {error}")

if __name__ == "__main__":
    main()
