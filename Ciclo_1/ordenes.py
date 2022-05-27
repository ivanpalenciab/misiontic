from functools import reduce


def ordenes(rutinaContable):
    #voy a guardar mi informacion en dos listas en una va a estar los numeros del registro y en la otra una lista de tuplas
    numeros_orden = [i[0] for i in rutinaContable if True ]
    contenido = list((map(lambda x: [i for i in x if type(i)==tuple],rutinaContable)))
   

    #Voy a crear una funcion que va a generarme el total por cada orden
    def total_orden(informacion):
        resultados=[]
        suma = lambda x,y:x+y
        for i in informacion:
            resultado = i[1]*i[2]
            resultados.append(resultado)
        return reduce(suma,resultados)
    
    #vamos a crear una lista con el total de cada orden
    total_pedido = list(map(total_orden,contenido))

    print('------------------------ Inicio Registro diario ---------------------------------')
    for i in range(0,len(total_pedido)):
        if total_pedido[i] < 600000:
            total_pedido[i] += 25000
            print('La factura',numeros_orden[i],'tiene un total en pesos de {:,.2f}'.format(total_pedido[i],2))
        else:
             print('La factura',numeros_orden[i],'tiene un total en pesos de {:,.2f}'.format(total_pedido[i],2))
    print('-------------------------- Fin Registro diario ----------------------------------')


registro = [
[1201,("25464",4,25842.99),("7854",18,23254.99),("8521",9,48951.95)],
[1202,("8756",3,115362.58),("1112",18,2354.99)],
[1203,('2547',1,125698.20),("2635",2,135645.20),("1254",1,13645.20),("9965",5,1645.20)],
[1204,("9635",7,11.99),("7733",11,18.99),("88112",5,390.95)] 
]

ordenes(registro)