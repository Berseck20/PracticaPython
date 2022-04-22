"""
Este programa pide primeramente la cantidad total de compras de una persona.
Si la cantidad es inferior a $100.00, el programa dirá que el cliente no aplica a la promoción.
Pero si la persona ingresa una cantidad en compras igual o superior a $100.00,
el programa genera de forma aleatoria un número entero del cero al cinco.
Cada número corresponderá a un color diferente de cinco colores de bolas que hay para determinar el descuento que el cliente recibirá como premio.
Si la bola aleatoria es color blanco, no hay descuento, pero si es uno de los otros cuatro colores,
sí se aplicará un descuento determinado según la tabla que  aparecerá,
y ese descuento se aplicará sobre el total de compra que introdujo inicialmente el usuario,
de manera que el programa mostrará un nuevo valor a pagar luego de haber aplicado el descuento.
"""
import random

def run():
    totalCompras = int(input("Ingrese El Total De Sus Compras: "))
    numeroBola = random.randrange(1,6)
    reiniciarPrograma = 0
    if totalCompras == 100 or reiniciarPrograma != 1:
        print(f"Su Gasto Es Igual O Mayor A ${totalCompras}, Usted Aplica A La Promocion")
        print("""
                        COLOR                   DESCUENTO


                        BOLA BLANCA             NO HAY DESCUENTO
                        BOLA ROJA               %10 DE DESCUENTO
                        BOLA AZUL               %15 DE DESCUENTO
                        BOLA VERDE              %25 DE DESCUENTO
                        BOLA AMARILLA           %50 DE DESCUENTO


        """)
        if numeroBola == 1:
                print("USTED OBTUVO UNA BOLA BLANCA")
                print("LAMENTABLEMENTE NO TIENE DESCUENTO")
                print(f"SU TOTAL A PAGAR SERA DE ${totalCompras}")
        elif numeroBola == 2:
                print("USTED OBTUVO UNA BOLA ROJA")
                print("OBTIENE UN %10 DE DESCUENTO")
                print(f"SU TOTAL A PAGAR SERA DE ${totalCompras - ((totalCompras * 10)/100)}")
        elif numeroBola == 3:
                print("USTED OBTUVO UNA BOLA AZUL")
                print("OBTIENE UN %15 DE DESCUENTO")
                print(f"SU TOTAL A PAGAR SERA DE ${totalCompras - ((totalCompras * 15)/100)}")
        elif numeroBola == 4:
                print("USTED OBTUVO UNA BOLA VERDE")
                print("OBTIENE UN %25 DE DESCUENTO")
                print(f"SU TOTAL A PAGAR SERA DE ${totalCompras - ((totalCompras * 25)/100)}")
        elif numeroBola == 5:
                print("USTED OBTUVO UNA BOLA AMARILLA")
                print("OBTIENE UN %50 DE DESCUENTO")
                print(f"SU TOTAL A PAGAR SERA DE ${totalCompras - ((totalCompras * 50)/100)}")
        else:
            print(f"Su Gasto Es Menos De $100, No Aplica Para El Descuento")
        
        reiniciarPrograma = int(input("SI DESEA SALIR PRESIONE 1 SINO INGRESE 2 PARA VOLVER A EMPEZAR: "))
        


if __name__ == "__main__":
    run()