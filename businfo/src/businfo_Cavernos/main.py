from businfo.src.businfo_Cavernos.controllers.main import Controller
from businfo.src.businfo_Cavernos.models.main import Model
from businfo.src.businfo_Cavernos.views.main import View

if __name__ == "__main__":
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.start()
