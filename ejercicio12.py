"""
Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.
"""


def masLarga():
    ListaPalabras = []
    cantPalabras = int(input("Que Cantidad De Palabras Quiere Ingresar: "))
    for num in range(cantPalabras):
        ListaPalabras.append(input("Ingrese La Palabras: "))
    
    palabraMasLarga = ""
    IndiceMasLarga = 0
    for word in ListaPalabras:
        if len(palabraMasLarga) < len(word):
            palabraMasLarga = word
            IndiceMasLarga = ListaPalabras.index(word)

    print(f"La Palabra Mas Larga De Las Que Ingresaste Es {palabraMasLarga} y Se Encuentra En El Indice {IndiceMasLarga}")

if __name__ == "__main__":
    masLarga()