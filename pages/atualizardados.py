import tkinter as tk

from models.config import Config


class AtualizarDados(tk.Frame):
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
        container9.pack(side="bottom")

        label = tk.Label(container1, text="Atualizar Dados",
                         font=controller.titlefont, bg=self.bg)
        label.pack()

        config_label = tk.Label(container2, text="Configuração",
                                font=controller.descriptionfont, bg=self.bg)
        config_label.pack()

        alimentacao_label = tk.Label(container3, text="Alimentação:",
                                     font=controller.buttonfont, bg=self.bg)
        alimentacao_label.pack(side="left")
        self.alimentacao_entry = tk.Entry(container3)
        self.alimentacao_entry["width"] = 20
        self.alimentacao_entry["font"] = controller.buttonfont
        self.alimentacao_entry.pack(side="left")

        salario_label = tk.Label(container4, text="Salário:",
                                 font=controller.buttonfont, bg=self.bg)
        salario_label.pack(side="left")
        self.salario_entry = tk.Entry(container4)
        self.salario_entry["width"] = 20
        self.salario_entry["font"] = controller.buttonfont
        self.salario_entry.pack(side="left")

        hospedagem_label = tk.Label(container5, text="Hospedagem:",
                                    font=controller.buttonfont, bg=self.bg)
        hospedagem_label.pack(side="left")
        self.hospedagem_entry = tk.Entry(container5)
        self.hospedagem_entry["width"] = 20
        self.hospedagem_entry["font"] = controller.buttonfont
        self.hospedagem_entry.pack(side="left")

        custo_gasolina_label = tk.Label(container6, text="Valor da Gasolina:",
                                        font=controller.buttonfont, bg=self.bg)
        custo_gasolina_label.pack(side="left")
        self.custo_gasolina_entry = tk.Entry(container6)
        self.custo_gasolina_entry["width"] = 20
        self.custo_gasolina_entry["font"] = controller.buttonfont
        self.custo_gasolina_entry.pack(side="left")

        update_button = tk.Button(
            container7, text="Alterar", command=self.alterarConfig)
        update_button.pack()

        self.config_status_label = tk.Label(container8,
                                            font=controller.buttonfont, bg=self.bg)
        self.config_status_label.pack()

        bou = tk.Button(container9, text="To Welcome Page",
                        command=lambda: controller.up_frame("WelcomePage"))
        bou.pack()

    def alterarConfig(self):
        config = Config()
        config.selectConfig()

        config.alimentacao = float(self.alimentacao_entry.get())
        config.salario_hora = float(self.salario_entry.get())
        config.hospedagem = float(self.hospedagem_entry.get())
        config.custo_gasolina = float(self.custo_gasolina_entry.get())
        

        self.config_status_label["text"] = config.updateConfig

        self.alimentacao_entry.delete(0, tk.END)
        self.salario_entry.delete(0, tk.END)
        self.hospedagem_entry.delete(0, tk.END)
        self.custo_gasolina_entry.delete(0, tk.END)
