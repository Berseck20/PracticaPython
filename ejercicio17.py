"""
Definir una tupla con 10 edades de personas.
Imprimir la cantidad de personas con edades superiores a 20.
Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.
"""

def run():
    contEdades = 0
    edades = (14,22,35,84,12,3,5,65,2,7)
    for edad in edades:
        if edad > 20:
            contEdades += 1
    
    print(f"La Cantidad De Personas Mayores a 20 Es: {contEdades}")
    pass

if __name__ == "__main__":
    run()