from tkinter import *


class UI:
    def __init__(self):
        self.THEME_COLOR = "#375362"
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=self.THEME_COLOR)
        self.start()

    def start(self):
        self.window.mainloop()



