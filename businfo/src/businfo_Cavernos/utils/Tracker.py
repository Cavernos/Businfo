class Tracker:
    def __init__(self, toplevel):
        self.toplevel = toplevel
        self.width, self.height = toplevel.winfo_width(), toplevel.winfo_height()
        self._func_id = None
        self.ratio = [1, 1]

    def bind_config(self):
        self._func_id = self.toplevel.bind("<Configure>", self.resize)
        return self.ratio

    def unbind_config(self):  # Untested.
        if self._func_id:
            self.toplevel.unbind("<Configure>", self._func_id)
            self._func_id = None

    def resize(self, event):
        if(event.widget == self.toplevel and
           (self.width != event.width or self.height != event.height)):
            #print(f'{event.widget=}: {event.height=}, {event.width=}\n')
            self.ratio[0] = self.width / event.width 
            self.ratio[1] = self.height / event.height
            self.width, self.height = event.width, event.height
