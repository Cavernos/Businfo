from tkinter import Frame

from businfo.src.businfo_Cavernos.views.boot0 import Boot0View
from businfo.src.businfo_Cavernos.views.boot1 import Boot1View
from businfo.src.businfo_Cavernos.views.loading import LoadingView
from businfo.src.businfo_Cavernos.views.login import LoginView
from businfo.src.businfo_Cavernos.views.root import Root


# class View:
#     def __init__(self):
#         self.root = Root()
#         self.frame_classes = {
#             "boot0": Boot0View,
#             "boot1": Boot1View,
#             "login": LoginView
#         }
#         self.current_frame = None
#
#     def switch(self, name):
#         new_frame: Frame = self.frame_classes[name](self.root)
#         if self.current_frame is not None:
#             self.current_frame.destroy()
#         self.current_frame: Frame = new_frame
#         self.current_frame.grid(row=0, column=0, sticky="nsew")
#
#     def launch(self):
#         self.root.update()
#         self.root.update_idletasks()
#         self.root.mainloop()

class View:
    def __init__(self):
        self.root = Root()
        self.frames = {}
        self._add_frame(Boot0View, "boot0")
        self._add_frame(Boot1View, "boot1")
        self._add_frame(LoginView, "login")
        self._add_frame(LoadingView, "loading")

    def _add_frame(self, Frame, name):
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def launch(self):
        self.root.update()
        self.root.update_idletasks()
        self.root.mainloop()
