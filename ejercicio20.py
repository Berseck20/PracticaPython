"""
Escriba una función es_bisiesto() que determine si un año determinado es un año bisiesto.
Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400
"""

def esBisiesto():
    año = int(input("Escriba un año para saber si es bisiesto o no: "))
    if año % 4 == 0:
        bisiesto = True
        print(f'El Año {año} Es Bisiesto.')
    else:
        print(f'El Año {año} No Es Bisisesto.')


if __name__ == '__main__':
    esBisiesto()