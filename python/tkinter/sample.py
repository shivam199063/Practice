import tkinter as tk


class  Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("ImageProcessing")

App=Application()
App.mainloop()