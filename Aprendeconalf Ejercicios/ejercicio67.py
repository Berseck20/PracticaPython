"""
Escribir un programa que gestione las facturas pendientes de cobro de una empresa.
Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura.
El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar.
Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario.
Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario.
Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
"""

def main():
    facturas = {'001':'10','002':'50','003':'30','004':'20','005':'90'}
    accion = input("Que Desea Hacer? [1: AÑADIR NUEVA FACTURA - 2: PAGAR UNA EXISTENTE - 3: TERMINAR PROGRAMA]: ")
    while accion != '3':
        if accion == '1':
            key = input("Ingrese el numero de factura: ")
            value = input("Ingrese el importe de la factura: ")
            facturas[key] = value
            accion = input("Que Desea Hacer? [1: AÑADIR NUEVA FACTURA - 2: PAGAR UNA EXISTENTE - 3: TERMINAR PROGRAMA]: ")

        elif accion == '2':
            nroFactura = input("Ingrese el numero de factura que desea pagar: ")
            facturas.pop(nroFactura)
            accion = input("Que Desea Hacer? [1: AÑADIR NUEVA FACTURA - 2: PAGAR UNA EXISTENTE - 3: TERMINAR PROGRAMA]: ")

    print("================ PROGRAMA TERMINADO ================")



if __name__ == "__main__":
    main()