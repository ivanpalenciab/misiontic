def AutoPartes(ventas:list):
    diccionario = {}
    for i in ventas:
        if diccionario.get(i[0]) == None:
            diccionario[i[0]] = []
        diccionario.setdefault(i[0], []).append((i[1],i[2],i[3],i[4],i[5],i[6],i[7]))        
    return diccionario    
    
def consultaRegistro(ventas, idProducto):    
    if idProducto in ventas:
        for k in ventas[idProducto]:                       
            print("Producto consultado :", idProducto,  " Descripción ",  k[0],  " #Parte ",  k[1],  " Cantidad vendida ",  k[2],  " Stock ",  k[3],  " Comprador", k[4],  " Documento ",  k[5],  " Fecha Venta ",  k[6])
    else:
        print("No hay registro de venta de ese producto")

         


lista = [(10,'cohete militar',1,2,200,'Vladimir putin',100,'12/06/2020'),(100,'ametralladora ligera',2,5,1000,'Timochenkp',22448475,'15/02/2001'),(1,'Bomba nuclear',5,1,4,'Donald Trump',25487,'15/09/2018')]
registro = AutoPartes(lista)

consulta =consultaRegistro(registro,1)
consultaRegistro(registro,2)
#print(len(registro['Id']))