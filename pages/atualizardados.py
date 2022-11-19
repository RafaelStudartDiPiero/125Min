import tkinter as tk

from models.config import Config


class AtualizarDados(tk.Frame):
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

        config_container = tk.Frame(self, bg=controller.pagesbg)
        config_container.pack(expand=True)

        container2 = tk.Frame(config_container, bg=controller.pagesbg)
        container2["pady"] = 5
        container2["padx"] = 20
        container2.pack()

        container3 = tk.Frame(config_container, bg=controller.pagesbg)
        container3["pady"] = 5
        container3["padx"] = 20
        container3.pack()

        container4 = tk.Frame(config_container, bg=controller.pagesbg)
        container4["pady"] = 5
        container4["padx"] = 5
        container4.pack()

        container5 = tk.Frame(config_container, bg=controller.pagesbg)
        container5["pady"] = 5
        container5["padx"] = 5
        container5.pack()

        container6 = tk.Frame(config_container, bg=controller.pagesbg)
        container6["pady"] = 5
        container6["padx"] = 5
        container6.pack()

        container7 = tk.Frame(config_container, bg=controller.pagesbg)
        container7["pady"] = 5
        container7["padx"] = 5
        container7.pack()

        container8 = tk.Frame(config_container, bg=controller.pagesbg)
        container8["pady"] = 5
        container8["padx"] = 5
        container8.pack()

        container9 = tk.Frame(config_container, bg=controller.pagesbg)
        container9["pady"] = 5
        container9["padx"] = 5
        container9.pack()

        container10 = tk.Frame(self, bg=controller.pagesbg)
        container10["pady"] = 5
        container10["padx"] = 5
        container10.pack(side="bottom", fill="x")

        label = tk.Label(container1, text="Atualizar Dados",
                         font=controller.titlefont, bg=controller.pagesbg)
        label.pack(side="left", padx=20)

        config_label = tk.Label(container2, text="Configuração",
                                font=controller.descriptionfont, bg=controller.pagesbg)
        config_label.pack()

        consumo_comb_label = tk.Label(container3, text="Consumo Combustível:",
                                      font=controller.buttonfont, bg=controller.pagesbg)
        consumo_comb_label.pack(side="left")
        self.consumo_comb_entry = tk.Entry(container3)
        self.consumo_comb_entry["width"] = 20
        self.consumo_comb_entry["font"] = controller.buttonfont
        self.consumo_comb_entry.pack(side="left")
        self.consumo_comb_current = tk.Label(container3,
                                             font=controller.buttonfont, bg=controller.pagesbg)
        self.consumo_comb_current.pack(side="left")

        tempo_manutencao_label = tk.Label(container4, text="Tempo Manutenção:",
                                          font=controller.buttonfont, bg=controller.pagesbg)
        tempo_manutencao_label.pack(side="left")
        self.tempo_manutencao_entry = tk.Entry(container4)
        self.tempo_manutencao_entry["width"] = 20
        self.tempo_manutencao_entry["font"] = controller.buttonfont
        self.tempo_manutencao_entry.pack(side="left")
        self.tempo_manutencao_current = tk.Label(container4,
                                                 font=controller.buttonfont, bg=controller.pagesbg)
        self.tempo_manutencao_current.pack(side="left")

        salario_label = tk.Label(container5, text="Salário:",
                                 font=controller.buttonfont, bg=controller.pagesbg)
        salario_label.pack(side="left")
        self.salario_entry = tk.Entry(container5)
        self.salario_entry["width"] = 20
        self.salario_entry["font"] = controller.buttonfont
        self.salario_entry.pack(side="left")
        self.salario_current = tk.Label(container5,
                                        font=controller.buttonfont, bg=controller.pagesbg)
        self.salario_current.pack(side="left")

        hospedagem_label = tk.Label(container6, text="Hospedagem:",
                                    font=controller.buttonfont, bg=controller.pagesbg)
        hospedagem_label.pack(side="left")
        self.hospedagem_entry = tk.Entry(container6)
        self.hospedagem_entry["width"] = 20
        self.hospedagem_entry["font"] = controller.buttonfont
        self.hospedagem_entry.pack(side="left")
        self.hospedagem_current = tk.Label(container6,
                                           font=controller.buttonfont, bg=controller.pagesbg)
        self.hospedagem_current.pack(side="left")

        custo_gasolina_label = tk.Label(container7, text="Valor da Gasolina:",
                                        font=controller.buttonfont, bg=controller.pagesbg)
        custo_gasolina_label.pack(side="left")
        self.custo_gasolina_entry = tk.Entry(container7)
        self.custo_gasolina_entry["width"] = 20
        self.custo_gasolina_entry["font"] = controller.buttonfont
        self.custo_gasolina_entry.pack(side="left")
        self.custo_gasolina_current = tk.Label(container7,
                                               font=controller.buttonfont, bg=controller.pagesbg)
        self.custo_gasolina_current.pack(side="left")

        update_button = tk.Button(
            container8, text="Alterar", command=self.alterarConfig, font=controller.buttonfont, bg=controller.buttonbg, height=2)
        update_button.pack()

        self.config_status_label = tk.Label(container9,
                                            font=controller.buttonfont, bg=controller.pagesbg)
        self.config_status_label.pack()

        bou = tk.Button(container10, text="Página Inicial",
                        command=lambda: controller.up_frame("WelcomePage"), font=controller.buttonfont, bg=controller.buttonbg, height=2)
        bou.pack(side="right")

    def alterarConfig(self):
        config = Config()
        config.selectConfig()

        try:
            config.consumo_combustivel = float(self.consumo_comb_entry.get(
            )) if self.consumo_comb_entry.get() != "" else config.consumo_combustivel
            config.tempo_manutencao = float(self.tempo_manutencao_entry.get(
            )) if self.tempo_manutencao_entry.get() != "" else config.tempo_manutencao
            config.salario_hora = float(
                self.salario_entry.get()) if self.salario_entry.get() != "" else config.salario_hora
            config.hospedagem = float(self.hospedagem_entry.get(
            )) if self.hospedagem_entry.get() != "" else config.hospedagem
            config.custo_gasolina = float(self.custo_gasolina_entry.get(
            )) if self.custo_gasolina_entry.get() != "" else config.custo_gasolina
        except:
            self.config_status_label["text"] = "Algum dos valores não pode ser interpretado como número"
            return

        self.config_status_label["text"] = config.updateConfig

        self.consumo_comb_entry.delete(0, tk.END)
        self.tempo_manutencao_entry.delete(0, tk.END)
        self.salario_entry.delete(0, tk.END)
        self.hospedagem_entry.delete(0, tk.END)
        self.custo_gasolina_entry.delete(0, tk.END)

        config.selectConfig()
        self.consumo_comb_current["text"] = config.consumo_combustivel
        self.tempo_manutencao_current["text"] = config.tempo_manutencao
        self.salario_current["text"] = config.salario_hora
        self.hospedagem_current["text"] = config.hospedagem
        self.custo_gasolina_current["text"] = config.custo_gasolina
