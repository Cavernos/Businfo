import time
from tkinter import Frame, Label, Tk
from businfo.definitions import width as root_w, height as root_h


class Info:
    def __init__(self, panel: Frame | Tk, border: int, bg: str, width: int, height: int, service_label: Label):
        self.info = Frame(panel, border=border, bg=bg, width=width, height=height)
        self.font = ['US_MSFont_Faremaster', root_h * 5 // 128]
        self.bg_color = "#312D8C"
        self.width = root_w

        self.clock_label = Label(self.info, font=self.font, fg="white", bg=self.bg_color)
        self.font[1] = root_h // 32
        self.driver_label = Label(self.info, font=self.font, fg="white", bg=self.bg_color, text="Cn:000000")
        self.service_label = Label(self.info, font=self.font, fg="white", bg=self.bg_color, text="S:000000")
        self.destination_label = Label(self.info, font=self.font, fg="white", bg=self.bg_color, text="D:000")
        self.line_label = Label(self.info, font=self.font, fg="white", bg=self.bg_color, text="L:0000")

        self.service = service_label

    def getInfoFrame(self):
        return self.info

    def clock(self) -> None:
        time_live = time.strftime("%H:%M:%S")
        self.clock_label.config(text=time_live)
        self.clock_label.after(200, self.clock)

    def place(self):
        self.info.grid(row=0)
        self.clock_label.place(x=root_w * 5 // 1024, y=root_h * 5 // 640)
        label_width = [self.driver_label.winfo_reqwidth(),
                       self.service_label.winfo_reqwidth(),
                       self.destination_label.winfo_reqwidth(),
                       self.line_label.winfo_reqwidth()]
        self.driver_label.place(
            x=root_w - label_width[0] - label_width[1] - label_width[2] - label_width[3] - 20, y=root_h // 64)
        self.service_label.place(
            x=root_w - label_width[1] - label_width[2] - label_width[3] - 15, y=root_h // 64)
        self.destination_label.place(
            x=root_w - label_width[2] - label_width[3] - 10, y=root_h // 64)
        self.line_label.place(
            x=root_w - label_width[3] - 5, y=root_h // 64)

    def getDriverLabel(self):
        return self.driver_label

    def getServiceLabel(self):
        return self.service_label

    def getServiceInfo(self):
        return self.service

    def getDestinationLabel(self):
        return self.destination_label

    def getLineLabel(self):
        return self.line_label
