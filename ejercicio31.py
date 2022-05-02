"""
Imprimir 10 veces la serie de números de 1 a 10.
"""
def run():
    serie = 1
    listaImprimir = [x for x in range(1,11)]

    while serie <= 10:
        print("\n=============================")
        print(f"Serie {serie}: \n")
        for num in listaImprimir:
            print(num)
        
        serie += 1

if __name__ == "__main__":
    run()