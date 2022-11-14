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
                     cep text,
        )""")

        c.execute("""create table if not exists config(
                     id_config integer primary key autoincrement,
                     alimentacao real,
                     salario_hora real,
                     hospedagem real,
                     custo_gasolina real,
        )""")

        c.execute("""insert into config(alimentacao, salario_hora, hospedagem, custo_gasolina)
                     select 0, 0, 0, 0
                     where not exists (select * from config)
        """)

        self.conexao.commit()
        c.close()
