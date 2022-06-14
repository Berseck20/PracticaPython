"""
Escribir un programa que pregunte al usuario una cantidad a invertir,
el interés anual y el número de años,
y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""

def run():
    cantidadInvertir = float(input("Ingrese La Cantidad Que Quiere Invertir: "))
    interesAnual = float(input("Cuanto Es El Interes Anual: "))
    cantidadAños = float(input("En Que Cantidad De Años: "))
    for años in range(1, int(cantidadAños + 1)):
        cantidadInvertir *= 1 + interesAnual / 100 
        print(f"En {años} Años Tendra: ${round(cantidadInvertir, 2)}")
    


if __name__ == "__main__":
    run()