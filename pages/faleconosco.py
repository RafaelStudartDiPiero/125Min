import tkinter as tk


class FaleConosco(tk.Frame):
    """"""

    def __init__(self, parent, controller):
        """"""
        tk.Frame.__init__(self, parent, bg=controller.pagesbg)
        self.controller = controller
        self.id = controller.id

        container1 = tk.Frame(self, bg=controller.pagesbg)
        container1["pady"] = 5
        container1["pady"] = 5
        container1.pack(fill="x")

        container2 = tk.Frame(self, bg=controller.pagesbg)
        container2["pady"] = 5
        container2["padx"] = 5
        container2.pack(fill="both", expand=True)

        message_container = tk.Frame(container2, bg=controller.pagesbg)
        message_container["pady"] = 5
        message_container["padx"] = 5
        message_container.pack(fill="x")

        container3 = tk.Frame(self, bg=controller.pagesbg)
        container3["pady"] = 5
        container3["padx"] = 5
        container3.pack(side="bottom", fill="x")

        label = tk.Label(container1, text="Fale Conosco",
                         font=controller.titlefont, bg=controller.pagesbg)
        label.pack(side="left", padx=20)

        message_label = tk.Label(message_container, text="""Encontrou algum problema no uso do 125Min?Por favor,nos avise!
        Telefone: +55 (18) 98129-4701
        E-mail: romulo.borio@ga.ita.br""",
                                 font=controller.descriptionfont, bg=controller.pagesbg)
        message_label.pack(side="left", padx=20)

        bou = tk.Button(container3, text="Página Inicial", font=controller.buttonfont,
                        command=lambda: controller.up_frame("WelcomePage"), bg=controller.buttonbg, height=2)
        bou.pack(side="right")
