"""
Solicitar un número e imprimir los dígitos pares de este.
"""

def run():
    numero = int(input("Ingresa Un Numero: "))
    pares = []
    for num in range(0, numero):
        if num % 2 == 0:
            pares.append(num)

    print(f"El numero ingresado es {numero}")
    print("Sus pares anteriores son:")
    print(pares)

if __name__ == "__main__":
    run()