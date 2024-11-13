# Escribe un programa que solicite al usuario ingresar números enteros indefinidamente.
# El programa debe sumar los números siempre que sean pares, pero debe detenerse si el usuario ingresa un número impar. 
# Usa un ciclo while para lograr esto.

# Inicializar la suma
pairs = 0

print("Type integer numbers, the program will sum pair numbers but if you type an unpair one it will finish.")

while True:
    try:
        # Solicitar al usuario un número entero
        number = int(input("Type your number: "))
        
        # Comprobar si el número es impar
        if number % 2 != 0:
            print("You typed an unpair number, the program has just finished.")
            break  # Salir del bucle si el número es impar
        
        # Si el número es par, añadirlo a la suma
        pairs += number
        print(f"The current sum is: {pairs}")
    
    except ValueError:
        print("Please, type a valid number.")
