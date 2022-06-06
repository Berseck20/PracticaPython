"""
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y
quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar.
El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.
Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
"""

def run():
    edadCliente = int(input("Ingrese su edad: "))
    if edadCliente <= 4:
        print(f"Su edad es de {edadCliente} años y puede entrar gratis")
    elif edadCliente >= 5 and edadCliente <= 18:
        print(f"Su edad es de {edadCliente} años y debe pagar 5€")
    elif edadCliente >= 19:
        print(f"Su edad es de {edadCliente} años y debe pagar 10€")


if __name__ == "__main__":
    run()