import os
import sys
import tempfile

sys.path.append("src")

from vfs import VFS


def test_vfs_load():
    with tempfile.TemporaryDirectory() as directory:
        file_path = os.path.join(directory, "test.txt")

        with open(file_path, "w", encoding="utf-8") as file:
            file.write("hello")

        vfs = VFS(directory)

        assert "test.txt" in vfs.data
        assert vfs.data["test.txt"] == "hello"


def test_vfs_nested():
    with tempfile.TemporaryDirectory() as directory:
        level1 = os.path.join(directory, "level1")
        level2 = os.path.join(level1, "level2")
        level3 = os.path.join(level2, "level3")

        os.makedirs(level3)

        file_path = os.path.join(level3, "test.txt")

        with open(file_path, "w", encoding="utf-8") as file:
            file.write("deep")

        vfs = VFS(directory)

        assert "level1" in vfs.data
        assert "level2" in vfs.data["level1"]
        assert "level3" in vfs.data["level1"]["level2"]


def test_vfs_reset():
    with tempfile.TemporaryDirectory() as directory:
        file_path = os.path.join(directory, "test.txt")

        with open(file_path, "w", encoding="utf-8") as file:
            file.write("hello")

        vfs = VFS(directory)

        vfs.reset()

        assert vfs.data == {}
        assert os.listdir(directory) == []