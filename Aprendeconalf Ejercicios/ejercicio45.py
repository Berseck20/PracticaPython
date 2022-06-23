"""
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
"""

def run():
    while True:
        frase1 = input("Introduzca una frase: ")
        if frase1 == "salir":
            print(frase1)
            break
        elif frase1 != "salir":
            print(frase1)
            continue
    
    print("FIN DEL PROGRAMA")


if __name__ == "__main__":
    run()