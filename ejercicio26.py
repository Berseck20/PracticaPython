"""
De la galería de productos, el usuario introducirá el código y el número de unidades del producto que desea comprar.
El programa determinará el total a pagar, como una factura.
Una variante a este ejercicio que lo haría un poco más complejo sería
dar la posibilidad de seguir ingresando diferentes códigos de productos con sus respectivas cantidades,
y cuando el usuario desee terminar el cálculo de la factura completa con todas sus compras. Te animas??
"""

def tienda():
    productoElegido = int(input("Codigo Del Producto Que Desea Comprar: "))
    cantidadProducto = int(input("Que Cantidad De Productos: "))
    precios = [20,5,30,35,5,12,8,17,3,25]
    #precios ={"camisa":20, "cinturon":5, "zapatos":30, "pantalon":35, "calcetines":5, "faldas":12, "gorras":8, "sueter":17, "corbata":3, "chaqueta":25}
    indx = 0
    for precio in precios:
        if productoElegido == indx:
            total = precio * cantidadProducto
            print(f"""
            USTED ELIGIO EL PRODUCTO N°{productoElegido}
            SU VALOR ES DE ${precio}
            Y QUIERE COMPRAR {cantidadProducto} PRODUCTO(S)
            EL TOTAL A PAGAR ES DE ${total}
            """)
            break
        elif productoElegido != indx:
            indx += 1
            
    if productoElegido != indx:    
        print("Ese Codigo De Producto No Se Encuentra Disponible")

if __name__ == "__main__":
    print("""

                    BIENVENIDO A FAKE TIENDA

                    ESTE ES NUESTRO CATALOGO:

                    PRODUCTO                                CODIGO

                    CAMISA................................... 1
                    CINTURON................................. 2
                    ZAPATOS.................................. 3
                    PANTALON................................. 4
                    CALCETINES............................... 5
                    FALDAS................................... 6
                    GORRAS................................... 7
                    SUETER................................... 8
                    CORBATA.................................. 9
                    CHAQUETA................................. 10
    
    
    """)
    tienda()