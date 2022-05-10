"""
Escribir un programa que pregunte el nombre del usuario en la consola y
un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
"""

def run():
    name = input("Introduce tu nombre: ")
    num = int(input("Introduce un numero: "))
    for n in range(1,num+1):
        print(name)

if __name__ == "__main__":
    run()