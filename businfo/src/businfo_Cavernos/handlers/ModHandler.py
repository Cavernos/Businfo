from tkinter import Canvas

from businfo.src.businfo_Cavernos.assets.DigitPad import DigitPad
from businfo.src.businfo_Cavernos.assets.ModButtons import ModButtons
from businfo.src.businfo_Cavernos.utils.utils import Utils


class ModHandler:
    def __init__(self, canvas: Canvas, digit_frame: DigitPad):
        self.utils = Utils()
        self.canvas = canvas
        self.digit_frame = digit_frame
        self.ModButtons = ModButtons(self.canvas, border=0, bg="#3A393A", width=535, height=210, x=73, y=139)

    def generate(self, filename, crop):
        self.digit_frame.removeDigitPad()
        self.utils.loading_screen(self.canvas, filename, crop)
        self.ModButtons.addButtons()
        self.ModButtons.place()

    def getModButtons(self):
        return self.ModButtons

