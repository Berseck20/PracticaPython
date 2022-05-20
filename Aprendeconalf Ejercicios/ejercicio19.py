"""
Escribir un programa que pregunte el correo electrónico del usuario en la consola y
muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es
"""

def run():
    correo = input("Escribe tu correo electronico: ")
    nuevocorreo = ""
    for letra in correo:
        if letra == "@":
            break
        else:
            nuevocorreo = nuevocorreo + letra

    nuevocorreo = nuevocorreo + "@ceu.es"
    print(f"Tu nuevo correo es: {nuevocorreo}")

if __name__ == "__main__":
    run()