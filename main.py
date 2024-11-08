# Escribe un programa que implemente un juego de adivinanza de números.
# El programa genera un número aleatorio entre 1 y 10. El usuario debe adivinar el número, 
# y el programa indica si el número ingresado es mayor, menor o igual al número generado.
import random

def guessing_game():
    rNumber = int(random.randint(1,10))
    print('I generated a random number between 1 to 10, try to guess wich one is it!')

    guess = False

    while not guess:
        n = int(input('Type your guess: '))
        if n < rNumber:
            print('Your guess is less than the choosen one!')
        elif n > rNumber:
            print('Your guess is higher than the choosen one!')
        else:
            print(f'Congrats, you have guessed the number!')
            guess = True

guessing_game()