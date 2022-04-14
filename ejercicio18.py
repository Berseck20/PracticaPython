"""
Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)
"""

def startwitha():
    cantPalabrasA = 0
    CONJUNTONOMBRES = ["Alameda","Arberto","Alondro","Trollface"]
    for word in CONJUNTONOMBRES:
        if word[0] == "a" or word[0] == "A":
            cantPalabrasA = cantPalabrasA + 1
            continue
    print("La Cantidad De Palabras Que Comienzan Con A Es: " + str(cantPalabrasA))

if __name__ == '__main__':
    startwitha()