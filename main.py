# Escribe un programa que genere un número aleatorio entre 1 y 100 y permita al usuario adivinarlo.
# El programa debe dar pistas si el número ingresado es mayor o menor que el número secreto. 
# Usa un ciclo while para permitir al usuario seguir intentando hasta que adivine el número.

import random

sNumber = random.randint(1, 100)
print("I have choosen a number between 1 and 100, try to guess wich one is it!")

while True:
    try:
        guess = int(input("Type your guess: "))

        if guess < sNumber:
            print("The number is higher than your guess. Keep trying!")
        elif guess > sNumber:
            print("The number is less than your guess. Keep trying!")
        else:
            print("Congrats! You have guessed the number.")
            break  
    except ValueError:
        print("Please, type a valid number.")
