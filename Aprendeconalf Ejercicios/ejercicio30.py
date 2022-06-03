"""
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
"""

def run():
    rentaAnual = int(input("Escriba Su Renta Anual: "))
    if rentaAnual <= 10000:
        print(f"Su Renta Anual Es De ${rentaAnual} y Su Tipo Impositivo Es De Un %5")
    elif rentaAnual>10001 and rentaAnual<=20000:
        print(f"Su Renta Anual Es De ${rentaAnual} y Su Tipo Impositivo Es De Un %15")
    elif rentaAnual>20001 and rentaAnual<=35000:
        print(f"Su Renta Anual Es De ${rentaAnual} y Su Tipo Impositivo Es De Un %20")
    elif rentaAnual>35001 and rentaAnual<=60000:
        print(f"Su Renta Anual Es De ${rentaAnual} y Su Tipo Impositivo Es De Un %30")
    elif rentaAnual>60001: 
        print(f"Su Renta Anual Es De ${rentaAnual} y Su Tipo Impositivo Es De Un %45")


if __name__ == "__main__":
    run()