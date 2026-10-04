def command_ls(args, vfs):
    if len(args) > 1:
        raise ValueError("ls: неверное количество аргументов")

    if len(args) == 0:
        path = "."
    else:
        path = args[0]

    items = vfs.list_directory(path)

    for item in items:
        print(item)


def command_cd(args, vfs):
    if len(args) != 1:
        raise ValueError("cd: требуется один аргумент")

    vfs.change_directory(args[0])

def command_cat(args, vfs):
    if len(args) != 1:
        raise ValueError("cat: требуется один аргумент")

    content = vfs.read_file(args[0])

    print(content)

def command_uptime(args, vfs):
    if len(args) != 0:
        raise ValueError("uptime: аргументы не поддерживаются")

    seconds = vfs.get_uptime()

    print(f"Время работы: {seconds} сек.")

def command_vfs_init(args, vfs):
    if len(args) != 0:
        raise ValueError("vfs-init: аргументы не поддерживаются")
    vfs.reset()
    print("VFS сброшена к состоянию по умолчанию")

def execute_command(command, args, vfs=None):
    if vfs is None:
        raise ValueError("VFS не инициализирована")
        
    if command == "ls":
        command_ls(args,vfs)

    elif command == "cd":
        command_cd(args,vfs)

    elif command == "vfs-init":
        command_vfs_init(args, vfs)

    elif command == "cat":
        command_cat(args, vfs)

    elif command == "uptime":
        command_uptime(args, vfs)

    else: 
        raise ValueError(f"Неизвестная команда: {command}")