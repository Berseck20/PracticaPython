"""
En una determinada empresa, sus empleados son evaluados al final de cada año.
Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando,
traduciéndose en mejores beneficios.
Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más,
pero no valores intermedios entre las cifras mencionadas.
A continuación se muestra una tabla con los niveles correspondientes a cada puntuación.
La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
"""

def run():
    puntuacion = float(input("Cual Fue Su Puntuacion Este Año: "))
    if puntuacion == 0.0:
        print("Su puntacion fue Inaceptable")
        print(f"Usted obtuvo una puntuacion de 0.0, no recibira un bono este año")
    elif puntuacion == 0.4:
        print("Su puntacion fue aceptable")
        print(f"Usted obtuvo una puntuacion de 0.4, usted recibira €{2400 + (2400 * puntuacion)}")
    elif puntuacion == 0.6:
        print("Su puntacion fue Meritoria")
        print(f"Usted obtuvo una puntuacion de 0.6, usted recibira €{2400 + (2400 * puntuacion)}")


if __name__ == "__main__":
    run()