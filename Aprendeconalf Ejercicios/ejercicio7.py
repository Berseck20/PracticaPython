"""
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal
y lo almacene en una variable, y muestre por pantalla la frase
Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
(altura ** 2)/peso
"""

def run():
    peso = int(input("Introduzca su peso(KG): "))
    altura = int(input("Introduzca su altura(CM): "))
    imc = round(peso/(altura ** 2),6)
    print(f"Tu indice de masa corporal es {imc}")

if __name__ == "__main__":
    run()