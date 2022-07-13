"""
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
"""

def main():
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    direccion = input("Ingrese su direccion: ")
    telefono = input("Ingrese su numero de telefono: ")
    datosPersonales = dict(Nombre = nombre, Edad = edad, Direccion = direccion, Telefono = telefono)
    print(f"{datosPersonales.get('Nombre')} tiene {datosPersonales.get('Edad')} años, vive en {datosPersonales.get('Direccion')} y su numero de telefono es {datosPersonales.get('Telefono')}")


if __name__ == "__main__":
    main()