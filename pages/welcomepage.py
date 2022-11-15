import tkinter as tk
from tkinter import font as tkfont


class WelcomePage(tk.Frame):
    """"""

    def __init__(self, parent, controller):
        """"""
        tk.Frame.__init__(self, parent, bg="#0501A7")
        self.controller = controller
        self.id = controller.id

        self.bg = "#0501A7"

        container1 = tk.Frame(self, bg=self.bg)
        container1["pady"] = 5
        container1["pady"] = 5
        container1.pack()

        container2 = tk.Frame(self, bg=self.bg)
        container2["pady"] = 5
        container2["padx"] = 5
        container2.pack(expand=True)

        container3 = tk.Frame(self, bg=self.bg)
        container3["pady"] = 5
        container3["padx"] = 5
        container3.pack(side="bottom")

        label = tk.Label(container1, text="Seja bem-vindo!",
                         font=controller.titlefont, bg=self.bg, fg="#FFFFFF")
        label.pack()

        b1 = tk.Button(container2, text="Planejar rota",
                       command=lambda: controller.up_frame("PlanejarRota"), font=controller.buttonfont, bg=controller.buttonbg, height=2)
        b1.pack(side="left", padx=20)

        b2 = tk.Button(container2, text="Atualizar dados",
                       command=lambda: controller.up_frame("AtualizarDados"), font=controller.buttonfont, bg=controller.buttonbg, height=2)
        b2.pack(side="left", padx=20)

        b3 = tk.Button(container2, text="Instruções de uso",
                       command=lambda: controller.up_frame("Instrucoes"), font=controller.buttonfont, bg=controller.buttonbg, height=2)
        b3.pack(side="left", padx=20)

        b4 = tk.Button(container2, text="Fale conosco",
                       command=lambda: controller.up_frame("FaleConosco"), font=controller.buttonfont, bg=controller.buttonbg, height=2)
        b4.pack(side="left", padx=20)

        des_label = tk.Label(
            container3, text="125Min, planejando o seu futuro!", font=controller.descriptionfont, bg=self.bg, fg="#FFFFFF")
        des_label.pack()
