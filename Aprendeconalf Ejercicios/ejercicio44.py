"""
Escribir un programa en el que se pregunte al usuario por una frase y una letra,
y muestre por pantalla el número de veces que aparece la letra en la frase.
"""

def run():
    frase = input("Ingrese una frase: ")
    letra = input("Ingrese una letra: ")
    count = 0
    for n in frase:
        if n == letra:
            count += 1
    
    print(f"En la Frase {frase} Contiene {count} Letras {letra}")



if __name__ == "__main__":
    run()