import tkinter as tk


class Instrucoes(tk.Frame):
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
        container2["padx"] = 5
        container2.pack(fill="both", expand=True)

        message_container0 = tk.Frame(container2, bg=controller.pagesbg)
        message_container0["padx"] = 5
        message_container0.pack(fill="x")

        container3 = tk.Frame(self, bg=controller.pagesbg)
        container3["pady"] = 5
        container3["padx"] = 5
        container3.pack(side="bottom", fill="x")

        label = tk.Label(container1, text="Instruções de Uso",
                         font=controller.titlefont, bg=controller.pagesbg)
        label.pack(side="left", padx=20)

        message = tk.Text(message_container0, font=controller.descriptionfont,
                          bg=controller.pagesbg, border=None)
        message.pack(side="left", padx=20)

        bou = tk.Button(container3, text="Página Inicial", font=controller.buttonfont,
                        command=lambda: controller.up_frame("WelcomePage"), bg=controller.buttonbg, height=2)
        bou.pack(side="right")

        message.insert(tk.END, """•Inicialmente, deve-se informar os dados referentes a configuração em “Atualizar dados”.
Após preencher os campos ou deixá-los vazios, pode-se clicar em "Alterar", mostrando os valores de configuração armazenados.

•Em seguida, vá em “Planejar rota” e selecione as agências que quer visitar.
Se necessário, registre uma nova agência em “Registrar nova agência”.

•Feito isso, o nosso banco de dados terá todas as informações necessárias para otimizar a rota.

•Por fim, basta ir em “Planejar rota”, atualizar as opções com as alterações realizadas e escolher 
as agências que quer visitar, clicando em "Planejar Rota".

•Pronto, o 125Min mostrará o melhor caminho a ser feito, fazendo você economizar tempo e 
dinheiro!
""")
