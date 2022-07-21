"""
Escribir un programa que cree un diccionario de traducción español-inglés.
El usuario introducirá las palabras en español e inglés separadas por dos puntos,
y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones.
Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra.
Si una palabra no está en el diccionario debe dejarla sin traducir.
"""

def main():
    dictionaty = {'El':'He','Come':'Eat','Cebolla':'Onion'}
    frase = input("Escriba una frase que quiera traducir: ")
    traducida = ''
    for word in frase:
        for key, value in dictionaty:
            if word == key:
                traducida = traducida + value
            else:
                continue

    print(f"Tu Frase Es '{frase}' y su traduccion es '{traducida}'")


if __name__ == "__main__":
    main()