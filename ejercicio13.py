"""
Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n,
y devuelva las palabras que tengan mas de n caracteres.
"""

def filtrar_palabras():
    listaPalabras = ["Jacinto", "Estroncio", "Energumeno", "Hello", "Cuaderno"]
    cantCaracteres = int(input("Que Cantidad De Caracteres Quiere Buscar: "))
    palabrasMasLargas = []
    for word in listaPalabras:
        if cantCaracteres < len(word):
            palabrasMasLargas.append(word)

    print("===================================================")
    print(f"Las Palabras De La Lista Son: {listaPalabras}")
    print(f"Las Palabras Que Contienen Mas De {cantCaracteres} Son {palabrasMasLargas}")
    print("===================================================")

if __name__ == "__main__":
    filtrar_palabras()