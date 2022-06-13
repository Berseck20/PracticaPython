"""
Escribir un programa que pida al usuario un número entero positivo y
muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""

import time

def run():
    numero = int(input("Ingrese un numero: "))
    while numero >= 0:
        print(numero)
        time.sleep(0.5)
        numero -= 1

    print("Fin De La Cuenta Atras!")

if __name__ == "__main__":
    run()