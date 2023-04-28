import json
import logging
import time
from tkinter import Entry, END, Canvas, N, W
from tkinter.ttk import Progressbar

from app.src.assets.DigitPad import DigitPad
from app.src.handlers.ModHandler import ModHandler
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
        self.progress_bar = Progressbar(self.canvas, length=327)

        for i in range(0, 13):
            self.digit_buttons[i].config(command=lambda j=i: self.digit_push(j))

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
                    self.service_search(text)
            case _:
                logging.info("No Button correspond to this")

    def mod_push(self, index):
        match index:
            case 0:
                self.screen_index = 1
                self.removeModeButtons()
                self.service()
            case 1:
                self.screen_index = 2
                self.removeModeButtons()
                self.special_dest()
            case 2:
                self.removeModeButtons()
                self.invalid_id()
                self.digit_pad.place()
            case _:
                logging.info("No Button correspond to this")

    def login(self):
        text = self.entry.get()[0:6]
        self.entry.place_forget()
        self.entry.delete(0, END)
        self.utils.loading_screen(self.canvas, "businfo_ID_loading.png", (0, 67, 1024, 640))
        self.progress_bar.place(x=20, y=190)
        self.progress_start()
        if text == "229":
            logging.info("Logged In")
            self.info.getDriverLabel().config(text="Cn:" + "{:06d}".format(int(text)))
            self.canvas.after(1000, self.valid_id)
        else:
            self.progress_bar.place_forget()
            self.utils.loading_screen(self.canvas, "businfo_ID_loading_error_WID.png", (0, 67, 1024, 640))
            self.canvas.after(2000, self.invalid_id)
            logging.info("Logging Failure")

    def invalid_id(self):
        self.utils.loading_screen(self.canvas, "businfo_ID_input.png", (0, 67, 1024, 640))
        self.info.getDriverLabel().config(text="Cn:000000")
        self.entry.place(x=17, y=220)

    def valid_id(self):
        self.progress_bar.place_forget()
        self.mod_handler.generate("businfo_mode_select.png", (0, 67, 1024, 640))
        self.mod_buttons = self.mod_handler.getModButtons().getButtons()
        for i in range(0, 3):
            self.mod_buttons[i].config(command=lambda j=i: self.mod_push(j))

    def progress_start(self):
        tasks = 5
        x = 0
        while x < tasks:
            time.sleep(0.5)
            self.progress_bar["value"] += 10
            x += 1
            self.canvas.update_idletasks()
        self.progress_bar['value'] = 0

    def removeModeButtons(self):
        self.mod_handler.getModButtons().mod_frame.place_forget()
        for i in range(0, 3):
            self.mod_buttons[i].place_forget()

    def special_dest(self):
        self.utils.loading_screen(self.canvas, "businfo_LK_input.png", (0, 67, 1024, 640))
        self.digit_pad.place()
        self.entry.place(x=17, y=220)

    def service(self):
        self.utils.loading_screen(self.canvas, "businfo_service_input.png", (0, 67, 1024, 640))
        self.digit_pad.place()
        self.entry.place(x=17, y=220)

    def service_search(self, service_int):
        self.utils.loading_screen(self.canvas, "businfo_service_loading.png", (0, 67, 1024, 640))
        self.progress_bar.place(x=20, y=190)
        self.progress_start()
        gprs = False
        services = {2}
        for service in services:
            if int(service_int) == service:
                gprs = True
            else:
                gprs = False
        if gprs:
            self.progress_bar.place_forget()
            self.service_found()
        else:
            self.progress_bar.place_forget()
            self.utils.loading_screen(self.canvas, "businfo_service_loading_error_gprs.png", (0, 67, 1024, 640))
            self.canvas.after(2000, self.service_not_found)

    def service_found(self):
        print(0)
        # TODO
        pass

    def service_not_found(self):
        self.utils.loading_screen(self.canvas, "businfo_service_input.png", (0, 67, 1024, 640))
        self.info.getServiceLabel().config(text="S:000000")
        self.entry.place(x=17, y=220)

