import os
from tkinter import Frame, Button, Canvas

from PIL import Image, ImageTk

from businfo.definitions import ROOT_DIR


class ModButtons:
    def __init__(self, panel: Canvas, border: int, bg: str, width: int, height: int, x: int, y: int):
        self.mod_frame = Frame(panel, border=border, bg=bg, width=width, height=height)
        self.x = x
        self.y = y
        self.height = height
        self.buttons = []
        self.image = []

    def place(self):
        self.mod_frame.place(x=self.x, y=self.y)
        for i in range(0, 3):
            self.buttons[i].place(x=-5, y=(self.height / 3) * i)

    def addButtons(self):
        for i in range(0, 3):
            image = Image.open(os.path.join(ROOT_DIR, "texture", "buttons", "modMenu", f"{i}.png"))
            self.image.append(ImageTk.PhotoImage(image))
            self.buttons.append(Button(self.mod_frame,
                                       image=self.image[i],
                                       width=540,
                                       height=self.height / 3 - 5,
                                       relief="sunken",
                                       cursor="hand2",
                                       border=0
                                       ))

    def getButtons(self):
        return self.buttons
