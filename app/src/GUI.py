from tkinter import *
import logging
from app.src.assets.DigitPad import DigitPad
from app.src.assets.Info import Info
from app.src.handlers.ButtonsHandler import ButtonHandler
from app.src.utils.utils import Utils


class GUI(object):
    def __init__(self) -> None:
        # Init Window

        self.root = Tk()
        self.root.geometry("1024x640")
        self.root.title("businfo")
        self.root.resizable(True, True)
        self.root.update()
        logging.info("Window Init Successfully")

        # Some Definition
        self.font = ['US_MSFont_Faremaster', 25, "italic"]
        self.bg_color = "#312D8C"
        self.width = self.root.winfo_width()
        self.height = self.root.winfo_height()
        self.utils = Utils()

        # Init First Frame
        self.main_frame = Frame(self.root, height=640)
        self.main_frame.grid(row=1)

        # Init Canvas for images
        self.canvas = Canvas(self.main_frame, width=1024, height=640, highlightthickness=0)
        self.canvas.pack()

        # Infos Frame
        self.info = Info(self.root, border=0, bg=self.bg_color, width=1024, height=67)
        self.info.clock()

        # Service Info
        self.service_label = Label(self.main_frame, font=self.font, fg="white", bg="#3A393A", text="Pas de service en charge")

        # Digits Frame
        self.digit_frame = DigitPad(self.main_frame, border=0, bg="#3A393A", width=290, height=460, x=405, y=83)
        self.digit_frame.addButtons()

        # Init Entry
        self.font[2] = ""
        self.input_entry = Entry(self.main_frame,
                                 font=self.font,
                                 bg="#313131",
                                 border=0,
                                 insertbackground="white",
                                 fg="white",
                                 width=6
                                 )
        self.input_entry.bind("<Key>", lambda e: "break")

        # Screen Configuration
        self.utils.loading_screen(self.canvas)
        self.root.after(500, lambda canvas=self.canvas: self.utils.loading_screen(canvas, "businfo_boot1.png"))
        self.root.after(1000, self.post_init)
        # App Loop
        self.root.mainloop()

    def post_init(self) -> None:
        self.utils.loading_screen(self.canvas, "businfo_ID_input.png", (0, 67, 1024, 640))
        logging.info("Post Init, Logging Screen is on")
        # Info Init
        self.info.place()
        # Service place
        self.service_label.place(x=5, y=0)
        # Entry Init
        self.input_entry.place(x=17, y=220)
        # Digit Init
        self.digit_frame.place()

        screen_index = 0

        # Bind Command and DigitPad
        ButtonHandler(self.digit_frame, self.input_entry, self.info, self.canvas, screen_index)


if __name__ == "__main__":
    logging.basicConfig(filename="../businfo.log", filemode="w+", level=logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler())
    gui = GUI()
