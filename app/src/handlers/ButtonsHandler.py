import datetime
import logging
import time
from tkinter import Entry, END, Canvas, N, W
from tkinter.ttk import Progressbar

from app.src.assets.DigitPad import DigitPad
from app.src.assets.EscapeButton import EscapeButton
from app.src.assets.MenuReturnButton import MenuReturnButton
from app.src.assets.ProgressBar import ProgressBar
from app.src.handlers.ModHandler import ModHandler
from app.src.handlers.ServiceHandler import ServiceHandler
from app.src.utils.utils import Utils

from app.src.assets.Info import Info


class ButtonHandler:
    def __init__(self, digit_pad: DigitPad, entry: Entry, info: Info, canvas: Canvas, screen_index: int):

        self.screen_index = screen_index
        self.utils = Utils()
        self.canvas = canvas
        self.info = info
        self.digit_pad = digit_pad
        self.digit_buttons = digit_pad.getButtons()
        self.mod_buttons = None
        self.mod_handler = ModHandler(self.canvas, digit_pad)
        self.entry = entry
        self.progress_bar = ProgressBar(self.canvas, length=327)
        self.escape_button = EscapeButton(self.canvas, border=0, width=194, height=94, x=823, y=470)
        self.menu_return_button = MenuReturnButton(self.canvas, border=0, width=90, height=60, x=715, y=506)

        self.service_handler = ServiceHandler(self.canvas, self.progress_bar, info, entry, digit_pad)
        self.is_login = False

        for i in range(0, 13):
            self.digit_buttons[i].config(command=lambda j=i: self.digit_push(j))
        self.escape_button.getItem().config(command=self.esc_push)
        self.menu_return_button.getItem().config(command=self.return_push)

    def digit_push(self, index):
        match index:
            case 0:
                self.entry.insert(END, "1")
            case 1:
                self.entry.insert(END, "2")
            case 2:
                self.entry.insert(END, "3")
            case 3:
                self.entry.insert(END, "4")
            case 4:
                self.entry.insert(END, "5")
            case 5:
                self.entry.insert(END, "6")
            case 6:
                self.entry.insert(END, "7")
            case 7:
                self.entry.insert(END, "8")
            case 8:
                self.entry.insert(END, "9")
            case 9:
                last_character = self.entry.get()[0:6][:-1]
                self.entry.delete(len(last_character), END)
            case 10:
                self.entry.insert(END, "0")
            case 11:
                self.entry.delete(0, END)
            case 12:
                if self.screen_index == 0:
                    self.login()
                elif self.screen_index == 2:
                    text = self.entry.get()[0:3]
                    print(text)
                    # TODO Enter text variable in a file
                    self.entry.place_forget()
                    self.entry.delete(0, END)
                    self.valid_id()
                elif self.screen_index == 1:
                    text = self.entry.get()[0:6]
                    self.entry.place_forget()
                    self.entry.delete(0, END)
                    if self.service_handler.active_service:
                        # TODO Pass Service Object
                        self.service_handler.service_found({"next_start": "19:15:00"})
                    else:
                        self.service_handler.service_search(text)
            case _:
                logging.info("No Button.py correspond to this")

    def mod_push(self, index):
        match index:
            case 0:
                self.screen_index = 1
                self.removeModeButtons()
                self.service_handler.service()
            case 1:
                self.screen_index = 2
                self.removeModeButtons()
                self.special_dest()
            case 2:
                self.removeModeButtons()
                self.invalid_id()
                self.service_handler.active_service = False
                self.info.getServiceLabel().config(text="S:000000")
                self.info.getServiceInfo().config(text="Pas de Service en charge")
                self.screen_index = 0
                self.digit_pad.place()
            case _:
                logging.info("No Button.py correspond to this")

    def esc_push(self):
        # TODO
        pass

    def return_push(self):
        if self.login and self.screen_index == 1:
            self.entry.delete(0, END)
            self.entry.place_forget()
            self.mod_handler.generate("businfo_mode_select.png", (0, 67, 1024, 640))

    def login(self):
        text = self.entry.get()[0:6]
        self.entry.place_forget()
        self.entry.delete(0, END)
        self.utils.loading_screen(self.canvas, "businfo_ID_loading.png", (0, 67, 1024, 640))
        self.progress_bar.getBar().place(x=20, y=190)
        self.progress_bar.progress_start()
        if text == "229":
            logging.info("Logged In")
            self.info.getDriverLabel().config(text="Cn:" + "{:06d}".format(int(text)))
            self.canvas.after(1000, self.valid_id)
        else:
            self.progress_bar.getBar().place_forget()
            self.utils.loading_screen(self.canvas, "businfo_ID_loading_error_WID.png", (0, 67, 1024, 640))
            self.canvas.after(2000, self.invalid_id)
            logging.info("Logging Failure")

    def invalid_id(self):
        self.utils.loading_screen(self.canvas, "businfo_ID_input.png", (0, 67, 1024, 640))
        self.info.getDriverLabel().config(text="Cn:000000")
        self.entry.place(x=17, y=220)
        self.is_login = False

    def valid_id(self):
        self.progress_bar.getBar().place_forget()
        self.mod_handler.generate("businfo_mode_select.png", (0, 67, 1024, 640))
        self.escape_button.place()
        self.menu_return_button.place()
        self.mod_buttons = self.mod_handler.getModButtons().getButtons()
        self.is_login = True
        for i in range(0, 3):
            self.mod_buttons[i].config(command=lambda j=i: self.mod_push(j))

    def removeModeButtons(self):
        self.mod_handler.getModButtons().mod_frame.place_forget()
        for i in range(0, 3):
            self.mod_buttons[i].place_forget()

    def special_dest(self):
        self.utils.loading_screen(self.canvas, "businfo_LK_input.png", (0, 67, 1024, 640))
        self.digit_pad.place()
        self.entry.place(x=17, y=220)
