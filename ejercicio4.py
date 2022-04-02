"""

4 - Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

"""

def esVocal():
    vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    letraIntroducida = input("Por Favor Introduce Una Letra: ")
    for letra in vocales:
        if letra == letraIntroducida:
            print("True")
            break
    if letra != letraIntroducida:
        print("False")
        
    

if __name__ == "__main__":
    esVocal()