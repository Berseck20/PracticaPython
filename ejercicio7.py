"""
7 - Definir una función es_palindromo() que reconoce palíndromos
(es decir, palabras que tienen el mismo aspecto escritas invertidas),
ejemplo: es_palindromo ("radar") tendría que devolver True.
"""

def es_palindromo():
    cadenaOriginal = input("Escribe Una Palabra: ")
    cadenaInvertida = ""
    for letra in cadenaOriginal[::-1]:
        cadenaInvertida = cadenaInvertida + letra

    if cadenaOriginal == cadenaInvertida:
        print("True")
    else:
        print("False")


if __name__ == "__main__":
    es_palindromo()