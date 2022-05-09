"""
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros.
Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario.
Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años.
Redondear cada cantidad a dos decimales.
"""

def run():
    interesAnual = 4
    cantInvertida = int(input("Que cantidad de dinero quiere invertir: "))
    primerAño = (cantInvertida * interesAnual/100) * 1
    segundoAño = (cantInvertida * interesAnual/100) * 2
    tercerAño = (cantInvertida * interesAnual/100) * 3
    print(f"Recibira ${primerAño} el primero año, ${segundoAño} el segundo año y ${tercerAño} el tercer año")
    pass

if __name__ == "__main__":
    run()