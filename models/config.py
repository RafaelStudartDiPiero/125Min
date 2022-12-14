from db.banco import Banco


class Config(object):

    def __init__(self, consumo_combustivel=0, tempo_manutencao=0, salario_hora=0, hospedagem=0, custo_gasolina=0, numero_motoristas=2):
        self.consumo_combustivel = consumo_combustivel
        self.tempo_manutencao = tempo_manutencao
        self.salario_hora = salario_hora
        self.hospedagem = hospedagem
        self.custo_gasolina = custo_gasolina
        self.numero_motoristas = numero_motoristas

    @property
    def updateConfig(self):
        banco = Banco()
        try:
            if (self.consumo_combustivel < 0 or self.tempo_manutencao < 0 or self.salario_hora < 0 or self.hospedagem < 0 or self.custo_gasolina < 0 or self.numero_motoristas < 1):
                raise Exception("Ocorreu um erro na alteração da configuração")
            c = banco.conexao.cursor()

            c.execute('''update config set consumo_combustivel = {},tempo_manutencao = {}, salario_hora = {}, hospedagem = {}, custo_gasolina = {}, numero_motoristas = {} where id_config = 0 '''.format(
                str(self.consumo_combustivel), str(self.tempo_manutencao), str(self.salario_hora), str(self.hospedagem), str(self.custo_gasolina), str(self.numero_motoristas)))

            banco.conexao.commit()
            c.close()

            return "Configuração atualizada com sucesso."

        except:
            return "Ocorreu um erro na alteração da configuração"

    def selectConfig(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute("select * from config where id_config = 0")

            for row in c:
                self.consumo_combustivel = row[1]
                self.tempo_manutencao = row[2]
                self.salario_hora = row[3]
                self.hospedagem = row[4]
                self.custo_gasolina = row[5]
                self.numero_motoristas = row[6]

            c.close()

            return "Configuração encontrada com sucesso."

        except:
            return "Ocorreu um erro na busca da configuração"
