import logging
import os
from tkinter import Canvas, N, W

from PIL import Image, ImageTk

from definitions import ROOT_DIR


class Utils:
    def __init__(self):
        self.load_photo = None

    def loading_screen(self, canvas: Canvas, filename="businfo_boot0.png", crop=None) -> None:
        back_img = canvas.create_image((0, 0), anchor=N + W)
        filename = os.path.join(ROOT_DIR, 'texture', filename)
        image = Image.open(filename)
        new_image = image.crop(crop)
        width, height = new_image.size
        self.load_photo = ImageTk.PhotoImage(new_image)
        canvas.itemconfig(back_img, image=self.load_photo)
        canvas.config(height=height)
        logging.info("Screen Info changes successfully")
