"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
"""

def run():
    palabra = input("Ingrese una palabra: ")
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for n in palabra:
        if n == "a":
            a += 1
        elif n == "e":
            e += 1
        elif n == "i":
            i += 1
        elif n == "o":
            o += 1
        elif n == "u":
            u += 1
    
    print(f"Tu Palabra: {palabra} Tiene {a} A, {e} E, {i} I, {o} O, {u} U")



if __name__ == "__main__":
    run()