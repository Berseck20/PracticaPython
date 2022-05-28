"""
Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
Si el divisor es cero el programa debe mostrar un error.
"""

def run():
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    if num2 == 0:
        print("****FATAL ERROR****")
    else:
        print(f"La division de los dos numeros es {num1/num2}")

if __name__ == "__main__":
    run()