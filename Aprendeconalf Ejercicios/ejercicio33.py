"""
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""

def run():
    pizza = input("Que tipo de pizza quiere, vegetariana o no vegetariana: ")
    if pizza == "vegetariana":
        ingredientesVegetarianos = input("Ingrese que ingredientes quiere ponerle (Pimiento y Tofu): ")
        print(f"Tu pizza es {pizza} y sus ingredientes son Mozzarella, Tomate, {ingredientesVegetarianos}")
    else:
        noVegetarianos = input("Ingrese que ingredientes quiere ponerle (Peperoni, Jamon y Salmon): ")
        print(f"Tu pizza es {pizza} y sus ingredientes son Mozzarella, Tomate, {noVegetarianos}")


if __name__ == "__main__":
    run()