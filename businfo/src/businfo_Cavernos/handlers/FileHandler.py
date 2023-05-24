import json
import os

from businfo.definitions import ROOT_DIR, template


class FileHandler:
    def __init__(self, file):
        self.cached_stamp = 0
        self.file = file
        self.template = template
        self.test_file = "E:\\SteamLibrary\\steamapps\\common\\OMSI 2\\plugins\\service.json"

    def file_update(self):
        # stamp = os.stat(os.path.join(ROOT_DIR, self.file)).st_mtime
        stamp = os.stat(self.test_file).st_mtime
        if stamp != self.cached_stamp:
            self.cached_stamp = stamp
            return True
        else:
            return False

    def decode(self):
        # with open(os.path.join(ROOT_DIR, self.file)) as json_file:
        with open(self.test_file) as json_file:
            try:
                file = json.load(json_file)
                self.template = file
            except ValueError as e:
                file = self.template
            return file




