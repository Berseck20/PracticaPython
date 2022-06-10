"""
Escribir un programa que pida al usuario un número entero positivo y
muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""

def run():
    numero = int(input("Ingrese un numero: "))
    numerosImpares = []
    counter = 1
    while counter <= numero:
        if counter % 2 == 1:
            numerosImpares.append(counter)
        counter += 1

    print(numerosImpares)


if __name__ == "__main__":
    run()