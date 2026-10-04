#!/bin/bash

echo "TEST 1 - только config"
python3 src/main.py --config config.toml

echo

echo "TEST 2 - VFS из командной строки"
python3 src/main.py --config config.toml --vfs custom_vfs

echo

echo "TEST 3 - стартовый скрипт из командной строки"
python3 src/main.py --config config.toml --script scripts/startup.txt