"""
Escribir un programa que pregunte por una muestra de números, separados por comas
los guarde en una lista y muestre por pantalla su media y desviación típica.
"""
import math


def mostrarPantalla(self):
    for num in self:
        if num == len(self):
            print(num)
        else:
            print(f"{num},", end=" ")

def mean(listaNumeros):
    media = sum(listaNumeros)/len(listaNumeros)

    return media

def desviacionTipica(listaNumeros):
    media = sum(listaNumeros)/len(listaNumeros)
    var = sum((l-media)**2 for l in listaNumeros) / len(listaNumeros)
    standarDeviation = math.sqrt(var)
    print(standarDeviation)

def main():
    cantNumeros = int(input("Que cantidad de numeros va a ingresar: "))
    listaNumeros = []
    for _ in range(1,cantNumeros+1):
        int(input("Ingrese el numero: "))
        listaNumeros.append(_)

    print("Los Numeros Que Ingresaste Son: ")
    mostrarPantalla(listaNumeros)
    print("La media de los numero ingresado es: ")
    print(mean(listaNumeros))
    print("La desviacion tipica de los numeros ingresados es: ")
    desviacionTipica(listaNumeros)

if __name__ == "__main__":
    main()