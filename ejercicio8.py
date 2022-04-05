"""
Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario.
Escribir la función usando el bucle for anidado.
"""

def superposicion():
    lista1 = [1,2,3,4,4]
    lista2 = [5,6,7,8,9,0]
    for numero1 in lista1:
        for numero2 in lista2:
            if numero1 == numero2:
                print("True")
                break
            else:
                continue
    print("False")


if __name__ == "__main__":
    superposicion()