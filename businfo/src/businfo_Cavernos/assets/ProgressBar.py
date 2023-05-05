import time
from tkinter.ttk import Progressbar


class ProgressBar:
    def __init__(self, canvas, length):
        self.canvas = canvas
        self.progress_bar = Progressbar(canvas, length=length)

    def getBar(self):
        return self.progress_bar

    def progress_start(self):
        tasks = 5
        x = 0
        while x < tasks:
            time.sleep(0.5)
            self.progress_bar["value"] += 10
            x += 1
            self.canvas.update_idletasks()
        self.progress_bar['value'] = 0
