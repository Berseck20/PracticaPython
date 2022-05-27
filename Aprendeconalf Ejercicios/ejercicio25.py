"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""

def run():
    contraseña = "elemento"
    usuario = input("Ingrese una contraseña: ")
    if usuario.lower() == contraseña.lower():
        print("La Contraseña Es Correcta!!")
    else:
        print("La Contraseña Es Incorrecta :(")

if __name__ == "__main__":
    run()