def AutoPartes(ventas:list):
    diccionario = {}
    for i in ventas:
        id_producto = i[0]
        description_producto=i[1]
        numero_parte_producto= i[2]
        cantidad_vendida_producto = i[3]
        stock_producto = i[4]
        nombre_comprador = i[5]
        cedula_comprador = i[6]
        fecha_venta = i[7]


        IDs =[] ; descripciones=[]

        diccionario['Id']=id_producto ; diccionario['descripcion_producto']=description_producto;diccionario['numero_parte_producto']=numero_parte_producto
        diccionario['cant_prod_vend']= cantidad_vendida_producto; diccionario['stock_´roducto']=stock_producto
        diccionario['nombre_comprador']=nombre_comprador ; diccionario['Cedeula_comprador']=cedula_comprador
        diccionario['Fecha_venta']=fecha_venta
    
    #print(diccionario)


def consultaRegistro(ventas,idProducto):
    registro = ventas['producto consultado']
    for i in registro:
        id_producto = i[0]
         


lista = [(10,'cohete militar',1,2,200,'Vladimir putin',100,'12/06/2020'),(100,'ametralladora ligera',2,5,1000,'Timochenkp',22448475,'15/02/2001'),(1,'Bomba nuclear',5,1,4,'Donald Trump',25487,'15/09/2018')]
AutoPartes(lista)

lista_2 = [i[0] for i in lista if True]
print(lista_2)