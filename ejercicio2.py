"""

Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

"""


def maxDeTres(numero1, numero2, numero3):
    if numero1 > numero2 and numero1 > numero3:
        print(numero1)
    elif numero2 > numero1 and numero2 > numero3:
        print(numero2)
    elif numero3 > numero1 and numero3 > numero2:
        print(numero3)



if __name__ == "__main__":
    numero1 = int(input("Ingrese El Primer Numero: "))
    numero2 = int(input("Ingrese El Segundo Numero: "))
    numero3 = int(input("Ingrese El Tercer Numero: "))
    maxDeTres(numero1, numero2, numero3)