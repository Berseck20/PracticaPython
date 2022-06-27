"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>,
donde <asignatura> es cada una de las asignaturas de la lista.
"""



def run():
    asignaturas = ["Matemáticas","Física","Química","Historia","Lengua"]
    for n in asignaturas:
        print(f"Yo Estudio {n}")


if __name__ == "__main__":
    run()