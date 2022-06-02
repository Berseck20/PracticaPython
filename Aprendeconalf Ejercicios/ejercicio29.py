"""
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
El grupo A esta formado por las mujeres con un nombre anterior a la M
y los hombres con un nombre posterior a la N y el grupo B por el resto.
Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
"""

def run():
    nombre = input("Escriba Su Nombre: ")
    sexo = input("Hombre o Mujer?: ")
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    for nom in nombre[0]:
        for letra in alfabeto:
            grupoA = 0
            grupoB = 0
            if (alfabeto.index(letra) < 12  and sexo == "Mujer") or (alfabeto.index(letra) > 12  and sexo == "Hombre"):
                grupoA = grupoA+1
                #print(f"Su Nombre Es {nombre}, Su Sexo Es {sexo} y Pertenece al Grupo A")
            else:
                grupoB = grupoB +1
                #print(f"Su Nombre Es {nombre}, Su Sexo Es {sexo} y Pertenece al Grupo B")

    if grupoA == 1:
        print(f"Su Nombre Es {nombre}, Su Sexo Es {sexo} y Pertenece al Grupo A")
    elif grupoB == 1:
        print(f"Su Nombre Es {nombre}, Su Sexo Es {sexo} y Pertenece al Grupo B")

if __name__ == "__main__":
    run()