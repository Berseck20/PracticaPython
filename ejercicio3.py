"""
3 - Definir una función que calcule la longitud de una lista o una cadena dada.
(Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.

"""

def propiaLen(cadena):
    contadorDeCadena = 0
    for caracteres in cadena:
        contadorDeCadena += 1
    
    print(f"Su Cadena De Caracteres Tiene Una Longitud De {contadorDeCadena} Caracteres")


if __name__ == "__main__":
    cadena = input("Escribe un mensaje: ")
    propiaLen(cadena)