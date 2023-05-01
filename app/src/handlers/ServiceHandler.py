import time
from datetime import datetime
from tkinter import END, Canvas, Entry, Label

from app.src.assets.DigitPad import DigitPad
from app.src.assets.Info import Info
from app.src.assets.ProgressBar import ProgressBar
from app.src.utils.utils import Utils
from definitions import font


class ServiceHandler:
    def __init__(self, canvas: Canvas, progress_bar: ProgressBar, info: Info, entry: Entry, digit_pad: DigitPad):
        self.screen = "recap"
        self.services = {}
        self.active_service = False
        self.utils = Utils()
        self.canvas = canvas
        self.info = info
        self.entry = entry
        self.progress_bar = progress_bar
        self.digit_pad = digit_pad

        self.dest_label = Label(self.canvas, font=font, fg="white", bg="#313131")
        self.start_label = Label(self.canvas, font=font, fg="white", bg="#313131")
        self.late_label = Label(self.canvas, font=font, fg="white", bg="#313131", wraplength=496)

    def service(self):
        self.utils.loading_screen(self.canvas, "businfo_service_input.png", (0, 67, 1024, 640))
        self.digit_pad.place()
        self.entry.place(x=17, y=220)

    def service_search(self, service_int):
        self.utils.loading_screen(self.canvas, "businfo_service_loading.png", (0, 67, 1024, 640))
        self.progress_bar.getBar().place(x=20, y=190)
        self.progress_bar.progress_start()
        self.services = {"number": 2,
                    "line": 20,
                    "ziel": 200,
                    "start": "Congress \t  \t Ibk",
                    "dest": "Hungerburg \t \t Ibk",
                    "next_start": "19:15:00",
                    "stops": [
                        "Saint Marc"
                    ]
                    }
        if int(service_int) == self.services["number"]:
            gprs = True
        else:
            gprs = False
        if gprs:
            self.progress_bar.getBar().place_forget()
            self.service_found(self.services)
        else:
            self.progress_bar.getBar().place_forget()
            self.utils.loading_screen(self.canvas, "businfo_service_loading_error_gprs.png", (0, 67, 1024, 640))
            self.canvas.after(2000, self.service_not_found)

    def service_found(self, services: dict):
        self.active_service = True
        if "number" in services or "line" in services or "ziel" in services:
            self.info.getServiceLabel().config(text="S:" + "{:06d}".format(int(services["number"])))
            self.info.getLineLabel().config(text="L:" + "{:04d}".format(int(services["line"])))
            self.info.getDestinationLabel().config(text="D:" + "{:03d}".format(int(services["ziel"])))
        else:
            self.info.getDestinationLabel().config(text="D:000")
            self.info.getLineLabel().config(text="L:0000")
            self.info.getServiceLabel().config(text="S:000000")
        self.info.getServiceInfo().config(text="Dest: " + services["dest"])
        self.start_label.config(text=services["start"])
        self.dest_label.config(text=services["dest"])
        self.late(services["next_start"])
        self.recap(services["next_start"])

    def service_not_found(self):
        self.utils.loading_screen(self.canvas, "businfo_service_input.png", (0, 67, 1024, 640))
        self.info.getServiceLabel().config(text="S:000000")
        self.info.getLineLabel().config(text="L:0000")
        self.info.getDestinationLabel().config(text="D:000")
        self.entry.place(x=17, y=220)

    def recap(self, next_start="19:15:00"):
        self.screen = "recap"
        self.entry.place_forget()
        self.entry.delete(0, END)
        self.digit_pad.removeDigitPad()
        self.digit_pad.removeButtons()
        next_start_format = datetime.strptime(next_start, "%H:%M:%S")
        now = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
        self.dest_label.place(x=17, y=178 + 67 / 2 - 25)
        self.start_label.place(x=17, y=315 + 67 / 2 - 25)
        self.late_label.place(x=17, y=458 + 67 / 2 - 25)
        if next_start_format < now:
            self.utils.loading_screen(self.canvas, "businfo_service_recap_r.png", (0, 67, 1024, 640))
        else:
            self.utils.loading_screen(self.canvas, "businfo_service_recap_a.png", (0, 67, 1024, 640))

    def late(self, next_start):
        now = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
        if now > datetime.strptime(next_start, "%H:%M:%S"):
            time_late = "+ " + str(now - datetime.strptime(next_start, "%H:%M:%S"))
        else:
            time_late = "- " + str(datetime.strptime(next_start, "%H:%M:%S") - now)
        self.late_label.config(text=next_start + "\t (" + str(time_late) + ")")
        self.late_label.after(200, self.late, next_start)

    def getRecapInfo(self):
        return [self.late_label, self.start_label, self.dest_label]
