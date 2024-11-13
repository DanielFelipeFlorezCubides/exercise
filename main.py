# Escribe un programa que solicite al usuario un número entero positivo n 
# y calcule el factorial de dicho número (n! = 1 * 2 * 3 * ... * n). Usa un ciclo for para realizar el cálculo.

result = 1
while True:
    try:
        n = int(input('Please type a possitive number: '))
        if n < 0:
            raise ValueError()
        if n == 0:
            raise ValueError()
        
        for i in range(1, n+1):
            result *= i
        print(f'The factorial of {n} is: {result}')
        break
    except ValueError as e:
        print('Dear user, you can only type possitive numbers. Please correct it')