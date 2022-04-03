"""
6 - Definir una función inversa() que calcule la inversión de una cadena.
Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""

def inversa(cadenaParaInversa):
    cadenaInvertida = ""
    # range(len(cadenaParaInversa), 0)
    for letra in cadenaParaInversa[::-1]:
        cadenaInvertida = cadenaInvertida + letra

    print(cadenaInvertida)


if __name__ == "__main__":
    cadenaParaInversa = input("Ingrese una cadena de texto: ")
    inversa(cadenaParaInversa)