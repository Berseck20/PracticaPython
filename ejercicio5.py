"""
5 - Escribir una función sum() y una función multip() que sumen y
multipliquen respectivamente todos los números de una lista.
Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""

def sum():
    listaSuma = []
    cantNumeros = int(input("Cuantos Numeros Quieres Sumar? "))
    for num in range(cantNumeros):
        numeroIntroducido = input("Introduce Un Numero: ")
        listaSuma.append(numeroIntroducido)
        num +=1
    sumaTotal = 0
    for numero in listaSuma:
        sumaTotal = sumaTotal + int(numero)
    print(f"La Suma Total De Los Numeros Introducido Es {sumaTotal}")
    


def multip():
    listaMultip = []
    cantNumeros = int(input("Cuantos Numeros Quieres Multiplicar? "))
    for numMultip in range(cantNumeros):
        numeroIntroducido = input("Introduce Un Numero: ")
        listaMultip.append(numeroIntroducido)
        numMultip +=1
    multipTotal = 1
    for numero in listaMultip:
        multipTotal = multipTotal * int(numero)
    print(f"La Multiplicacion Total De Los Numeros Introducido Es {multipTotal}")

if __name__ == "__main__":
    print("Bienvenido A Este Programa, Elije Una Opcion")
    print("Que Quieres Hacer?")
    print("1) Sumar / 2) Multiplicar")
    choice = input("Elije Una Opcion: ")
    if choice == "1":
        sum()
    elif choice == "2":
        multip()
    else:
        print("Elije una de las opciones listadas")