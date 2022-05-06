"""
Los números de las claves de dos cajas fuertes están mezcladas en un
número entero llamado clave maestra. Determine ambas claves, la primera
clave se construye con los dígitos impares de la clave maestra y la
segunda con los pares. Ejemplo: Clave Maestra= 12345, clave1=135,
clave2=24.
"""

def run():
    claveMaestra = input("Ingrese La Clave Maestra: ")
    cajaFuerte1 = ""
    cajaFuerte2 = ""
    for num in claveMaestra:
        if int(num) % 2 == 0:
            cajaFuerte1 = cajaFuerte1 + str(num)
        else:
            cajaFuerte2 = cajaFuerte2 + str(num)

    print(f"La Clave Maestras Es {claveMaestra}, La Primera Caja Fuerte Tiene La Clave {cajaFuerte1} y La Segunda {cajaFuerte2}")
    pass

if __name__ == "__main__":
    run()