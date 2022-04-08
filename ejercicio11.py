"""
La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte), solo van a funcionar para 2 o 3 números.
Supongamos que tenemos mas de 3 números o no sabemos cuantos números son.
Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.
"""

def maxInList():
    cantNumeros = int(input("Que Cantidad De Numeros Quiere Ingresar? "))
    listaNumeros = []
    while cantNumeros > 0:
        numerosEnLista = int(input("Ingrese Los Numeros Que Desee: "))
        listaNumeros.append(numerosEnLista)
        cantNumeros -= 1

    mayorNum = 0
    for num in range(len(listaNumeros)):
        if listaNumeros[num] > mayorNum:
            mayorNum = listaNumeros[num]
        else:
            break
    
    print(f"El Mayor De Los Numero En La Lista Proporcionada Es {mayorNum}")

if __name__ == "__main__":
    maxInList()