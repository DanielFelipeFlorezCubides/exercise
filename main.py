# Escribe un programa que solicite al usuario dos números enteros, un valor de inicio y un valor de fin. 
# El programa debe imprimir todos

while True:
    try:
        bNumber = int(input('Please type the beggining number: '))
        eNumber = int(input('Please type the end number: '))
        if bNumber < 0 and eNumber <= 0:
            raise ValueError
        
        for bNumber in range(eNumber+1):
            print(f'The numbers between are: {bNumber}')
        break
    except ValueError as e:
        print('Dear user, you have to use a possitive number in each cases. Please correct it')