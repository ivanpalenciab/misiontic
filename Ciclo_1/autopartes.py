def AutoPartes(ventas:list):
    diccionario = {}
    IDs_producto=[i[0] for i in ventas if True]
    descripciones_prod=[i[1] for i in ventas if True]
    partes_prod=[i[2] for i in ventas if True]
    cant_vend=[i[3] for i in ventas if True]
    stock_prod=[i[4] for i in ventas if True]
    nombre_compradores=[i[5] for i in ventas if True]
    IDs_compradores=[i[6] for i in ventas if True]
    fechas_venta=[i[7] for i in ventas if True]


        

    diccionario['Id']=IDs_producto ; diccionario['descripcion_producto']=descripciones_prod;diccionario['numero_parte_producto']=partes_prod
    diccionario['cant_prod_vend']= cant_vend; diccionario['stock_producto']=stock_prod
    diccionario['nombre_comprador']=nombre_compradores ; diccionario['Cedeula_comprador']=IDs_compradores
    diccionario['Fecha_venta']=fechas_venta
    
    return diccionario


def consultaRegistro(ventas,idProducto):
    cont = 0
    j=0
    for i in ventas['Id']:
        j+=1
        if i == idProducto:
            cont = 0
            id = i
            dproduct=ventas['descripcion_producto'][cont]
            npartes = ventas['numero_parte_producto'][cont]
            cant_ven = ventas['cant_prod_vend'][cont]
            stock=ventas['stock_producto'][cont]
            nombre_comprador = ventas['nombre_comprador'][cont]
            cedula_comprador = ventas['Cedeula_comprador'][cont]
            fecha=ventas['Fecha_venta'][cont]
            cont +1
            

            print( f'Producto consultado : {id} Descripción {dproduct} #Parte {npartes} Cantidad vendida {cant_ven} Stock {stock} Comprador {nombre_comprador} Documento {cedula_comprador} Fecha Venta {fecha}')
            break

        else:
            if cont == 0 and j== len(ventas['Id']):
                print('No hay registro de venta de ese producto')
            else:
               break

         


lista = [(10,'cohete militar',1,2,200,'Vladimir putin',100,'12/06/2020'),(100,'ametralladora ligera',2,5,1000,'Timochenkp',22448475,'15/02/2001'),(1,'Bomba nuclear',5,1,4,'Donald Trump',25487,'15/09/2018')]
registro = AutoPartes(lista)

consulta =consultaRegistro(registro,1)
consultaRegistro(registro,2)
#print(len(registro['Id']))