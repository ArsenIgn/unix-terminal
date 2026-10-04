def command_ls(args):
    if len(args) > 1:
        raise ValueError("ls: неверное количество аргументов")

    print("Команда: ls")
    print("Аргументы:", args)

def command_cd(args):
    if len(args) != 1:
        raise ValueError("cd: требуется один аргумент")

    print("Команда: cd")
    print("Аргументы:", args)


def execute_command(command, args):
    if command == "ls":
        command_ls(args)

    elif command == "cd":
        command_cd(args)

    else: 
        raise ValueError(f"Неизвестная команда: {command}")