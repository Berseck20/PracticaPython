"""
Este programa muestra primero el listado de categorías de películas y pide al usuario que introduzca el código de la categoría de la película
y posterior a ello pide que el usuario introduzca el número de días de atraso, y así se muestra al final el total a pagar.
"""

def atraso():
    categoria = int(input("ESCRIBE EL CODIGO DE LA CATEGORIA DE LA PELICULA: "))
    diasAtraso = float(input("ESCRIBE LOS DIAS DE ATRASO: "))
    if categoria == 1:
        print(f"EL TOTAL A PAGAR ES ${(categoria + (diasAtraso * 0.5))}")
    elif categoria == 2:
        print(f"EL TOTAL A PAGAR ES ${(categoria + (diasAtraso * 0.75))}")
    elif categoria == 3:
        print(f"EL TOTAL A PAGAR ES ${(categoria + (diasAtraso * 1))}")
    elif categoria == 4:
        print(f"EL TOTAL A PAGAR ES ${(categoria + (diasAtraso * 1.5))}")
    else:
        print("INGRESE UNA CATEGORIA CORRECTA")



if __name__ == "__main__":
    print("""
                CATEGORIAS          PRECIOS         CODIGO          RECARGO/DIA DE ATRASO

                FAVORITOS           $2.50              1                    $0.50
                NUEVOS              $3.00              2                    $0.75
                ESTRENOS            $3.50              3                    $1.00
                SUPER ESTRENOS      $4.00              4                    $1.50 
    
    """)
    atraso()