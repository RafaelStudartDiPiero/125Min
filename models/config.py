from db.banco import Banco


class Config(object):

    def __init__(self, alimentacao = 0, salario_hora = 0, hospedagem = 0, custo_gasolina = 0):
        self.id_config = 0
        self.alimentacao = alimentacao
        self.salario_hora = salario_hora
        self.hospedagem = hospedagem
        self.custo_gasolina = custo_gasolina
    
    @property
    def updateConfig(self):
        banco = Banco()
        try: 
            c = banco.conexao.cursor()

            c.execute("update config set alimentacao = '" + self.alimentacao + "', salario_hora = '" + self.salario_hora +
                      "', hospedagem = '" + self.hospedagem + "', custo_gasolina = '" + self.custo_gasolina + "' where id_config = '" + self.id_config + "' ")

            banco.conexao.commit()
            c.close()

            return "Configuração atualizada com sucesso."

        except:
            return "Ocorreu um erro na alteração da configuração"