from functools import reduce


def ordenes(rutinaContable):
    #Con la informacion dada voy a obtener un diccionario con el numero de orden como llave y los productos vendido
    llaves = [i[0] for i in rutinaContable if True ]
    contenido = (map(lambda x: [i for i in x if type(i)==tuple],rutinaContable))
    diccionario = dict(zip(llaves,contenido)) 

    print('----------------- Inicio Registro diario --------------------------')
    print(diccionario)
    print('----------------- Fin Registro diario -----------------------------')


registro = [
[1201,("25464",4,25842.99),("7854",18,23254.99),("8521",9,48951.95)],
[1202,("8756",3,115362.58),("1112",18,2354.99)],
[1203,('2547',1,125698.20),("2635",2,13564.20),("1254",1,13645.20),("9965",5,1645.20)],
[1204,("9635",7,11.99),("7733",11,18.99),("88112",5,390.95)] 
]

lista = ["hola mundo", 5 , 5.0]

list9 = lambda x: [i for i in x if type(i) != str]
#mult = reduce(lambda a,b:a*b,list9)

#print(mult)
art = [1201,("25464",4,25842.99),("7854",18,23254.99),("8521",9,48951.95)]

list_1 =lambda x: [i for i in x if type(i)==tuple]
llaves = [i[0] for i in registro if True ]
content = (map(lambda x: [i for i in x if type(i)==tuple],registro))
dictionary = dict(zip(llaves,content))
xd =dict(zip(dictionary.keys() ,map(lambda x: [i for i in x if type(i) != str] ,dictionary)))
#print(dictionary)

print(xd)