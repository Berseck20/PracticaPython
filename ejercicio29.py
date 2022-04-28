"""
Determinar la cantidad de dígitos de un numero (1- 100000)
"""

def contDigitos():
    numero = input("Ingrese Un Numero: ")
    digitos = 0
    for num in numero:
        digitos += 1 

    print(f"El Numero Ingresado {numero} Tiene En Total {digitos} Digitos")
    pass

if __name__ == "__main__":
    contDigitos()