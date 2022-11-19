import sqlite3


class Banco():

    def __init__(self):
        self.conexao = sqlite3.connect('125MIN.db')
        self.createTables()

    def createTables(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists agencias(
                     id_agencia integer primary key autoincrement,
                     rua text,
                     numero text,
                     cidade text,
                     cep text)""")

        c.execute("""create table if not exists config(
                     id_config integer primary key autoincrement,
                     consumo_combustivel real,
                     tempo_manutencao real,
                     salario_hora real,
                     hospedagem real,
                     custo_gasolina real,
                     numero_motoristas integer)""")

        c.execute("""insert into config(id_config ,consumo_combustivel, tempo_manutencao, salario_hora, hospedagem, custo_gasolina, numero_motoristas)
                     select 0, 0, 0, 0, 0, 0, 2
                     where not exists (select * from config)""")

        self.conexao.commit()
        c.close()
