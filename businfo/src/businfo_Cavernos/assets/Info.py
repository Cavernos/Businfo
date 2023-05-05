import time
from tkinter import Frame, Label, Tk


class Info:
    def __init__(self, panel: Frame | Tk, border: int, bg: str, width: int, height: int, service_label: Label):
        self.info = Frame(panel, border=border, bg=bg, width=width, height=height)
        self.font = ['US_MSFont_Faremaster', 25]
        self.bg_color = "#312D8C"
        self.width = 1024

        self.clock_label = Label(self.info, font=self.font, fg="white", bg=self.bg_color)
        self.font[1] = 20
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
        self.clock_label.place(x=5, y=5)
        self.driver_label.place(x=5 * self.width / 8 - 60, y=10)
        self.service_label.place(x=5 * self.width / 8 + 80, y=10)
        self.destination_label.place(x=5 * self.width / 8 + 205, y=10)
        self.line_label.place(x=5 * self.width / 8 + 285, y=10)

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
