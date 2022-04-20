"""
Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden
las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos
últimas tiene que decir que riman un poco y si no, que no riman.
"""

def rimanPalabras():
    primeraPalabra = input("Introduce Una Palabra: ")
    longitudPrimeraPalabra = len(primeraPalabra)
    segundaPalabra = input("Introduce Otra Palabra: ")
    longitudSegundaPalabra = len(segundaPalabra)

    if primeraPalabra[longitudPrimeraPalabra - 3 : longitudPrimeraPalabra] == segundaPalabra[longitudSegundaPalabra - 3 : longitudSegundaPalabra]:
        print(f"Las Palabras {primeraPalabra} y {segundaPalabra} Riman")
    elif primeraPalabra[longitudPrimeraPalabra - 2 : longitudPrimeraPalabra] == segundaPalabra[longitudSegundaPalabra - 2 : longitudSegundaPalabra]:
        print(f"Las Palabras {primeraPalabra} y {segundaPalabra} Riman Un Poco")
    else:
        print("Las Palabras No Riman")

if __name__ == "__main__":
    rimanPalabras()