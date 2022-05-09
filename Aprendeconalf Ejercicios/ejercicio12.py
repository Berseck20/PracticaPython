"""
Una panadería vende barras de pan a 3.49€ cada una.
El pan que no es el día tiene un descuento del 60%.
Escribir un programa que comience leyendo el número de barras vendidas que no son del día.
Después el programa debe mostrar el precio habitual de una barra de pan,
el descuento que se le hace por no ser fresca y el coste final total.
"""

def run():
    barraPanFresca = 3.49
    barraPanDiaAnterior = (barraPanFresca * 6/100)*10
    barrasPanVendidas = int(input("Cuantas barras de pan del dia anterior vendio? "))
    print(f"El coste de la barra de pan del dia es de {barraPanFresca}")
    print(f"El coste de la barra de pan del dia anterior es de {barraPanDiaAnterior}")
    print(f"El total a pagar es {round((barrasPanVendidas * barraPanDiaAnterior),2)}")
    pass

if __name__ == "__main__":
    run()