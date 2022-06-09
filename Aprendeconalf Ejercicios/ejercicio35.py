"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""

def run():
    edad = int(input("Ingrese Su Edad: "))
    for año in range(1,edad+1):
        print(f"Cumpliste {año} Año De Edad")

if __name__ == "__main__":
    run()