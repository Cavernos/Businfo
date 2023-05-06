import time
from datetime import datetime
from tkinter import END, Canvas, Entry, Label, N, W

from PIL import ImageTk

from businfo.src.businfo_Cavernos.assets.DigitPad import DigitPad
from businfo.src.businfo_Cavernos.assets.Info import Info
from businfo.src.businfo_Cavernos.assets.ProgressBar import ProgressBar
from businfo.src.businfo_Cavernos.handlers.FileHandler import FileHandler
from businfo.src.businfo_Cavernos.utils.utils import Utils
from businfo.definitions import font, ROOT_DIR


class ServiceHandler:
    def __init__(self, canvas: Canvas, progress_bar: ProgressBar, info: Info, entry: Entry, digit_pad: DigitPad):
        self.screen = ""
        self.file_handler = FileHandler("service.json")
        self.services = self.file_handler.decode()
        self.active_service = False
        self.utils = Utils()
        self.canvas = canvas
        self.info = info
        self.entry = entry
        self.progress_bar = progress_bar
        self.digit_pad = digit_pad

        self.dest_label = Label(self.canvas, font=font, fg="white", bg="#313131")
        self.start_label = Label(self.canvas, font=font, fg="white", bg="#313131")
        self.late_label = Label(self.canvas, font=font, fg="white", bg="#313131")
        self.stops_label = []
        for i in range(len(self.services["stops"])):
            self.stops_label.append(Label(self.canvas,
                                          font=font,
                                          fg="white",
                                          bg="#3A393A",
                                          text=self.services["stops"][str(i)]["name"]))
        self.arrow = Label(self.canvas, font=font, fg="white", bg="#3A393A")

    def service(self):
        self.utils.loading_screen(self.canvas, "businfo_service_input.png", (0, 67, 1024, 640))
        self.digit_pad.place()
        self.entry.place(x=17, y=220)

    def service_search(self, service_int):
        self.utils.loading_screen(self.canvas, "businfo_service_loading.png", (0, 67, 1024, 640))
        self.progress_bar.getBar().place(x=20, y=190)
        self.progress_bar.progress_start()
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
            self.info.getLineLabel().config(text="L:" + str(services["line"]))
            self.info.getDestinationLabel().config(text="D:" + "{:03d}".format(int(services["ziel"])))
        else:
            self.info.getDestinationLabel().config(text="D:000")
            self.info.getLineLabel().config(text="L:0000")
            self.info.getServiceLabel().config(text="S:000000")
        self.info.getServiceInfo().config(text="Dest: " + services["dest"])
        self.start_label.config(text=services["start"])
        self.dest_label.config(text=services["dest"])
        self.recap()

    def service_not_found(self):
        self.utils.loading_screen(self.canvas, "businfo_service_input.png", (0, 67, 1024, 640))
        self.info.getServiceLabel().config(text="S:000000")
        self.info.getLineLabel().config(text="L:0000")
        self.info.getDestinationLabel().config(text="D:000")
        self.entry.place(x=17, y=220)

    def recap(self):
        self.screen = "recap"
        self.entry.place_forget()
        self.entry.delete(0, END)
        self.digit_pad.removeDigitPad()
        self.digit_pad.removeButtons()
        self.dest_label.place(x=17, y=178 + 67 / 2 - 25)
        self.start_label.place(x=17, y=315 + 67 / 2 - 25)
        self.late_label.place(x=17, y=458 + 67 / 2 - 25)
        self.late()

    def main_page(self):
        self.screen = "main"
        match len(self.services["stops"]):
            case 1:
                self.load_main_page(1)
            case 2:
                self.load_main_page(2)
            case 3:
                self.load_main_page(3)
            case _:
                self.load_main_page(4)

    def load_main_page(self, index):
        for i in range(0, 3):
            self.getServiceInfo()[i].place_forget()
        self.utils.loading_screen(self.canvas, f"businfo_service_main{index}.png", (0, 67, 1024, 640))
        if index == 4:
            index = index - 1
        for i in range(0, index):
            self.stops_label[i].place(x=192, y=391 - 83 * i)
        self.late_label.place(x=192, y=458 + 67 / 2 - 25)
        self.late()
        self.arrow.place(x=0, y=315)

    def late(self):
        if self.file_handler.file_update():
            self.services = self.file_handler.decode()
        now = datetime.strptime(time.strftime("%H:%M:%S"), "%H:%M:%S")
        next_start = self.services["next_start"]
        if self.screen == "recap":
            late = (now - datetime.strptime(next_start, "%H:%M:%S")).total_seconds()
            if now > datetime.strptime(next_start, "%H:%M:%S"):
                time_late = "+ " + "{:02d}:{:02d}:{:02d}".format(int(late // 3600), int(late % 3600 // 60),
                                                                 int(late % 60))
                self.utils.loading_screen(self.canvas, "businfo_service_recap_r.png", (0, 67, 1024, 640))

            else:
                advance = - late
                time_late = "- " + "{:02d}:{:02d}:{:02d}".format(int(advance // 3600), int(advance % 3600 // 60),
                                                                 int(advance % 60))
                self.utils.loading_screen(self.canvas, "businfo_service_recap_a.png", (0, 67, 1024, 640))
            self.late_label.config(text=next_start + "\t (" + time_late + ")")
            self.late_label.after(200, self.late)

        elif self.screen == "main":
            if now > datetime.strptime(self.services["stops"]["0"]["horaire"], "%H:%M:%S"):
                late = (now - datetime.strptime(self.services["stops"]["0"]["horaire"], "%H:%M:%S")).total_seconds()
                time_late = "+ " + "{:02d}:{:02d}".format(int(late // 60), int(late % 60))
                if int(late // 60) >= 2:
                    self.image = ImageTk.PhotoImage(self.utils.load_image("fleches.png", (260, 0, 389, 200)))
                    self.arrow.config(image=self.image)
                if len(self.services["stops"]) >= 3:
                    self.utils.loading_screen(self.canvas,
                                              f"businfo_service_main4_r.png",
                                              (0, 67, 1024, 640))
                else:
                    self.utils.loading_screen(self.canvas,
                                              f"businfo_service_main{len(self.services['stops'])}_r.png",
                                              (0, 67, 1024, 640))
            else:
                late = (datetime.strptime(self.services["stops"]["0"]["horaire"], "%H:%M:%S") - now).total_seconds()
                time_late = "- " + "{:02d}:{:02d}".format(int(late // 60), int(late % 60))
                if int(late // 60) >= 3:
                    self.image = ImageTk.PhotoImage(self.utils.load_image("fleches.png", (140, 0, 260, 200)))
                    self.arrow.config(image=self.image)
                elif 0 < int(late // 60) < 3:
                    self.image = ImageTk.PhotoImage(self.utils.load_image("fleches.png", (389, 0, 518, 200)))
                    self.arrow.config(image=self.image)
                if len(self.services["stops"]) >= 3:
                    self.utils.loading_screen(self.canvas,
                                              f"businfo_service_main4_a.png",
                                              (0, 67, 1024, 640))
                else:
                    self.utils.loading_screen(self.canvas,
                                              f"businfo_service_main{len(self.services['stops'])}_a.png",
                                              (0, 67, 1024, 640))
            self.late_label.config(text=time_late)
            self.late_label.after(200, self.late)

    def getServiceInfo(self):
        return [self.late_label, self.start_label, self.dest_label, self.arrow, self.stops_label]

    def setScreen(self, screen):
        self.screen = screen
