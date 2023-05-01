import datetime
from tkinter import END, Canvas, Entry

from app.src.assets.DigitPad import DigitPad
from app.src.assets.Info import Info
from app.src.assets.ProgressBar import ProgressBar
from app.src.utils.utils import Utils


class ServiceHandler:
    def __init__(self, canvas: Canvas, progress_bar: ProgressBar, info: Info, entry: Entry, digit_pad: DigitPad):
        self.active_service = False
        self.utils = Utils()
        self.canvas = canvas
        self.info = info
        self.entry = entry
        self.progress_bar = progress_bar
        self.digit_pad = digit_pad

    def service(self):
        self.utils.loading_screen(self.canvas, "businfo_service_input.png", (0, 67, 1024, 640))
        self.digit_pad.place()
        self.entry.place(x=17, y=220)

    def service_search(self, service_int):
        self.utils.loading_screen(self.canvas, "businfo_service_loading.png", (0, 67, 1024, 640))
        self.progress_bar.getBar().place(x=20, y=190)
        self.progress_bar.progress_start()
        services = {"number": 2,
                    "line": 20,
                    "start": "Congress \t  \t Ibk",
                    "dest": "Hungerburg \t \t Ibk",
                    "next_start": "19:15:00",
                    "stops": [
                        "Saint Marc"
                    ]
                    }
        if int(service_int) == services["number"]:
            gprs = True
        else:
            gprs = False
        if gprs:
            self.progress_bar.getBar().place_forget()
            self.service_found(services)
        else:
            self.progress_bar.getBar().place_forget()
            self.utils.loading_screen(self.canvas, "businfo_service_loading_error_gprs.png", (0, 67, 1024, 640))
            self.canvas.after(2000, self.service_not_found)

    def service_found(self, services: dict):
        self.active_service = True
        self.info.getServiceLabel().config(text="S:" + "{:06d}".format(int(services["number"])))
        self.info.getServiceInfo().config(text="Dest: " + services["dest"])
        next_start = datetime.datetime.strptime(services["next_start"], "%H:%M:%S").replace(year=2000).timestamp()
        now = datetime.datetime.now().timestamp()
        if next_start < now:
            self.entry.place_forget()
            self.entry.delete(0, END)
            self.digit_pad.removeDigitPad()
            self.digit_pad.removeButtons()
            self.utils.loading_screen(self.canvas, "businfo_service_recap_r.png", (0, 67, 1024, 640))
        # TODO
        pass

    def service_not_found(self):
        self.utils.loading_screen(self.canvas, "businfo_service_input.png", (0, 67, 1024, 640))
        self.info.getServiceLabel().config(text="S:000000")
        self.entry.place(x=17, y=220)
