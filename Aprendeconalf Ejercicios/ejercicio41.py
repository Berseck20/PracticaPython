"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""

def run():
    truePassword = "contraseña"
    password = input("Introduzca una contraseña: ")
    while True:
        if password != truePassword:
            password = input("Contraseña Incorrecta, Por Favor Introduzca De Nuevo!: ")
            continue
        elif password == truePassword:
            print("La Contraseña Es Correcta!")
            break


if __name__ == "__main__":
    run()