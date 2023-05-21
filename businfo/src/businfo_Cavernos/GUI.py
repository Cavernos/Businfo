import sys
from tkinter import *
import logging
from assets.DigitPad import DigitPad
from assets.Info import Info
from handlers.ButtonHandler import ButtonHandler
from utils.utils import Utils
from utils.Tracker import Tracker
from businfo.definitions import font, width, height


class GUI(object):
    def __init__(self, system: str) -> None:
        # Init Window
        self.root = Tk()
        if system == "linux":
            self.root.geometry(f"{width}x{height}")
        else:
            self.root.geometry(f"{width}x{height}")
        self.root.title("businfo")
        self.root.resizable(True, True)
        self.root.update_idletasks()
        self.root.update()
        logging.info("Window Init Successfully")

        # Some Definition
        self.bg_color = "#312D8C"
        self.width = self.root.winfo_width()
        self.height = self.root.winfo_height()
        self.utils = Utils()

        # Init First Frame
        self.main_frame = Frame(self.root, height=height)
        self.main_frame.grid(row=1)

        # Init Canvas for images
        self.canvas = Canvas(self.main_frame, width=width, height=height, highlightthickness=0)
        self.canvas.pack()

        # Infos Frame
        self.service_label = Label(self.main_frame, font=font, fg="white", bg="#3A393A", text="Pas de service en "
                                                                                                   "charge")
        self.info = Info(self.root,
                         border=0,
                         bg=self.bg_color,
                         width=width,
                         height=height * 67 // 640,
                         service_label=self.service_label)
        self.info.clock()
        # Digits Frame
        self.digit_frame = DigitPad(self.main_frame, 
                                    border=0, 
                                    bg="#3A393A", 
                                    width=width * 145 // 512, 
                                    height=height * 23 // 12, 
                                    x=width * 405 // 1024, 
                                    y=height * 83 // 640)
        self.digit_frame.addButtons()

        # Init Entry
        font[2] = ""
        self.input_entry = Entry(self.main_frame,
                                 font=font,
                                 bg="#313131",
                                 border=0,
                                 fg="white",
                                 insertbackground="white",
                                 width=6,
                                 relief="sunken",
                                 highlightthickness=0,
                                 validate="none"
                                 )
        self.input_entry.bind("<Key>", lambda e: "break")
        self.input_entry.bind("<KeyPress>", lambda e: "break")

        # Screen Configuration
        self.utils.loading_screen(self.canvas)
        self.root.after(500, lambda canvas=self.canvas: self.utils.loading_screen(canvas, "businfo_boot1.png"))
        self.root.after(1000, self.post_init)
        
        # App Loop
        self.root.mainloop()

    def post_init(self) -> None:
        self.utils.loading_screen(self.canvas, "businfo_ID_input.png", (0, height * 67 // 640, width, height))
        logging.info("Post Init, Logging Screen is on")
        # Info Init
        self.info.place()
        # Service place
        self.service_label.place(x=width * 5 // 1024, y=0)
        # Entry Init
        self.input_entry.place(x=17 * width // 1024, y=height * 11 // 32)
        # Digit Init
        self.digit_frame.place()

        screen_index = 0

        # Bind Command and DigitPad
        ButtonHandler(self.digit_frame, self.input_entry, self.info, self.canvas, screen_index)


if __name__ == "__main__":
    # logging.basicConfig(filename="businfo.log", filemode="w+", level=logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler())
    if sys.platform == 'linux':
        gui = GUI("linux")
    elif sys.platform == 'win32':
        gui = GUI("windows")
