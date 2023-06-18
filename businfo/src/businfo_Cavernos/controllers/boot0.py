from businfo.src.businfo_Cavernos.views.boot0 import Boot0View


class Boot0Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame: Boot0View = self.view.frames["boot0"]

    def update_view(self):
        self.view.switch("boot1")
