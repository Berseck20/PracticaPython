"""
Escribir una función que reciba una muestra de números en una lista y devuelva su media.
"""
import random

def mean(listNum):
    suma = 0
    for num in listNum:
        suma += num

    media = suma / len(listNum)
    print(f"La lista ingresada es {listNum}")
    print(f"La suma de todos sus numeros es {sum(listNum)}")
    print(f"Su media es {media}")

def main():
    listNum = []
    for x in range(1,11):
        listNum.append(random.randrange(10,100))

    mean(listNum)

if __name__ == "__main__":
    main()