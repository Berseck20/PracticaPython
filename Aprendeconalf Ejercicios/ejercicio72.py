"""
Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
"""

def areaCirculo(areaInicial):
    pi = 3.14
    areaFinal = pi * (areaInicial ** 2)
    print(f"El area del circulo es de {areaFinal}")
    return pi, areaFinal


def volCilindro(pi, areaFinal, alturaCilindro):
    volumenCilindro = pi * areaFinal * areaFinal * alturaCilindro
    print(f"El Volumen de un cilindro de {alturaCilindro} altura es de {volumenCilindro} cm3")



def main():
    areaInicial = int(input("Ingrese el area del circulo: "))
    alturaCilindro = int(input("Ingrese la Altura Del Cilindro: "))
    pi, areaFinal = areaCirculo(areaInicial)
    volCilindro(pi, areaFinal, alturaCilindro)


if __name__ == "__main__":
    main()