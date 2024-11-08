# Escribe un programa que determine el tipo de triángulo en función de sus lados usando if.
# Solicita al usuario que ingrese las longitudes de los tres lados de un triángulo. 
# Determina si el triángulo es equilátero, isósceles o escaleno.

sideLenght_1 = float(input('Please type the lenght of the first side of the triangle: '))
sideLenght_2 = float(input('Please type the lenght of the second side of the triangle: '))
sideLenght_3 = float(input('Please type the lenght of the third side of the triangle: '))

if sideLenght_1 == sideLenght_2 and sideLenght_1 == sideLenght_3:
    print('This is an equilateral triangle!')
elif (sideLenght_1 == sideLenght_2 and sideLenght_1 != sideLenght_3) or (sideLenght_1 != sideLenght_2 and sideLenght_1 == sideLenght_3):
    print('This is an isoceles triangle!')
else:
    print('This is a scalene triangle!')