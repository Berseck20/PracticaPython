"""
Para un numero N menor de 100. Mostrar la suma de los cuadrados de los números que están separados entre si cuatro posiciones.
"""

def run():
    numIngresado = int(input("Ingresa Un Numero Menor a 100: "))
    if numIngresado > 100:
        print("Ingresa Un Numero Menor A 100")
    else:
        sumaTotal = 0
        numeros = [num for num in range(1,numIngresado,4)]
        for num in numeros:
            cuadrado = num ** 2
            print(cuadrado)
            sumaTotal = sumaTotal + cuadrado
        print(f"La Suma De Los Cuadrador De Los Numeros Anteriores A {numIngresado} Es De {sumaTotal}")
    pass

if __name__ == "__main__":
    run()