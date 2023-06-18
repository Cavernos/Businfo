from tkinter import Frame, Canvas, W, N

from PIL import ImageTk

from businfo.definitions import width, height
from businfo.src.businfo_Cavernos.utils.utils import Utils


class Boot1View(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.utils = Utils()
        self.canvas = Canvas(self, width=width, height=height, highlightthickness=0)
        self.canvas.create_image((0, 0), anchor=N + W)
        self.load_photo = ImageTk.PhotoImage(self.utils.load_image("businfo_boot1"))
        self.canvas.itemconfig(1, image=self.load_photo)
        self.canvas.pack()