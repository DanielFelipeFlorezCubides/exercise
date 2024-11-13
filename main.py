# Escribe un programa que solicite al usuario un número entero positivo n y calcule la suma de los primeros n números enteros. 
# Utiliza un ciclo for para realizar la suma.

sum = 0
while True:
    try:
        n = int(input('Please type a possitive number: '))
        if n < 0:
            raise ValueError()
        if n == 0:
            raise ValueError()
        
        for i in range(n):
            sum = sum + (i+1)
        print(f'The sum of the first numbers before {n} is: {sum}')
        break
    except ValueError as e:
        print('Dear user, you can only type possitive numbers. Please correct it')