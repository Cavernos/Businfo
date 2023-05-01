import os
from tkinter import Canvas, Button, SUNKEN

from PIL import ImageTk, Image

from app.src.assets.Button import ButtonAsset
from definitions import ROOT_DIR


class MenuReturnButton(ButtonAsset):
    def __init__(self, panel: Canvas, border: int, width: int, height: int, x: int, y: int):
        super().__init__(panel, border, width, height, x, y)
        self.image = Image.open(os.path.join(ROOT_DIR, "texture", "menu_return_button.png"))
        super().createButton()


