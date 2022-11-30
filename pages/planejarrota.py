import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from db.banco import Banco
from VRP import run_otimization
from functools import partial


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

        self.container2 = tk.Frame(self, bg=controller.pagesbg)
        self.container2["pady"] = 5
        self.container2["padx"] = 5
        self.container2.pack(expand=True)

        containerupdate = tk.Frame(self.container2, bg=controller.pagesbg)
        containerupdate["pady"] = 5
        containerupdate["padx"] = 5
        containerupdate.pack(side="bottom", fill="x")

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

        self.scroll = ScrolledText(self.container2, width=20, height=10)
        self.scroll.pack()

        planning_button = tk.Button(
            containerupdate, text="Planejar Rota", command=self.runOtimization, font=controller.buttonfont, bg=controller.buttonbg, height=2)
        planning_button.pack(side="bottom")

        update_button = tk.Button(
            containerupdate, text="Atualizar", command=self.updateListaAgencias, font=controller.buttonfont, bg=controller.buttonbg, height=2)
        update_button.pack(side="bottom")

        question_label = tk.Label(container4, text="Não encontrou alguma agência",
                                  font=controller.descriptionfont, bg=controller.pagesbg)
        question_label.pack(side="left")

        register_bou = tk.Button(container5, text="Registrar nova agência", font=controller.buttonfont,
                                 command=lambda: controller.up_frame("AdicionarAgencia"), bg=controller.buttonbg, padx=40, height=2)
        register_bou.pack(side="left")

        inicial_bou = tk.Button(container5, text="Página Inicial", font=controller.buttonfont,
                                command=lambda: controller.up_frame("WelcomePage"), bg=controller.buttonbg, height=2)
        inicial_bou.pack(side="right")

        self.check_box = []
        self.selected_boxes = []

    def choose(self, index, row):
        if self.var_list[index].get() == 1:
            self.selected_boxes.append(row)
        else:
            self.selected_boxes.remove(row)

    def updateListaAgencias(self):
        self.scroll.delete('1.0', tk.END)
        self.var_list = []
        self.selected_boxes = []
        banco = Banco()
        c = banco.conexao.cursor()
        c.execute(
            '''select * from agencias ''')

        for cb in self.check_box:
            cb.pack_forget()
            cb.destroy()

        self.check_box = []
        for index, row in enumerate(c):
            self.var_list.append(tk.IntVar(value=0))
            cb = tk.Checkbutton(self.scroll, variable=self.var_list[index],
                                text=row[4], command=partial(self.choose, index, row))
            self.check_box.append(cb)
            cb.pack()
            self.scroll.window_create('end', window=cb)
            self.scroll.insert('end', '\n')

    def runOtimization(self):
        self.selected_boxes.insert(0, (0, 'Rua Nunes Machado', '977', 'Araras', '13600-021'))
        run_otimization(self.selected_boxes)
