"""
Escribir un programa que pregunte el nombre del usuario en la consola
y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras,
donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
"""

def run():
    nombre = input("Escribe tu nombre: ")
    count = 0
    for n in nombre:
        count += 1

    print(f"El Nombre Es {nombre.upper()} y Tiene {count} Letras")
    pass

if __name__ == "__main__":
    run()