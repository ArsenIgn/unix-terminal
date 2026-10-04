import argparse
import tomllib


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--vfs",
        help="Путь к физическому расположению VFS"
    )

    parser.add_argument(
        "--script",
        help="Путь к стартовому скрипту"
    )

    parser.add_argument(
        "--config",
        help="Путь к конфигурационному файлу"
    )

    return parser.parse_args()


def read_config(config_path):
    if config_path is None:
        return {}

    try:
        with open(config_path, "rb") as file:
            return tomllib.load(file)

    except FileNotFoundError:
        raise ValueError(
            f"не удалось открыть конфигурационный файл: {config_path}"
        )

    except tomllib.TOMLDecodeError:
        raise ValueError(
            f"ошибка чтения TOML-файла: {config_path}"
        )


def get_configuration(args):
    config = read_config(args.config)

    vfs_path = args.vfs or config.get("vfs_path")
    startup_script = args.script or config.get("startup_script")

    return {
        "vfs_path": vfs_path,
        "startup_script": startup_script,
        "config_path": args.config
    }