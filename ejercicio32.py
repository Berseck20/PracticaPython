"""
Para un número N imprimir su tabla de multiplicar.
"""

def run():
    numeroMultiplicar = int(input("Ingrese El Numero Del Que Quiere Saber Su Tabla De Multiplicar: "))
    print("===========================================")
    for num in range(1,11):
        print(f"{numeroMultiplicar} * {num} = {numeroMultiplicar * num}")
    print("===========================================")

if __name__ == "__main__":
    run()