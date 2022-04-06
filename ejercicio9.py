"""
9 - Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n.
Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""

def generarNCaracteres(multiplicador, caracterAMultiplicar):
    cadenaFinal = ""
    cadenaFinal = cadenaFinal + (caracterAMultiplicar * multiplicador)
    print(cadenaFinal)
    pass

if __name__ == "__main__":
    generarNCaracteres(10, "Hola ")