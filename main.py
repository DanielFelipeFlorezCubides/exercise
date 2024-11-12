# Escribe un programa que calcule el costo de estacionamiento basado en el número de horas, con tarifas progresivas.
# El costo de estacionamiento se calcula de la siguiente manera:

# Primera hora: $5
# Segunda a cuarta hora: $4 por hora
# Más de cuatro horas: $3 por cada hora adicional
# Solicita al usuario el número de horas de estacionamiento y calcula el costo total.

hours = int(input("Type the parking hours: "))
total = 0
additionalHours = hours - 4 
if hours == 1:
    total += 5
elif 2 <= hours <= 4:
    total += 5 + ((hours - 1) * 4)
elif hours > 4:
    total += 17 + (additionalHours * 3)
        
print(f"The total ammount to pay will be: ${total}")