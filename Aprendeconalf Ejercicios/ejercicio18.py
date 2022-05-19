"""
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
"""

def run():
    frase = input("Ingrese Una Frase: ")
    vocal = input("Introduzca Una Vocal: ")
    vocalUpper = vocal.upper()
    fraseFinal = ""
    for letra in frase:
        if letra == vocal:
            fraseFinal = fraseFinal + vocalUpper
        else:
            fraseFinal = fraseFinal + letra

    print(fraseFinal)

if __name__ == "__main__":
    run()