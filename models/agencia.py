from db.banco import Banco


class Agencia(object):

    def __init__(self, id_agencia=0, rua="", numero="", cidade="", cep=""):
        self.id_agencia = id_agencia
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.cep = cep

    def inserirAgencia(self):
        banco = Banco()

        try:
            if not self.numero.isdigit():
                raise Exception("Ocorreu um erro na inserção de uma agência")

            if len(self.cep) != 9:
                raise Exception("Ocorreu um erro na inserção de uma agência")

            if (not self.cep[0:5].isdigit()) or self.cep[5] != "-" or (not self.cep[6:9].isdigit()):
                raise Exception("Ocorreu um erro na inserção de uma agência")

            c = banco.conexao.cursor()

            c.execute('''insert into agencias(rua,numero,cidade,cep) values("{}","{}","{}","{}")'''.format(
                self.rua, self.numero, self.cidade, self.cep))

            banco.conexao.commit()
            c.close()

            return "Agência cadastrada com sucesso."

        except:
            return "Ocorreu um erro na inserção de uma agência"

    @property
    def updateAgencia(self):
        banco = Banco()
        try:
            if not self.numero.isdigit():
                raise Exception("Ocorreu um erro na alteração de uma agência")

            if len(self.cep) != 9:
                raise Exception("Ocorreu um erro na alteração de uma agência")

            if (not self.cep[0:5].isdigit()) or self.cep[5] != "-" or (not self.cep[6:9].isdigit()):
                raise Exception("Ocorreu um erro na alteração de uma agência")

            agencia_aux = Agencia()
            if agencia_aux.selectAgencia(self.cep) == "Ocorreu um erro na busca de uma agência":
                raise Exception("Ocorreu um erro na alteração de uma agência")

            c = banco.conexao.cursor()

            c.execute('''update agencias set rua ="{}", numero = "{}", cidade = "{}" where cep="{}"'''.format(
                self.rua, self.numero, self.cidade, str(self.cep)))

            banco.conexao.commit()
            c.close()

            return "Agência atualizada com sucesso."

        except:
            return "Ocorreu um erro na alteração de uma agência"

    @property
    def deleteAgencia(self):
        banco = Banco()
        try:
            if self.selectAgencia(self.cep) == "Ocorreu um erro na busca de uma agência":
                raise Exception("Ocorreu um erro na exclusão de uma agência")

            c = banco.conexao.cursor()

            c.execute('''delete from agencias where cep ="{}" '''.format(
                str(self.cep)))

            banco.conexao.commit()
            c.close()

            return "Agência excluída com sucesso."

        except:
            return "Ocorreu um erro na exclusão de uma agência"

    def selectAgencia(self, cep):
        banco = Banco()
        self.id_agencia = -1
        try:
            c = banco.conexao.cursor()
            c.execute(
                '''select * from agencias where cep ="{}"'''.format(str(cep)))

            for row in c:
                self.id_agencia = row[0]
                self.rua = row[1]
                self.numero = row[2]
                self.cidade = row[3]
                self.cep = row[4]

            # k = c.fetchone()
            if self.id_agencia == -1:
                c.close()
                raise Exception("Ocorreu um erro na busca de uma agência")

            c.close()

            return "Agência encontrada com sucesso."

        except:
            return "Ocorreu um erro na busca de uma agência"
