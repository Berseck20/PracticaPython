"""
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""

def run():
    for num in range(1,12):
        print(f"{num-1} x 10 = {(num-1)*10}")


if __name__ == "__main__":
    run()