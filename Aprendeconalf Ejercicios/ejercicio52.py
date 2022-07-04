"""
Escribir un programa que almacene el abecedario en una lista,
elimine de la lista las letras que ocupen posiciones múltiplos de 3,
y muestre por pantalla la lista resultante.
"""

def run():
    abcdario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    new_abc = []
    for letra in range(len(abcdario)):
        if letra % 3 == 0:
            new_abc.append(abcdario[letra])


    print(new_abc)



if __name__ == "__main__":
    run()