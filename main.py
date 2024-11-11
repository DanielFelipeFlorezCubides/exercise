# Escribe un programa que determine si un número es positivo, negativo o cero usando if.
# Solicita al usuario que ingrese un número y determina si es positivo, negativo o cero.

number = int(input('Please type a number: '))

if number < 0:
    print('This is a negative number')
elif number == 0:
    print('You typed 0 number')
else:
    print('This is a postive number')