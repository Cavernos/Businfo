import logging
from tkinter import Entry, END, Canvas

from businfo.src.businfo_Cavernos.assets.DigitPad import DigitPad
from businfo.src.businfo_Cavernos.assets.EscapeButton import EscapeButton
from businfo.src.businfo_Cavernos.assets.MenuReturnButton import MenuReturnButton
from businfo.src.businfo_Cavernos.assets.ProgressBar import ProgressBar
from businfo.src.businfo_Cavernos.handlers.Login import Login
from businfo.src.businfo_Cavernos.handlers.ModHandler import ModHandler
from businfo.src.businfo_Cavernos.handlers.ServiceHandler import ServiceHandler
from businfo.src.businfo_Cavernos.utils.utils import Utils

from businfo.src.businfo_Cavernos.assets.Info import Info


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
        self.login = Login(self.entry,
                           self.progress_bar,
                           self.canvas,
                           self.info,
                           self.mod_handler,
                           self.escape_button,
                           self.menu_return_button)

        self.service_handler = ServiceHandler(self.canvas, self.progress_bar, info, entry, digit_pad)

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
                match self.screen_index:
                    # Screen Login
                    case 0:
                        self.login.login()
                        self.canvas.after(1000, self.assign_mod_action)
                    # Screen Service
                    case 1:
                        text = self.entry.get()[0:6]
                        self.entry.place_forget()
                        self.entry.delete(0, END)
                        self.service_handler.service_search(text)
                    # Screen Special dest
                    case 2:
                        text = self.entry.get()[0:3]
                        print(text)
                        # TODO Enter text variable in a file
                        self.entry.place_forget()
                        self.entry.delete(0, END)
                        self.info.getDestinationLabel().config(text="D:" + "{:03}".format(int(text)))
                        self.login.valid_id()
                        self.screen_index = 1
            case _:
                logging.info("No Button.py correspond to this")

    def mod_push(self, index):
        match index:
            # Service Button
            case 0:
                if self.service_handler.active_service:
                    self.removeModeButtons()
                    self.service_handler.recap()
                else:
                    self.screen_index = 1
                    self.removeModeButtons()
                    self.service_handler.service()

            # Special Dest Button
            case 1:
                self.screen_index = 2
                self.removeModeButtons()
                self.special_dest()
            # Finish service Button
            case 2:
                self.finish_service()
            case _:
                logging.info("No Button.py correspond to this")

    def finish_service(self):
        self.removeModeButtons()
        self.login.invalid_id()
        self.service_handler.active_service = False
        self.info.getServiceLabel().config(text="S:000000")
        self.info.getLineLabel().config(text="L:0000")
        self.info.getDestinationLabel().config(text="D:000")
        self.info.getServiceInfo().config(text="Pas de Service en charge")
        self.screen_index = 0
        self.digit_pad.place()

    def special_dest(self):
        self.utils.loading_screen(self.canvas, "businfo_LK_input.png", (0, 67, 1024, 640))
        self.digit_pad.place()
        self.entry.place(x=17, y=220)

    def esc_push(self):
        if self.service_handler.active_service:
            self.removeModeButtons()
            self.service_handler.main_page()

    def return_push(self):
        if self.login and self.screen_index == 1:
            self.service_handler.setScreen("mod_chooser")
            self.entry.delete(0, END)
            self.entry.place_forget()
            service_info = self.service_handler.getServiceInfo()
            for i in range(0, 3):
                service_info[i].place_forget()
            for j in range(len(self.service_handler.services["stops"])):
                service_info[3][j].place_forget()
            self.mod_handler.generate("businfo_mode_select.png", (0, 67, 1024, 640))

    def assign_mod_action(self):
        if self.login.is_login:
            self.mod_buttons = self.mod_handler.getModButtons().getButtons()
            for i in range(0, 3):
                self.mod_buttons[i].config(command=lambda j=i: self.mod_push(j))
        else:
            logging.warning("Please Login")

    def removeModeButtons(self):
        self.mod_handler.getModButtons().mod_frame.place_forget()
        for i in range(0, 3):
            self.mod_buttons[i].place_forget()


