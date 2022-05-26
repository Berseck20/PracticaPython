"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""

def run():
    edad = int(input("Ingrese Su Edad: "))
    if edad > 18:
        print("Usted Es Mayor De Edad!")
    else:
        print("Usted Es Menor De Edad!")

if __name__ == "__main__":
    run()