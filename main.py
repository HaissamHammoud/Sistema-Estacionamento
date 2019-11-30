import datetime
import numpy as np
import sqlite3 as sql
from comsql import Database

db = Database('Patio.db')

#def Entrada(placa, horario):
    #horario = datetime.datetime.now()
    #entr = {placa : [horario]}
    #conn.execute("INSERT INTO carrosnopatio(Placa_do_carro,Horario_de_entrada) VALUES (?,?)",(placa,horario))
    #print("O carro de placa {}, deu entrada no horario {} ".format(placa,horario.hour))
    #return entr


#def Saida(placa, horario):
#    permanencia=
#    print(permanencia)
#
#    return(preco)



enter = True
while enter == True:
    a = input("""
    Deseja dar entrada(a)
    Saida(b)
    Verificar os carros no patio (v)
    Sair do programa(s): """)
    if a == "a":

        placa = input("digite o numero da placa: ")
        modelo = input("digite o modelo do carro: ")
        horario = datetime.datetime.now()
        db.insert(placa,modelo,horario)


    elif a == "b":

        placa = input("Digite a placa do carro que esta saindo: ")
        horario = datetime.datetime.now()
        valor_por_hora = input("Digite o valor por hora: ")
        db.saida(placa,horario,valor_por_hora)


    elif a == 'v':
        db.todos_os_carros()
    else:
        db.finalizar
        enter = False
