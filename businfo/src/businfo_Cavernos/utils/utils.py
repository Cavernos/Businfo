import os
from tkinter import Canvas, N, W

from PIL import Image, ImageTk

from businfo.definitions import ROOT_DIR, width as root_w, height as root_h


class Utils:
    def __init__(self):
        self.height = None
        self.load_photo = None

    def loading_screen(self, canvas: Canvas, filename="businfo_boot0", crop=None) -> None:
        self.load_photo = ImageTk.PhotoImage(self.load_image(filename, crop))
        canvas.create_image((0, 0), anchor=N + W)
        canvas.itemconfig(1, image=self.load_photo)
        canvas.config(height=self.height)

    def load_image(self, filename, crop=None):
        filename = os.path.join(ROOT_DIR, 'texture', filename + ".png")
        image = Image.open(filename)
        new_image = image.crop(crop)
        width, self.height = new_image.size
        return new_image.resize((root_w * width // 1024, root_h * self.height // 640))

