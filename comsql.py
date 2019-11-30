import sqlite3
import datetime



class Database:


    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS carros(placa, modelo,horario)")
        self.conn.commit()

    def insert(self,placa,modelo,horario):
        self.cur.execute("INSERT INTO carros VALUES(?,?,?)",(placa,modelo,horario))
        self.conn.commit()
        print('carro de placa {} foi adicionado ao patio'.format(placa))

    def saida(self,placa,horario,valor_por_hora):
        self.cur.execute("SELECT horario FROM carros WHERE placa = (?)",(placa,))
        self.rows = self.cur.fetchall()
        print(self.rows)
        try:
            self.horario_de_entrada = self.rows[0][0]
            self.entrada= datetime.datetime.strptime(self.horario_de_entrada,
            '%Y-%m-%d %H:%M:%S.%f')
            self.deltas = horario - self.entrada
            self.tempo_estacionado = float(self.deltas.total_seconds())/60/60
            self.custo = float(valor_por_hora) * self.tempo_estacionado
            print("Carro de placa: {}".format(placa))
            print("entrada no patio: {}".format(self.horario_de_entrada))
            print("saida do patio:{}".format(horario))
            print("O tempo de permanencia foi de : {}".format(self.tempo_estacionado))
            print("O valor a ser pago pe de {}".format(self.custo))

            self.confirma = input('para confirmar, digite (s)')
            self.cur.execute('DELETE FROM carros WHERE placa = ?' , (placa,))
            self.conn.commit()
        except:
            print("Carro não encontrado.")


    def todos_os_carros(self):
            self.cur.execute("SELECT * FROM carros")
            self.rows = self.cur.fetchall()
            print(self.rows)







    def finalizar():
        self.conn.close()
