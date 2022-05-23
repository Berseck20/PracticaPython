"""
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y
muestra por pantalla, el día, el mes y el año. 
Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
"""

def run():
    fechaNacimiento = input("Ingrese La Fecha De Su Nacimiento (Formato dd/mm/aaaa): ")
    cumpleaños = fechaNacimiento.split("/")
    dia = cumpleaños[0]
    mes = cumpleaños[1]
    año = cumpleaños[2]
    if len(dia) == 1:
        dia = "0" + dia
    elif len(mes) == 1:
        mes = "0" + mes
    print(f"Su Cumpleaños Es El Dia {dia} Del Mes {mes} Del Año {año}")

if __name__ == "__main__":
    run()