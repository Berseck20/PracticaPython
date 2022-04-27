"""
Una
PyME, tiene la siguiente estructura de pagos para sus 10 empleados: 

Un sueldo
base

Una bonificación del 1% del sueldo base, por
cada mes trabajado

Una asignación familiar del 5% del sueldo base,
por cada hijo


La suma de los tres valores anteriores, conforman
la “base imponible”.
Todos los empleados están en FONASA, así que
deben cotizar el 7% de la base imponible en salud. Los empleados están en una de dos: AFPs, la
primera cobra (entre imposición y otros gastos) el 12 % de la base imponible, mientras que la
segunda cobra el 11.4%

Construyan un programa Python que:

a) Pida el ingreso de datos de los 10 empleados
y los almacene. Debe pedir: nombre, apellido, sueldo base, afap, fecha de ingreso
y cantidad de hijos.

b) El programa debe calcular la base imponible,
según lo indicado arriba y luego descontar según corresponda.

c) El programa debe calcular lo que se debe
pagar a FONASA y el monto de cada AFAP.

d) El programa debe calcular los promedios de
pago a los empleados

e) El programa debe implementar control de
excepciones en cada ingreso de información.

El mensaje debe ser claro al usuario, indicando
que debe corregir en cada intento de ingresar los datos.E
Se entiende por:

FONASA: El Fondo Nacional de Salud, FONASA, es el organismo público encargado de otorgar cobertura de atención,
tanto a las personas que cotizan el 7% de sus ingresos mensuales en FONASA, como a aquellas que, por carecer de recursos propios,
financia el Estado a través de un aporte fiscal directo.

AFAP: AFAP significa “Administradora de Fondos de Ahorro Previsional”.
Son empresas que administran parte del aporte de los trabajadores afiliados para que en el futuro tengan una mejor jubilación. 
"""



class trabajadores(object):
    def __init__(self, nombre, apellido, sueldoBase, afap, diaIngreso, cantHijos):
        self.nombre = nombre
        self.apellido = apellido
        self.sueldoBase = sueldoBase
        self.afap = afap
        self.diaIngreso = diaIngreso
        self.cantHijos = cantHijos


def run():
    trabajador1 = trabajadores("Juan", "Carlos", 35000, 5, "2005", 2)
    
    baseImponible = trabajador1.sueldoBase + ((1 * trabajador1.sueldoBase / 100) * (((2022 - int(trabajador1.diaIngreso)) * 12))) + ((5 * trabajador1.sueldoBase / 100) * trabajador1.cantHijos)
    descuentoFONASA = baseImponible - (7 * (baseImponible / 100))
    pass

if __name__ == "__main__":
    run()








    