import inspect
from tkinter import END

from businfo.src.businfo_Cavernos.views.login import LoginView


class LoginController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame: LoginView = self.view.frames["login"]
        self._bind()

    def _bind(self):
        self.digit_buttons = self.frame.digit_pad.getButtons()
        for i in range(0, 13):
            self.digit_buttons[i].config(command=lambda j=i: self._digit_push(j))

    def push(self):
        print("hello world")

    def _digit_push(self, index):
        match index:
            case 0:
                self.frame.entry.insert(END, "1")
                print("je suis appelé 2")
            case 1:
                self.frame.entry.insert(END, "2")
            case 2:
                self.frame.entry.insert(END, "3")
            case 3:
                self.frame.entry.insert(END, "4")
            case 4:
                self.frame.entry.insert(END, "5")
            case 5:
                self.frame.entry.insert(END, "6")
            case 6:
                self.frame.entry.insert(END, "7")
            case 7:
                self.frame.entry.insert(END, "8")
            case 8:
                self.frame.entry.insert(END, "9")
            case 9:
                last_character = self.frame.entry.get()[0:6][:-1]
                self.frame.entry.delete(len(last_character), END)
            case 10:
                self.frame.entry.insert(END, "0")
            case 11:
                self.frame.entry.delete(0, END)
            case 12:
                self.signin()

    def signin(self):
        user_id = self.frame.entry.get()[0:6]
        data = {"id": user_id}
        print(data)
        self.model.auth.login(data)
