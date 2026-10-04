import os
import shutil


class VFS:
    def __init__(self, root_path):
        self.root_path = root_path
        self.data = {}
        self.load()

    def load(self):
        if not os.path.exists(self.root_path):
            os.makedirs(self.root_path)

        self.data = self._read_directory(self.root_path)

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

    def reset(self):
        if os.path.exists(self.root_path):
            shutil.rmtree(self.root_path)

        os.makedirs(self.root_path)

        self.data = {}