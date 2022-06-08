"""
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""

def run():
    nomb = input("Ingrese su nombre: ")
    for n in range(1,11):
        print(f"Tu Nombre Es {nomb}")

if __name__ == "__main__":
    run()