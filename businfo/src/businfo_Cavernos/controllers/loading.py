from businfo.src.businfo_Cavernos.views.loading import LoadingView


class LoadingController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame: LoadingView = self.view.frames["loading"]
        self.model.auth.add_event_listeners("auth_changed", self.auth_state_listener)

    def auth_state_listener(self, event):
        if event.is_logged_in:
            self.frame.info.getDriverLabel().config(text="Cn:" + "{:06d}".format(int(event.current_user["id"])))
