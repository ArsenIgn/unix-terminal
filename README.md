# unix-terminal

Учебный проект — эмулятор Unix-терминала, написанный на Python.

Программа работает с виртуальной файловой системой и поддерживает базовые команды терминала.

## Команды

Реализованы следующие команды:

- `ls` — просмотр содержимого директории;
- `cd` — переход между директориями;
- `cat` — вывод содержимого файла;
- `touch` — создание нового файла;
- `uptime` — вывод времени работы программы;
- `vfs-init` — сброс виртуальной файловой системы;
- `exit` — завершение работы программы.

## Возможности
Также программа поддерживает:

- виртуальную файловую систему;
- запуск команд из стартового скрипта;
- конфигурационный файл TOML;
- аргументы командной строки;
- обработку ошибок;
- тестирование с помощью pytest.


## Структура проекта

```text
unix-terminal/
├── scripts/
│   ├── stage4_error.txt
│   ├── stage4_startup.txt
│   ├── stage5_error.txt
│   ├── stage5_startup.txt
│   ├── startup.txt
│   ├── test_cli.bat
│   ├── test_cli.sh
│   ├── test_startup.txt
│   ├── test_vfs_deep.bat
│   ├── test_vfs_files.bat
│   └── test_vfs_minimal.bat
│
├── src/
│   ├── commands.py
│   ├── config.py
│   ├── main.py
│   ├── parser.py
│   └── vfs.py
│
├── tests/
│   ├── test_commands.py
│   ├── test_config.py
│   ├── test_repl.py
│   └── test_vfs.py
│
├── vfs/
│   ├── folder/
│   │   └── level12/
│   │       └── level13/
│   │           └── test.txt
│   └── file1.txt
│
├── vfs_test/
│   └── deep/
│
├── .gitignore
├── config.toml
├── README.md
├── run.bat
└── run.sh