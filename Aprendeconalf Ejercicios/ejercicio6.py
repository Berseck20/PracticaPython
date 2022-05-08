"""
Escribir un programa que lea un entero positivo, "N"
introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta "N".
La suma de los  primeros enteros positivos puede ser calculada de la siguiente forma:

suma = (n*(n+1))/ 2
"""

def run():
    n = int(input("Escribe Un Numero: "))
    suma = 0
    for num in range(1,n+1):
        suma = suma + num

    print(f"El numero introducido es {n}, La suma de todos sus enteros anteriores es {suma}")

if __name__ == "__main__":
    run()