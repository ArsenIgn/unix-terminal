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

def command_vfs_init(args, vfs):
    if len(args) != 0:
        raise ValueError("vfs-init: аргументы не поддерживаются")
    vfs.reset()
    print("VFS сброшена к состоянию по умолчанию")

def execute_command(command, args, vfs=None):
    if command == "ls":
        command_ls(args)

    elif command == "cd":
        command_cd(args)

    elif command == "vfs-init":
        if vfs is None:
            raise ValueError("VFS не инициализирована")
        command_vfs_init(args, vfs)

    else: 
        raise ValueError(f"Неизвестная команда: {command}")