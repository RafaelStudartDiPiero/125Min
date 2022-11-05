import tkinter as tk
from tkinter import font as tkfont


class WelcomePage(tk.Frame):
    """"""

    def __init__(self, parent, controller):
        """"""
        tk.Frame.__init__(self, parent, bg="#0501A7")
        self.controller = controller
        self.id = controller.id

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        label = tk.Label(self, text="Seja bem-vindo!",
                         font=controller.titlefont, bg="#0501A7", fg="#FFFFFF")

        label.grid(column=1, row=0, sticky=tk.N, padx=5, pady=5, columnspan=2)

        b1 = tk.Button(self, text="Planejar rota",
                       command=lambda: controller.up_frame("PlanejarRota"), font=controller.buttonfont, bg="#FFFFFF")

        b1.grid(column=0, row=1, sticky=tk.N, padx=5, pady=5)

        b2 = tk.Button(self, text="Atualizar dados",
                       command=lambda: controller.up_frame("AtualizarDados"), font=controller.buttonfont, bg="#FFFFFF")

        b2.grid(column=1, row=1, sticky=tk.N, padx=5, pady=5)

        b3 = tk.Button(self, text="Instruções de uso",
                       command=lambda: controller.up_frame("Instrucoes"), font=controller.buttonfont, bg="#FFFFFF")

        b3.grid(column=2, row=1, sticky=tk.N, padx=5, pady=5)

        b4 = tk.Button(self, text="Fale conosco",
                       command=lambda: controller.up_frame("FaleConosco"), font=controller.buttonfont, bg="#FFFFFF")

        b4.grid(column=3, row=1, sticky=tk.N, padx=5, pady=5)

        label = tk.Label(
            self, text="125Min, planejando o seu futuro!", font=controller.descriptionfont, bg="#0501A7", fg="#FFFFFF")

        label.grid(column=1, row=2, sticky=tk.N, padx=5, pady=5, columnspan=2)
