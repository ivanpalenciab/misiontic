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

         


lista = [
 (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
 (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
 (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
 (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
 (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')
 ]
registro = AutoPartes(lista)


consulta =consultaRegistro(registro,2010)

#print(len(registro['Id']))