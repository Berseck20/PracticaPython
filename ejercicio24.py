"""
Has un programa que pida al usuario una cantidad de dolares, una tasa de interés y un numero de años.
Muestra por pantalla en cuanto se habrá convertido el capital inicial transcurridos esos años si cada año se aplica la tasa de interés introducida.
Recordar que un capital C dolares a un interés del x por cien durante n años se convierte en C * (1 + x/100)elevado a n (años).
Probar el programa sabiendo que una cantidad de 10000 dolares al 4.5% de interés anual se convierte en 24117.14 dolares al cabo de 20 años.
"""

def interes():
    dolares = int(input("Ingrese La Cantidad De Dolares Que Tiene: "))
    tasaInteres = float(input("Cual Sera La Tasa De Interes Anual: "))
    numAños = int(input("En Cuantos Años: "))
    totalAcumulado = round((dolares * (1 + tasaInteres/100) ** numAños), 2)
    print(f"""
        Si Usted Invierte Un Capital Inicial De {dolares}
        A Una Tasa De %{tasaInteres}
        Al Cabo De {numAños} Años
        Obtendra {totalAcumulado}                                                                  
    """)

if __name__ == "__main__":
    interes()