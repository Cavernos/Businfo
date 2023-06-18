import time

from businfo.src.businfo_Cavernos.controllers.boot0 import Boot0Controller
from businfo.src.businfo_Cavernos.controllers.boot1 import Boot1Controller
from businfo.src.businfo_Cavernos.controllers.loading import LoadingController
from businfo.src.businfo_Cavernos.controllers.login import LoginController
from businfo.src.businfo_Cavernos.models.main import Model
from businfo.src.businfo_Cavernos.views.main import View


class Controller:
    def __init__(self, model: Model, view: View):
        self.view = view
        self.model = model
        self.boot0_controller = Boot0Controller(model, view)
        self.boot1_controller = Boot1Controller(model, view)
        self.login_controller = LoginController(model, view)
        self.loading_controller = LoadingController(model, view)

        self.model.auth.add_event_listeners("auth_changed", self.auth_state_listener)

    def auth_state_listener(self, data):
        self.view.switch("loading")
        self.view.root.after(20, self.loading_controller.frame.progress_bar.progress_start)
        if data.is_logged_in:
            self.view.root.after(1000, self.view.switch, "action")
        else:
            self.view.root.after(1000, self.view.switch, "id_error")
            self.view.root.after(3000, self.view.switch, "login")

    def start(self):
        self.view.switch("boot0")
        self.view.root.after(500, self.boot0_controller.update_view)
        self.view.root.after(1000, self.boot1_controller.update_view)
        self.view.launch()
