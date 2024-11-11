# Escribe un programa que calcule el IMC y determine el estado de peso.
# Solicita al usuario su peso (en kg) y su altura (en metros). 
# Calcula el IMC y clasifícalo en bajo peso (<18.5), peso normal (18.5-24.9), sobrepeso (25-29.9), u obesidad (>=30).

weight = float(input('Please type your weight(kg): '))
height = float(input('Please type your height(m): '))

if weight > 0 and height > 0:
    imc = (weight / (height ** 2))
    print(f'Your imc is: {round(imc)}')

if imc < 18.5:
    print('You have a low weight')
elif imc <= 24.9:
    print('Your weight is normal')
elif imc <= 29.9:
    print('Your weight exceed the recommended one')
else:
    print('You have obesity weight level')