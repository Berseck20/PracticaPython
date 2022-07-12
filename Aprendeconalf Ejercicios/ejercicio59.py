"""
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y
muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""


def main():
    divisas = {'Euro':'€', 'Dolar':'$', 'Yen':'¥'}
    user = input("ingrese la divisa que desea consultar: ")
    for key, value in divisas.items():
        if key.lower() == user:
            print(f"La divisa que usted consulto {key}: {value}")
            break
        else:
            print("La divisa no se encuentra disponible")
            break
    pass


if __name__ == "__main__":
    main()