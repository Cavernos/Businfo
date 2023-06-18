from businfo.src.businfo_Cavernos.views.boot1 import Boot1View


class Boot1Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame: Boot1View = self.view.frames["boot1"]

    def update_view(self):
        self.view.switch("login")
