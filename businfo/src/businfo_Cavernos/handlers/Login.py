import logging
from tkinter import Canvas, Entry, END

from businfo.src.businfo_Cavernos.assets.EscapeButton import EscapeButton
from businfo.src.businfo_Cavernos.assets.Info import Info
from businfo.src.businfo_Cavernos.assets.MenuReturnButton import MenuReturnButton
from businfo.src.businfo_Cavernos.assets.ProgressBar import ProgressBar
from businfo.src.businfo_Cavernos.handlers.ModHandler import ModHandler
from businfo.src.businfo_Cavernos.utils.utils import Utils


class Login:
    def __init__(self, entry: Entry,
                 progress_bar: ProgressBar,
                 canvas: Canvas, info: Info,
                 mod_handler: ModHandler,
                 escape_button: EscapeButton,
                 menu_return_button: MenuReturnButton
                 ):
        self.utils = Utils()
        self.entry = entry
        self.progress_bar = progress_bar
        self.canvas = canvas
        self.info = info
        self.mod_handler = mod_handler
        self.escape_button = escape_button
        self.menu_return_button = menu_return_button
        self.is_login = False

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
        self.is_login = True


