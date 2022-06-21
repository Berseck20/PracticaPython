"""
Escribir un programa que pida al usuario una palabra y
luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
"""

def run():
    palabra = input("Introduzca Una Palabra: ")
    for n in palabra[::-1]:
        print(n)
    print("FIN")


if  __name__ == "__main__":
    run()