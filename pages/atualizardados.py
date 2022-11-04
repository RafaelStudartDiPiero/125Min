import tkinter as tk


class AtualizarDados(tk.Frame):
    """"""

    def __init__(self, parent, controller):
        """"""
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id

        label = tk.Label(self, text="Atualizar Dados", font=controller.titlefont)

        label.pack()

        bou = tk.Button(self, text="To Welcome Page",
                        command=lambda: controller.up_frame("WelcomePage"))

        bou.pack()