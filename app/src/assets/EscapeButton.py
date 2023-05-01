import os
from tkinter import Button, Canvas
from tkinter.constants import SUNKEN

from PIL import Image, ImageTk

from app.src.assets.Button import ButtonAsset
from definitions import ROOT_DIR


class EscapeButton(ButtonAsset):
    def __init__(self, panel: Canvas, border: int, width: int, height: int, x: int, y: int):
        super().__init__(panel, border, width, height, x, y)
        self.image = Image.open(os.path.join(ROOT_DIR, "texture", "escape_button.png"))
        super().createButton()
