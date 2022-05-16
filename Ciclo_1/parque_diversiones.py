def cliente(informacion:dict) -> dict:
    id_cliente = informacion['id_cliente']
    nombre = informacion['nombre']
    edad = informacion['edad']
    primer_ingreso = informacion['primer_ingreso']

    if edad > 18:
        atraccion = 'X-Treme'
        valor_boleta = 20000
        apto = True
        if primer_ingreso == True:
            valor_boleta = valor_boleta*0.95

    elif edad >=15 and edad <=18:
        atraccion = 'Carroschocones'
        valor_boleta=5000 
        apto = True
        if primer_ingreso ==True:
            valor_boleta=valor_boleta*0.93
    
    elif edad >=7 and edad < 15:
        atraccion = 'Sillas voladoras'
        valor_boleta = 10000
        apto = True
        if primer_ingreso== True:
            valor_boleta = valor_boleta*0.95

    else:
        atraccion='N/A'
        apto = False
        valor_boleta='N/A'


    diccionario={'nombre': nombre, 'edad': edad, 'atraccion': atraccion, 'apto':apto,'primer_ingreso': primer_ingreso, 'total_boleta': valor_boleta}
    print (diccionario)



#tests
diccionario={'id_cliente':1,'nombre':'Johana Fernandez','edad':20,'primer_ingreso':True}
diccionario_1 = {'id_cliente':1,'nombre':'Johana Fernandez','edad':20,'primer_ingreso':False}
diccionario_2 = {'id_cliente':2,'nombre':'Gloria Suarez','edad':3,'primer_ingreso':True}
diccionario_3 = {'id_cliente':3,'nombre':'Tatiana Suarez','edad':17,'primer_ingreso':True}
diccionario_4 = {'id_cliente':4,'nombre':'Tatiana Ruiz','edad':8,'primer_ingreso':True}
diccionario_5 = {'id_cliente':4,'nombre':'Tatiana Ruiz','edad':8,'primer_ingreso':False}

cliente(diccionario)
cliente(diccionario_1)
cliente(diccionario_2)
cliente(diccionario_3)
cliente(diccionario_4)
cliente(diccionario_5)
