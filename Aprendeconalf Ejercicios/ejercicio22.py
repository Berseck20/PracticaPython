"""
Escribir un programa que pregunte por consola por los productos de una cesta de la compra,
separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
"""

def run():
    listaDeCompra = []
    for n in range(1,3):
        individual = input("Ingrese el producto que va a comprar: ")
        listaDeCompra.append(individual)
    
    print("Tu Lista De Compra Es La Siguiente: ")
    for prod in listaDeCompra:
        print(prod)
    pass

if __name__ == "__main__":
    run()