"""
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y
muestre por pantalla el número de euros y el número de céntimos del precio introducido.
"""

def run():
    producto = input("Ingrese el precio del producto con sus centimos: €")
    divisionDePrecio = producto.split(",")
    print(f"El valor del producto es €{divisionDePrecio[0]} y sus centimos son ¢{divisionDePrecio[1]}")

if __name__ == "__main__":
    run()