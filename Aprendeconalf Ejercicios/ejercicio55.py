"""
Escribir un programa que almacene en una lista los siguientes precios,
50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
"""

def run():
    precios = [50, 75, 46, 22, 80, 65, 8]
    precios.sort()
    print(f"El Precio Minimo Es De ${precios[0]} y El Maximo Es De ${precios[len(precios)-1]}")


if __name__ == "__main__":
    run()