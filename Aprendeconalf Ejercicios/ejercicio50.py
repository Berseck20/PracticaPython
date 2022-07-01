"""
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
"""

def run():
    numeros = [x for x in range(1,11)][::-1]
    print(numeros)


if __name__ == "__main__":
    run()