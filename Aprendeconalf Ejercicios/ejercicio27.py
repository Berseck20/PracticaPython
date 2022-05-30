"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
"""

def run():
    num = input("Ingrese un numero: ")
    if int(num) % 2 == 0:
        print(f"El Numero {num} Es Par")
    else:
        print(f"El Numero {num} Es Impar")

if __name__ == "__main__":
    run()