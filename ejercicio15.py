"""
Construir un pequeño programa que convierta números binarios en enteros.
"""

def binToInt():
    numBinarioDerecho = input("Ingrese Un Numero Binario: ")
    totalInt = 0
    exponencial = len(numBinarioDerecho) -1
    for valor in numBinarioDerecho:
        totalInt += ((int(valor) * 2) ** exponencial)
        exponencial -= 1

    print(f"Su Numero En Binario Es {numBinarioDerecho}, Convertido A Decimal Es {totalInt}")

    

if __name__ == "__main__":
    binToInt()
