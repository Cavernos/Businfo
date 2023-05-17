import json
import os

from businfo.definitions import ROOT_DIR


class FileHandler:
    def __init__(self, file):
        self.cached_stamp = 0
        self.file = file

    def file_update(self):
        stamp = os.stat(os.path.join(ROOT_DIR, self.file)).st_mtime
        if stamp != self.cached_stamp:
            self.cached_stamp = stamp
            return True
        else:
            return False

    def decode(self):
        with open(os.path.join(ROOT_DIR, self.file)) as json_file:
            file = json.load(json_file)
            return file
