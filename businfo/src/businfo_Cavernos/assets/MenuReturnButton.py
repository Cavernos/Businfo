import os
from tkinter import Canvas

from PIL import Image

from businfo.src.businfo_Cavernos.assets.Button import Buttons
from businfo.definitions import ROOT_DIR


class MenuReturnButton(Buttons):
    def __init__(self, panel: Canvas, border: int, width: int, height: int, x: int, y: int):
        super().__init__(panel, border, width, height, x, y)
        self.image = Image.open(os.path.join(ROOT_DIR, "texture", "buttons", "menu_return_button.png"))
        super().createButton()


