"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo,
de altura el número introducido.
"""

def run():
    altura = int(input("Ingrese un numero: "))
    for num in range(1,altura+1):
        print("*" * num)


if __name__ == "__main__":
    run()