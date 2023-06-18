from tkinter import Tk

from businfo.definitions import width, height


class Root(Tk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{width}x{height}")
        self.title("businfo")
        self.resizable(True, True)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.update()
        self.update_idletasks()
