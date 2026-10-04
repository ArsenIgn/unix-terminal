import os
import sys

sys.path.append("src")

from parser import parse_command


def test_ls():
    command, args = parse_command("ls test")

    assert command == "ls"
    assert args == ["test"]


def test_cd():
    command, args = parse_command("cd folder")

    assert command == "cd"
    assert args == ["folder"]

def test_environment_variable():
    os.environ["TEST_FOLDER"] = "my_folder"

    command, args = parse_command("cd $TEST_FOLDER")

    assert command == "cd"
    assert args == ["my_folder"]