"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""

def run():
    numeros = []
    for n in range(1,6):
        numeros.append(int(input("Escribe Los Numeros Ganadores De la Loteria: ")))

    numeros.sort()
    for n in numeros:
        print(n) 



if __name__ == "__main__":
    run()