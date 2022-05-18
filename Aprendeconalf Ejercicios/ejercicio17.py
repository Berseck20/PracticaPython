"""
Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
"""
def run():
    frase = input("Ingrese Una Frase O Palabra: ")
    print(f"Su Frase Es {frase} y Asi Se Veria Invertida {frase[::-1]}")
    pass

if __name__ == "__main__":
    run()