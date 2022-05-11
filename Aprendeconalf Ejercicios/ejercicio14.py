"""
Escribir un programa que pregunte el nombre completo del usuario en la consola
y después muestre por pantalla el nombre completo del usuario tres veces,
una con todas las letras minúsculas,
otra con todas las letras mayúsculas y
otra solo con la primera letra del nombre y de los apellidos en mayúscula.
El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""

def run():
    nombreCompleto = input("Ingrese Su Nombre Completo: ")
    print(nombreCompleto.lower())
    print(nombreCompleto.upper())
    print(nombreCompleto.title())
    pass

if __name__ == "__main__":
    run()