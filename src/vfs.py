import os
import shutil
import time

class VFS:
    def __init__(self, root_path):
        self.root_path = root_path
        self.data = {}
        self.current_path = []
        self.start_time = time.time()
        self.load()

    def load(self):
        if not os.path.exists(self.root_path):
            os.makedirs(self.root_path)

        self.data = self._read_directory(self.root_path)
        self.current_path = []

    def _read_directory(self, path):
        result = {}

        for item in os.listdir(path):
            full_path = os.path.join(path, item)

            if os.path.isdir(full_path):
                result[item] = self._read_directory(full_path)

            else:
                with open(full_path, "r", encoding="utf-8") as file:
                    result[item] = file.read()

        return result

    def get_current_directory(self):
        directory = self.data

        for part in self.current_path:
            directory = directory[part]

        return directory

    def _resolve_path(self, path):
        if path.startswith("/"):
            parts = []
        else:
            parts = self.current_path.copy()

        path_parts = path.split("/")

        for part in path_parts:
            if part == "" or part == ".":
                continue

            if part == "..":
                if parts:
                    parts.pop()
            else:
                parts.append(part)

        return parts

    def get_node(self, path):
        parts = self._resolve_path(path)
        node = self.data

        for part in parts:
            if not isinstance(node, dict):
                raise ValueError(f"не является директорией: {part}")

            if part not in node:
                raise ValueError(f"путь не найден: {path}")

            node = node[part]

        return node


    def list_directory(self, path="."):
        node = self.get_node(path)

        if not isinstance(node, dict):
            raise ValueError(f"не является директорией: {path}")

        return list(node.keys())


    def change_directory(self, path):
        new_path = self._resolve_path(path)
        node = self.data

        for part in new_path:
            if not isinstance(node, dict):
                raise ValueError(f"не является директорией: {path}")

            if part not in node:
                raise ValueError(f"директория не найдена: {path}")

            node = node[part]

            if not isinstance(node, dict):
                raise ValueError(f"не является директорией: {path}")
        self.current_path = new_path

    def read_file(self, path):
        node = self.get_node(path)

        if isinstance(node, dict):
            raise ValueError(f"это директория: {path}")

        return node

    def get_uptime(self):
        return int(time.time() - self.start_time)

    def reset(self):
        if os.path.exists(self.root_path):
            shutil.rmtree(self.root_path)

        os.makedirs(self.root_path)

        self.data = {}
        self.current_path = []