"""
Escribir una función que calcule el total de una factura tras aplicarle el IVA.
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar,
y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
"""

def iva(totalFactura, cantIVA=21):
    totalMasIVA = totalFactura * (cantIVA / 100)
    totalFinal = totalFactura + totalMasIVA
    print("=============================================")
    print(f"La factura es de ${totalFactura}")
    print(f"El IVA es de %{cantIVA}")
    print(f"El total a pagar sera de ${totalFinal}")


def main():
    totalFactura = int(input("Total de la factura a pagar: "))
    cantIVA = int(input("Cantidad de IVA: "))
    iva(totalFactura, cantIVA)


if __name__ == "__main__":
    main()