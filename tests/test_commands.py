import os
import sys
import tempfile

sys.path.append("src")

from vfs import VFS


def create_test_vfs(directory):
    file_path = os.path.join(directory, "file1.txt")

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("hello")

    folder_path = os.path.join(directory, "folder")
    os.makedirs(folder_path)

    second_file = os.path.join(folder_path, "file2.txt")

    with open(second_file, "w", encoding="utf-8") as file:
        file.write("world")


def test_ls():
    with tempfile.TemporaryDirectory() as directory:
        create_test_vfs(directory)
        vfs = VFS(directory)

        items = vfs.list_directory()

        assert "file1.txt" in items
        assert "folder" in items


def test_cd():
    with tempfile.TemporaryDirectory() as directory:
        create_test_vfs(directory)
        vfs = VFS(directory)

        vfs.change_directory("folder")

        assert vfs.current_path == ["folder"]


def test_cd_parent():
    with tempfile.TemporaryDirectory() as directory:
        create_test_vfs(directory)
        vfs = VFS(directory)

        vfs.change_directory("folder")
        vfs.change_directory("..")

        assert vfs.current_path == []


def test_cat():
    with tempfile.TemporaryDirectory() as directory:
        create_test_vfs(directory)
        vfs = VFS(directory)

        content = vfs.read_file("file1.txt")

        assert content == "hello"


def test_cat_in_folder():
    with tempfile.TemporaryDirectory() as directory:
        create_test_vfs(directory)
        vfs = VFS(directory)

        vfs.change_directory("folder")

        content = vfs.read_file("file2.txt")

        assert content == "world"


def test_uptime():
    with tempfile.TemporaryDirectory() as directory:
        vfs = VFS(directory)

        seconds = vfs.get_uptime()

        assert seconds >= 0

def test_touch():
    with tempfile.TemporaryDirectory() as directory:
        create_test_vfs(directory)
        vfs = VFS(directory)

        vfs.touch("new.txt")

        assert "new.txt" in vfs.data
        assert vfs.data["new.txt"] == ""


def test_touch_only_in_memory():
    with tempfile.TemporaryDirectory() as directory:
        create_test_vfs(directory)
        vfs = VFS(directory)

        vfs.touch("new.txt")

        file_path = os.path.join(directory, "new.txt")

        assert not os.path.exists(file_path)