"""
10 - Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla.
Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
****
*********
*******
"""

def procedimiento(numero1, numero2, numero3):
    listaNume = [numero1, numero2, numero3]
    caracter = "/"
    for index in listaNume:
        histograma = ""
        histograma = histograma + (index * caracter)
        print(histograma)


if __name__ == "__main__":
    procedimiento(2, 5, 8)