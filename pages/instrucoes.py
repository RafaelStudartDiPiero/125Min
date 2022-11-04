import tkinter as tk


class Instrucoes(tk.Frame):
    """"""

    def __init__(self, parent, controller):
        """"""
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id

        label = tk.Label(self, text="Instruções de Uso", font=controller.titlefont)

        label.pack()

        bou = tk.Button(self, text="To Welcome Page",
                        command=lambda: controller.up_frame("WelcomePage"))

        bou.pack()