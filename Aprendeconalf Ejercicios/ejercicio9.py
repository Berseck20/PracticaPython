"""
Escribir un programa que pregunte al usuario una cantidad a invertir,
el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
"""

def run():
    cantInvertir = int(input("Ingrese la cantidad que va a invertir: "))
    interesAnual = int(input("Que interes anual tiene: "))
    cantAños = int(input("Que cantidad de años va a invertir: "))

    total = cantInvertir * ((1 + interesAnual)** cantAños)
    print(f"El Total Es ${total}")


if __name__ == "__main__":
    run()