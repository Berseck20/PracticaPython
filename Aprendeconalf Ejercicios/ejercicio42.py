"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
"""

def run():
    numeroEntero = int(input("Ingrese un numero: "))
    for i in range(2, numeroEntero):
        if numeroEntero % i == 0:
            break
    if (i + 1)  == numeroEntero:
        print(f"{numeroEntero} Es un numero primo")
    else: 
        print(f"{numeroEntero} NO es un numero primo")


if __name__ == "__main__":
    run()