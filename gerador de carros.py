import random
import datetime
from comsql import Database



lista_de_carros = ['Palio','Corsa','Celta','Honda','Focus']
def gdc():
    generator = []
    info = []
    for i in range(3):
        c = random.choice('qwertyuioplkjhgfdsazxcvbnm')
        generator.append(c)
        
    for i in range(4):
        b = random.randint(0,9)
        generator.append(b)
        print(generator)

    a = str(generator[0])
    for i in range(len(generator)):
        a = a + str(generator[i])

    generator = []
    for i in lista_de_carros:
        b  = random.choice(lista_de_carros)
        
    c = datetime.datetime.now()
    a = a[1:]
    info =[a,b,c]
        
    
    return info

print(gdc())
db = Database('Patio.db')
sinal = True
while sinal == True:
    inp = input('tecle enter para dar a entrada em um carro aleatorio: ')
    a = gdc()
    db.insert(a[0],a[1],a[2])
    

        
