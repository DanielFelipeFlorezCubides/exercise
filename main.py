# Escribe un programa que determine si un año es bisiesto o no.
# Solicita al usuario que ingrese un año y determina si es bisiesto 
# (divisible entre 4, pero no entre 100, salvo que sea divisible entre 400).

year = float(input('Please type the year number: '))
leap = False

if year % 400 == 0:
    leap = True
elif year % 100 == 0:
    leap = False
elif year % 4 == 0:
    leap = True

if leap:
    print('This is a leap year')
else:
    print('This is not a leap year')