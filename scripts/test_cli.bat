@echo off

echo TEST 1 - только config
python src/main.py --config config.toml

echo.

echo TEST 2 - VFS из командной строки
python src/main.py --config config.toml --vfs custom_vfs

echo.

echo TEST 3 - стартовый скрипт из командной строки
python src/main.py --config config.toml --script scripts/startup.txt