import tkinter as tk


class PlanejarRota(tk.Frame):
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
        container2.pack(expand=True)

        container3 = tk.Frame(self, bg=controller.pagesbg)
        container3["pady"] = 5
        container3["padx"] = 5
        container3.pack(side="bottom", fill="x")

        container4 = tk.Frame(container3, bg=controller.pagesbg)
        container4["pady"] = 5
        container4["padx"] = 5
        container4.pack(side="top", fill="x")

        container5 = tk.Frame(container3, bg=controller.pagesbg)
        container5["pady"] = 5
        container5["padx"] = 5
        container5.pack(side="bottom", fill="x")

        label = tk.Label(container1, text="Planejar Rota",
                         font=controller.titlefont, bg=controller.pagesbg)
        label.pack(side="left", padx=20)

        question_label = tk.Label(container4, text="Não encontrou alguma agência",
                                  font=controller.descriptionfont, bg=controller.pagesbg)
        question_label.pack(side="left")

        register_bou = tk.Button(container5, text="Registrar nova agência", font=controller.buttonfont,
                                 command=lambda: controller.up_frame("AtualizarDados"), bg=controller.buttonbg, padx=40, height=2)
        register_bou.pack(side="left")

        inicial_bou = tk.Button(container5, text="Página Inicial", font=controller.buttonfont,
                                command=lambda: controller.up_frame("WelcomePage"), bg=controller.buttonbg, height=2)
        inicial_bou.pack(side="right")
