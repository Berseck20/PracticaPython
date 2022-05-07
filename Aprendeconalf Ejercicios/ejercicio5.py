"""
Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
Después debe mostrar por pantalla la paga que le corresponde.
"""

horasTrabajadas = input("Cuantas Horas Trabajaste?: ")
pagoHora = input("Cuanto Te Pagan Por Hora: ")
print(f"Por {horasTrabajadas} Horas Te Tienen Que Pagar ${int(horasTrabajadas) * int(pagoHora)}")