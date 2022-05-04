"""
Identificar si la suma de los dígitos de un numero es par o impar.
"""

def run():
    numero1 = int(input("Ingrese un numero: "))
    numero2 = int(input("Ingrese otro numero: "))
    sumaTotal = numero1 + numero2
    if sumaTotal % 2 == 0:
        print(f"La suma de los numeros ingresado es {sumaTotal}, El resultado es un numero par")
    else:
        print(f"La suma de los numeros ingresado es {sumaTotal}, El resultado es un numero impar")

if __name__ == "__main__":
    run()