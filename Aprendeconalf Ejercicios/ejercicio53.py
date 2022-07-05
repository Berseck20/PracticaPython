"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
"""

def run():
    palabra = input("Ingrese Una Palabra: ")
    if palabra == palabra[::-1]:
        print(f"Tu palabra {palabra} es un palindromo")
    else:
        print("Tu palabra NO es un palindromo")



if __name__ == "__main__":
    run()