from db.banco import Banco


class Config(object):

    def __init__(self, alimentacao=0, salario_hora=0, hospedagem=0, custo_gasolina=0):
        self.alimentacao = alimentacao
        self.salario_hora = salario_hora
        self.hospedagem = hospedagem
        self.custo_gasolina = custo_gasolina

    @property
    def updateConfig(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute('''update config set alimentacao = {}, salario_hora = {}, hospedagem = {}, custo_gasolina = {} where id_config = 0 '''.format(
                str(self.alimentacao), str(self.salario_hora), str(self.hospedagem), str(self.custo_gasolina)))

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
                self.alimentacao = row[1]
                self.salario_hora = row[2]
                self.hospedagem = row[3]
                self.custo_gasolina = row[4]

            c.close()

            return "Configuração encontrada com sucesso."

        except:
            return "Ocorreu um erro na busca da configuração"
