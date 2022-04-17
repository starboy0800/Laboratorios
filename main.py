#JUAN SEBASTIAN MUÑOZ ROJAS (2177436)

#funcion
def precio(mes, meses):
    valor=mes*meses
    return valor

#valores de entrada}
for i in range(0, 3, 1):
    print("Quedan", 3-i,"personas por ingresar")
    nombre=str(input("Escribe el nombre: "))
    edad=float(input("Escribe la edad de "+ nombre +": "))
    meses=int(input("Escribe la cantidad de meses que  "+ nombre +" desea contratar: "))
    #estructuras de decision
    if edad>=0 and edad<12:
        categoria='Infantil'
        mes=43000
    else:
        if edad>=12 and edad<=18:
            categoria='Juvenil'
            mes=36000
        else:
            if edad>18 and edad<120:
                categoria='Mayores'
                mes=32000
    #valores de salida
    if edad<0 or edad>120:
        print("Ingresó un valor no valido, intentelo de nuevo")
    else:
        print("Nombre: ",nombre)
        print("Categoría: ", categoria)
        print("Valor a pagar: $", precio(mes, meses))
#FIN    
