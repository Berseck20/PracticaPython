"""
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y
muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
"""

def main():
    meses = {'01': 'Enero','02': 'Febrero','03': 'Marzo','04':'Abril','05':'Mayo','06':'Junio','07':'Julio','08':'Agosto','09':'Septiembre','10':'Octubre','11':'Noviembre','12':'Diciembre'}
    dia = input("Ingrese El Dia: ")
    mes = input("Ingrese El Mes: ")
    año = input("Ingrese El Año: ")

    var = 0
    mes = "0" + mes


    for mon in meses:
        if mon == mes:
            var = meses[mon]
            break
        else:
            continue
    
    print(f"{dia} de {var} del año {año}")

    pass


if __name__ == "__main__":
    main()