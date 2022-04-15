"""
Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene,
cuantas letras "e" tiene y así hasta completar todas las vocales.
Se puede hacer que el usuario sea quien elija la palabra.
"""

def contar_vocales():
    characterA, characterE, characterI, characterO, characterU = 0,0,0,0,0
    word = input("Ingrese Una Palabra: ")
    for character in word:
        if character == "a" or character == "A":
            characterA += 1
        elif character == "e" or character == "E":
            characterE += 1
        elif character == "i" or character == "I":
            characterI += 1
        elif character == "o" or character == "O":
            characterO += 1
        elif character == "u" or character == "U":
            characterU += 1

    print(f"La Palabra {word} Tiene {characterA} Letras A, {characterE} Letras E, {characterI} Letras I, {characterO} Letras O, {characterU} Letras U")

if __name__ == "__main__":
    contar_vocales()