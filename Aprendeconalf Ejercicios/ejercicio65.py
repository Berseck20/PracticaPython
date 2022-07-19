"""
Escribir un programa que cree un diccionario simulando una cesta de la compra.
El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar.
Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato
"""

def main():
    carritoCompras = {}
    seguir = ""
    total = 0
    while True:
        articulo = input("Que articulo desea comprar: ")
        precio = input("Cuanto vale: $")
        carritoCompras[articulo] = precio
        total = total + int(precio)
        seguir = input("Desea agregar algo mas al carrito? ")
        if seguir == "no" or seguir == "No" or seguir == "NO":
            break
        elif seguir == "si" or seguir == "Si" or seguir == "SI":
            continue
    
    print("==== LISTA DE LA COMPRA ====")
    for key, values in carritoCompras.items():
        print(key + "\t" + "    " + values)
    print("Coste Total:" + "\t" + str(total))


if __name__ == "__main__":
    main()