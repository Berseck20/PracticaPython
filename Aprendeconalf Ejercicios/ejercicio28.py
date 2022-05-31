"""
Para tributar un determinado impuesto se debe ser mayor de 16 años y
tener unos ingresos iguales o superiores a 1000 € mensuales.
Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y
muestre por pantalla si el usuario tiene que tributar o no.
"""

def run():
    edad = int(input("Ingrese Su Edad: "))
    sueldo = int(input("Ingrese Su Sueldo Mensual: "))
    if edad > 16 and sueldo > 1000:
        print("Usted Deberia Tributar")
    else:
        print("No Es Necesario Que Usted Tribute")

if __name__ == "__main__":
    run()