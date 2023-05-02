import json


class FileHandler:
    def __init__(self, file):
        self.file = file

    def decode(self):
        return json.load(self.file)
