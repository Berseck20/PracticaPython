"""
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y
un resto <r> donde <n> y <m> son los números introducidos por el usuario,
y <c> y <r> son el cociente y el resto de la división entera respectivamente.
"""

def run():
    num1 = int(input("Introduzca un numero: "))
    num2 = int(input("Introduzca otro numero: "))
    c = num1 / num2
    r = num1 % num2
    print(f"La division entre {num1} y {num2} da un cociente de {c} y un resto de {r}")

if __name__ == "__main__":
    run()