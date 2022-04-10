"""
Escribir un programa que le diga al usuario que ingrese una cadena.
El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
"""

import string

def evaluarCadena():
    cadena = input("Ingrese Una Cadena De Caracteres: ")
    letrasMayus = string.ascii_uppercase
    cantMayus = 0
    for caracterCadena in cadena:
        for mayus in letrasMayus:
            if mayus == caracterCadena:
                cantMayus += 1
    
    print(f"La Cadena Que Ingreso Tiene {cantMayus} Letras Mayusculas")

if __name__ == "__main__":
    evaluarCadena()