import os
from tkinter import Frame, Button, SUNKEN

from PIL import ImageTk, Image

from definitions import ROOT_DIR


class DigitPad:
    def __init__(self, panel: Frame, border: int, bg: str, width: int, height: int, x: int, y: int):
        self.digit_frame = Frame(panel, border=border, bg=bg, width=width, height=height)
        self.x = x
        self.y = y
        self.image = []
        self.buttons = []
        self.button_width = [int()] * 13
        self.button_height = [int()] * 13
        for j in range(0, 4):
            for i in range(0, 3):
                button_index = i + 3 * j
                self.button_width[button_index] = 87 if i == 0 else 88
                self.button_height[button_index] = 72 if j == 3 else 73

    def place(self):
        self.digit_frame.place(x=self.x, y=self.y)
        for j in range(0, 4):
            for i in range(0, 3):
                button_index = i + 3 * j
                x = 0 if i == 0 else i * self.button_width[button_index - 1] + 10 * i
                y = 0 if j == 0 else j * self.button_height[button_index - 3] + 10 * j
                self.buttons[button_index].place(x=x, y=y)
        self.buttons[12].place(x=196, y=379)

    def addButtons(self):
        for i in range(0, 13):
            image = Image.open(os.path.join(ROOT_DIR, "texture", "digits", f"{i}.png"))
            self.image.append(ImageTk.PhotoImage(image))
            self.buttons.append(Button(self.digit_frame,
                                       image=self.image[i],
                                       width=self.button_width[i],
                                       height=self.button_height[i],
                                       relief=SUNKEN,
                                       cursor="hand2",
                                       border=0
                                       ))

    def getButtons(self):
        return self.buttons

    def removeButtons(self):
        for i in range(0, 13):
            self.buttons[i].place_forget()

    def removeDigitPad(self):
        self.removeButtons()
        self.digit_frame.place_forget()



