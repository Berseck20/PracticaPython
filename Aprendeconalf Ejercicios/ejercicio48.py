"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura,
y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota>
donde <asignatura> es cada una des las asignaturas de la lista y
<nota> cada una de las correspondientes notas introducidas por el usuario.
"""

def run():
    asignaturas = ["Matemáticas","Física","Química","Historia","Lengua"]
    notas = []
    for num in range(0, len(asignaturas)):
        numero = input(f"Que Nota Tienes En {asignaturas[num]}: ")
        notas.append(numero)
    print("===============================================================")
    for n in range(0,len(asignaturas)):
        print(f"En {asignaturas[n]} Tienes Una Nota De {notas[n]}")


if __name__ == "__main__":
    run()