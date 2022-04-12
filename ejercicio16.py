"""
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla.
"""


def run():
    añoEnCurso = input("Ingrese El Año En Curso: ")
    for i in range(3):
        nombre = input("Ingrese Su Nombre: ")
        nacimiento = input("Ingrese Su Fecha De Nacimiento: ")
        print("=====================================")
        print(nombre + " En El Año " + añoEnCurso + " Cumplira " + str(int(añoEnCurso) - int(nacimiento)))
        print("=====================================")



if __name__ == "__main__":
    run()