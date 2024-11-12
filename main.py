# Escribe un programa que determine el mayor de tres números usando if.
# Solicita al usuario que ingrese tres números y determina cuál es el mayor.

fNumber = int(input('Please type the first number: '))
sNumber = int(input('Please type the second number: '))
tNumber = int(input('Please type the third number: '))

if fNumber > sNumber and fNumber > tNumber:
    print(f'{fNumber} is the higher number')
elif fNumber == sNumber and fNumber > tNumber:
    print(f'{fNumber} is the higher number')
elif fNumber > sNumber and fNumber == tNumber:
    print(f'{fNumber} is the higher number')
elif fNumber < sNumber and sNumber > tNumber:
    print(f'{sNumber} is the higher number')
elif fNumber > sNumber and sNumber == tNumber:
    print(f'{sNumber} is the higher number')
elif fNumber == sNumber and sNumber > tNumber:
    print(f'{sNumber} is the higher number')
elif tNumber > sNumber and fNumber < tNumber:
    print(f'{tNumber} is the higher number')
elif tNumber == sNumber and fNumber > tNumber:
    print(f'{tNumber} is the higher number')
elif tNumber > sNumber and fNumber == tNumber:
    print(f'{tNumber} is the higher number')