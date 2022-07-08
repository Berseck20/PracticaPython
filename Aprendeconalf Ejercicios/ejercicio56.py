"""
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
"""

def run():
    vect1 = [1,2,3]
    vect2 = [-1,0,2]
    print(f"El Producto Escalar Es Igual A {sum([i*j for (i, j) in zip(vect1, vect2)])}")
    print(zip(vect1, vect2))

if __name__ == "__main__":
    run()