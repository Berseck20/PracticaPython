"""
Escribe un programa que te permita jugar a una versión simplificada del
juego Master Mind. El juego consistirá en adivinar una cadena de números
distintos. Al principio, el programa debe pedir la longitud de la cadena (de 2
a 9 cifras). Después el programa debe ir pidiendo que intentes adivinar la
cadena de números. En cada intento, el programa informará de cuántos números
han sido acertados (el programa considerará que se ha acertado un número si
coincide el valor y la posición).
EJ:
Dime la longitud de la cadena: 4
Intenta adivinar la cadena: 1234
Con 1234 has adivinado 1 valores. Intenta adivinar
la cadena: 1243
Con 1243 has adivinado 0 valores. Intenta adivinar
la cadena: 1432
Con 1432 has adivinado 2 valores. Intenta adivinar
la cadena: 2431
Con 2431 has adivinado 4 valores.
Felicidades
"""

import random

def mastermind():
    lenCadenaNum = int(input("Ingrese de que longitud sera la cadena de numeros: "))
    cadenaAdivinar = ""
    if lenCadenaNum <= 9:
        for num in range(lenCadenaNum):
            cadenaAdivinar = cadenaAdivinar + str(random.randint(2,lenCadenaNum))
    else:
        print("Ingrese una cadena de numeros de minimo 2 y maximo 9 caracteres")
    
    
    gano = True
    while gano == True:
        contadorAciertos = 0
        cadenaIngresada = int(input("Intenta Adivinar La Cadena: "))
        for num in cadenaAdivinar:
            for num2 in str(cadenaIngresada):
                if num2 == num:
                    contadorAciertos += 1

        if contadorAciertos == lenCadenaNum:
            print(f"Acertaste!!, Tuviste {contadorAciertos} Aciertos")
            gano = False
        else:
            print(f"En La Cadena {cadenaIngresada} Acertaste {contadorAciertos} Valores")
            print("")


if __name__ == "__main__":
    mastermind()