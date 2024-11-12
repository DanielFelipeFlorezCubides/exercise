# Escribe un programa que calcule el tiempo que tarda en llegar un automóvil a su destino.
# Solicita al usuario la distancia a recorrer (en km) y la velocidad promedio del automóvil (en km/h). 
# Calcula el tiempo de viaje en horas y minutos. Si la velocidad es mayor a 120 km/h, muestra un mensaje de advertencia.

distance = float(input("Type the distance(km): "))
speed = float(input("Type the speed(km/h): "))

if distance > 0 and speed > 0:
    if speed > 120:
        print("You are going too fast")
    
    time = distance / speed 
    if time < 1:
        time = time * 60
        print("The travel time will be:",round(time), "minutes")
    else:
        integer = int(time)
        minutes = (time - integer)*60
        print("The travel time will be: ", integer, "hours and", round(minutes), "minutes")