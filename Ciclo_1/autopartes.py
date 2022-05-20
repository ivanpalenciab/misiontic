def AutoPartes(ventas:list):
    for i in ventas:
        for j in range(0,4):
            nombre_producto = i[0]
            abreviacion=i[1]
            tipo= i[2]
            descripcion = i[3]
        print (f'el producto vendido fue {nombre_producto} con la abreviacion {abreviacion} del tipo {tipo} y la descripcion {descripcion}')

def consultaRegistro(ventas,idProducto):
    pass


lista = [('cohete militar','coh_mil','cohete','Cohete capas de destruir el mundo'),('ametralladora ligera','soft-amet','Ametralladora','Ametralladora para matar gente'),('Bomba nuclear','Bomb-nuc','bomba','Arma para matar mucha pero mucha gente')]
AutoPartes(lista)