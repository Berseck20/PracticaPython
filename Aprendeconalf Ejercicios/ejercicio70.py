"""
Escribir una función que reciba un número entero positivo y devuelva su factorial.
"""

def factorial():
    numero = int(input("Ingrese un numero: "))
    original = numero
    suma = 1
    while numero > 1:
        suma *= numero
        numero -= 1
    
    print(f"El factorial del numero {original} es {suma}")



if __name__ == "__main__":
    factorial()