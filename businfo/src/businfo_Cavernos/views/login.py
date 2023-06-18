from tkinter import Frame, Canvas, N, W, Entry, Label

from PIL import ImageTk

from businfo.definitions import height, width, font
from businfo.src.businfo_Cavernos.assets.DigitPad import DigitPad
from businfo.src.businfo_Cavernos.assets.Info import Info
from businfo.src.businfo_Cavernos.utils.utils import Utils


class LoginView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.utils = Utils()

        # Canvas
        self.canvas = Canvas(self, width=width, height=height - 67, highlightthickness=0)
        self.canvas.create_image((0, 0), anchor=N + W)
        self.load_photo = ImageTk.PhotoImage(
            self.utils.load_image("businfo_ID_input", (0, height * 67 // 640, width, height)))
        self.canvas.itemconfig(1, image=self.load_photo)
        self.canvas.create_text((width * 200 // 1024, height * 5 // 128), font=font, text="Pas de service en charge",
                                fill="white")
        self.canvas.pack(side="bottom")

        # Info
        self.info = Info(self,
                         border=0,
                         bg="#312D8C",
                         width=width,
                         height=height * 67 // 640)
        self.info.clock()
        self.info.place()



        # DigitPad
        self.digit_pad = DigitPad(self, border=0,
                                  bg="#3A393A",
                                  width=width * 145 // 512,
                                  height=height * 23 // 12,
                                  x=width * 405 // 1024,
                                  y=height * 150 // 640)
        self.digit_pad.addButtons()
        self.digit_pad.place()

        # Entry
        self.entry = Entry(self, font=font,
                           bg="#313131",
                           border=0,
                           fg="white",
                           insertbackground="white",
                           width=6,
                           relief="sunken",
                           highlightthickness=0,
                           validate="none")
        self.entry.bind("<Key>", lambda e: "break")
        self.entry.bind("<KeyPress>", lambda e: "break")
        self.entry.place(x=17 * width // 1024, y=height * 287 // 640)
