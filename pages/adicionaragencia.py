import tkinter as tk
from models.agencia import Agencia


class AdicionarAgencia(tk.Frame):
    """"""

    def __init__(self, parent, controller):
        """"""
        tk.Frame.__init__(self, parent, bg="#E2E2E2")
        self.controller = controller
        self.id = controller.id

        self.bg = "#E2E2E2"

        container1 = tk.Frame(self, bg=self.bg)
        container1["pady"] = 5
        container1["pady"] = 5
        container1.pack()

        config_container = tk.Frame(self, bg=self.bg)
        config_container.pack(expand=True)

        container2 = tk.Frame(config_container, bg=self.bg)
        container2["pady"] = 5
        container2["padx"] = 20
        container2.pack()

        container3 = tk.Frame(config_container, bg=self.bg)
        container3["pady"] = 5
        container3["padx"] = 20
        container3.pack()

        container4 = tk.Frame(config_container, bg=self.bg)
        container4["pady"] = 5
        container4["padx"] = 5
        container4.pack()

        container5 = tk.Frame(config_container, bg=self.bg)
        container5["pady"] = 5
        container5["padx"] = 5
        container5.pack()

        container6 = tk.Frame(config_container, bg=self.bg)
        container6["pady"] = 5
        container6["padx"] = 5
        container6.pack()

        container7 = tk.Frame(config_container, bg=self.bg)
        container7["pady"] = 5
        container7["padx"] = 5
        container7.pack()

        container8 = tk.Frame(config_container, bg=self.bg)
        container8["pady"] = 5
        container8["padx"] = 5
        container8.pack()

        container9 = tk.Frame(self, bg=self.bg)
        container9["pady"] = 5
        container9["padx"] = 5
        container9.pack()

        container10 = tk.Frame(self, bg=self.bg)
        container10["pady"] = 5
        container10["padx"] = 5
        container10.pack()

        container11 = tk.Frame(self, bg=self.bg)
        container11["pady"] = 5
        container11["padx"] = 5
        container11.pack()

        container12 = tk.Frame(self, bg=self.bg)
        container12["pady"] = 5
        container12["padx"] = 5
        container12.pack()

        container13 = tk.Frame(self, bg=self.bg)
        container13["pady"] = 5
        container13["padx"] = 5
        container13.pack(side="bottom")

        label = tk.Label(container1, text="Agência",
                         font=controller.titlefont, bg=self.bg)
        label.pack()

        agencia_label = tk.Label(container2, text="Registrar Agência",
                                font=controller.descriptionfont, bg=self.bg)
        agencia_label.pack()

        rua_label = tk.Label(container3, text="Rua:",
                             font=controller.buttonfont, bg=self.bg)
        rua_label.pack(side="left")
        self.rua_entry = tk.Entry(container3)
        self.rua_entry["width"] = 20
        self.rua_entry["font"] = controller.buttonfont
        self.rua_entry.pack(side="left")

        numero_label = tk.Label(container4, text="Número:",
                             font=controller.buttonfont, bg=self.bg)
        numero_label.pack(side="left")
        self.numero_entry = tk.Entry(container4)
        self.numero_entry["width"] = 20
        self.numero_entry["font"] = controller.buttonfont
        self.numero_entry.pack(side="left")

        cidade_label = tk.Label(container5, text="Cidade:",
                             font=controller.buttonfont, bg=self.bg)
        cidade_label.pack(side="left")
        self.cidade_entry = tk.Entry(container5)
        self.cidade_entry["width"] = 20
        self.cidade_entry["font"] = controller.buttonfont
        self.cidade_entry.pack(side="left")

        cep_label = tk.Label(container6, text="CEP:",
                             font=controller.buttonfont, bg=self.bg)
        cep_label.pack(side="left")
        self.cep_entry = tk.Entry(container6)
        self.cep_entry["width"] = 20
        self.cep_entry["font"] = controller.buttonfont
        self.cep_entry.pack(side="left")

        create_button = tk.Button(
            container7, text="Adicionar", command=self.adicionarAgencia)
        create_button.pack()

        self.nova_agencia_status_label = tk.Label(container8,
                                            font=controller.buttonfont, bg=self.bg)
        self.nova_agencia_status_label.pack()

        agencia_label = tk.Label(container9, text="Excluir Agência",
                                 font=controller.descriptionfont, bg=self.bg)
        agencia_label.pack()

        cep2_label = tk.Label(container10, text="CEP:",
                             font=controller.buttonfont, bg=self.bg)
        cep2_label.pack(side="left")
        self.cep2_entry = tk.Entry(container10)
        self.cep2_entry["width"] = 20
        self.cep2_entry["font"] = controller.buttonfont
        self.cep2_entry.pack(side="left")

        delete_button = tk.Button(
            container11, text="Excluir", command=self.excluirAgencia)
        delete_button.pack()

        self.excluir_agencia_status_label = tk.Label(container12,
                                                  font=controller.buttonfont, bg=self.bg)
        self.excluir_agencia_status_label.pack()

        bou = tk.Button(container13, text="Voltar",
                        command=lambda: controller.up_frame("PlanejarRota"))
        bou.pack()

    def adicionarAgencia(self):
        agencia = Agencia()
        try:
            if agencia.cep != "":
                raise ValueError("Já existe uma agência com este CEP")
            if self.rua_entry.get() == "" or self.numero_entry.get() == "" or self.cidade_entry.get() == "" or self.cep_entry.get() == "":
                raise ValueError("Algum campo não foi preenchido")
            agencia.rua = self.rua_entry.get()
            agencia.numero = int(self.numero_entry.get())
            agencia.cidade = self.cidade_entry.get()
            agencia.cep = self.cep_entry.get()

        except ValueError as error:
            self.nova_agencia_status_label["text"] = error
            return

        self.nova_agencia_status_label["text"] = agencia.inserirAgencia()
        self.rua_entry.delete(0, tk.END)
        self.numero_entry.delete(0, tk.END)
        self.cidade_entry.delete(0, tk.END)
        self.cep_entry.delete(0, tk.END)

    def excluirAgencia(self):
        cep = self.cep2_entry.get()
        agencia = Agencia()
        agencia.selectAgencia(cep)
        if agencia.cep == "":
            self.excluir_agencia_status_label["text"] = "Essa agência não existe"
        else:
            self.excluir_agencia_status_label["text"] =  agencia.deleteAgencia
