import tkinter as tk


class WelcomePage(tk.Frame):
    """"""

    def __init__(self, parent, controller):
        """"""
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id

        label = tk.Label(self, text="Welcome Page", font=controller.titlefont)

        label.pack()

        bou = tk.Button(self, text="To Page 1",
                        command=lambda: controller.up_frame("PageOne"))

        bou.pack()
