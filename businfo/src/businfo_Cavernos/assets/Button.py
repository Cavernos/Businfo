import os
from tkinter import SUNKEN, Button, Canvas

from PIL import Image, ImageTk

from businfo.definitions import ROOT_DIR


class Buttons:
    def __init__(self, panel: Canvas, border: int, width: int, height: int, x: int, y: int):
        self.panel = panel
        self.border = border
        self.width = width
        self.height = height
        self.y = y
        self.x = x
        self.image = Image.open(os.path.join(ROOT_DIR, "texture", "buttons", "menu_return_button.png"))
        self.item = None
        self.imagetk = None

    def place(self):
        self.item.place(x=self.x, y=self.y)

    def createButton(self):
        self.imagetk = ImageTk.PhotoImage(self.image)
        self.item = Button(self.panel, border=self.border, width=self.width, height=self.height, image=self.imagetk,
                           relief=SUNKEN,
                           cursor="hand2")

    def getItem(self):
        return self.item
