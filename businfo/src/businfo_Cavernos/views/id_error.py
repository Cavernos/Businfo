from tkinter import Frame, N, W, Canvas

from PIL import ImageTk

from businfo.definitions import width, height, font
from businfo.src.businfo_Cavernos.assets.Info import Info
from businfo.src.businfo_Cavernos.utils.utils import Utils


class IdErrorView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.utils = Utils()
        self.canvas = Canvas(self, width=width, height=height - 67, highlightthickness=0)
        self.canvas.create_image((0, 0), anchor=N + W)
        self.load_photo = ImageTk.PhotoImage(
            self.utils.load_image("businfo_ID_loading_error_WID", (0, height * 67 // 640, width, height)))
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
