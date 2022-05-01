def CDT(usuario:str,capital:int,tiempo:int):
    if tiempo > 2:
        interes = (capital*0.03*tiempo)/12
        valor = capital + interes
        return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {str(capital)} para un tiempo de {str(tiempo)} meses es: {str(valor)}"
    else:
        interes = (capital*0.02)
        valor = capital - interes
        return f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {str(capital)} para un tiempo de {str(tiempo)} meses es: {str(valor)}'

print(CDT('AB1012',1000000,3))
print(CDT('ER3366',650000,2))