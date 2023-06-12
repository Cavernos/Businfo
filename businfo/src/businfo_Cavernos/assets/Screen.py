from tkinter import Canvas, Label, Frame, Tk, END

from businfo.definitions import width, height, font
from businfo.src.businfo_Cavernos.utils.utils import Utils


class Screen:
    def __init__(self, root: Frame | Tk, index, info_list=None):
        self.index = index
        self.bg = []

        self.canvas = Canvas(root, width=width, height=height, highlightthickness=0)
        self.canvas.pack()
        self.bg_color = "#312D8C"
        self.utils = Utils()
        self.info_list = info_list
        self.service_label = Label(root.master, font=font, fg="white", bg="#3A393A", text="Pas de service en charge")

    def draw(self):
        match self.index:
            case 0:
                self.utils.loading_screen(self.canvas, self.bg[0])
            case 1:
                self.utils.loading_screen(self.canvas, self.bg[0])
            case 2:
                self.utils.loading_screen(self.canvas, self.bg[0], self.bg[1])

    def set_background(self):
        match self.index:
            case 0:
                self.bg = ["businfo_boot0.png"]
            case 1:
                self.bg = ["businfo_boot1.png"]
            case 2:
                self.bg = ["businfo_ID_input.png", (0, height * 67 // 640, width, height)]
                if self.info_list is not None:
                    for info in self.info_list:
                        if type(info) is tuple:
                            info[0].place(x=info[1], y=info[2])
                        else:
                            info.place()

    def set_info_list(self, info_list):
        self.info_list = info_list

    def get_info_list(self):
        return self.info_list

    def setId(self, index):
        self.index = index

    def getId(self):
        return self.index


