"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta,
un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta.
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
"""

def main():
    tablaPrecios = {'platano': 1.35, 'manzana': 0.80, 'pera': 0.85, 'naranja': 0.70}
    tipoFruta = input("Que Fruta Quiere Comprar: ")
    cantFruta = int(input("Cantidad De Kilos Que Quiere: "))
    for key in tablaPrecios:
        try:
            if key == tipoFruta:
                print(f"La Fruta Que Va a Comprar Es {key}")
                print(f"Su Precio Por Kilo Es De ${tablaPrecios[key]}")
                print(f"El Total A Pagar Es: ${tablaPrecios[key] * cantFruta}")
                break
            else:
                continue
        except tipoFruta != key:
            print("La fruta que usted quiere no se encuentra disponible")


if __name__ == "__main__":
    main()