"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""

def run():
    asignaturas = ["Matemáticas","Física","Química","Historia","Lengua"]
    for mat in asignaturas:
        nota = int(input(f"Que Nota Tienes En {mat}:"))
        if nota <= 6:
            asignaturas.remove(mat)
        else:
            continue
    
    print(f"Las Materias Que Aprobaste Son: {asignaturas}")



if __name__ == "__main__":
    run()