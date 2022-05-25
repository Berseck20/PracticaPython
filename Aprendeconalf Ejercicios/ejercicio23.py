"""
Escribir un programa que pregunte el nombre el un producto,
su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto
seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y
el coste total con 8 dígitos enteros y 2 decimales.
"""

def run():
    nombreProducto = input("Ingrese el producto que va a comprar: ")
    precioProducto = input("Ingrese el precio del producto: ")
    numeroUnidades = input("Cuantas unidades va a comprar?: ")
    costeTotal = int(precioProducto) * int(numeroUnidades)
    costeTotalStr = str(costeTotal)
    print(f"El producto que va a comprar es {nombreProducto} y cuesta {precioProducto.zfill(7 - len(precioProducto))},00")
    print(f"Vas a comprar {numeroUnidades} Unidades y el total es {str(costeTotal).zfill(9 - len(costeTotalStr))},00")

if __name__ == "__main__":
    run()