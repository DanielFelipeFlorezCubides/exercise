# Escribe un programa que permita al usuario adivinar una letra secreta usando match.
# El programa contiene una letra secreta (por ejemplo, "A"). 
# El usuario debe adivinar la letra, y el programa le indicará si acertó o no.

import random
import string

letra_secreta = random.choice(string.ascii_uppercase)
letra_usuario = input("Adivina la letra secreta (de A a Z): ").upper()

if letra_usuario == letra_secreta:
    print("¡Felicidades! Adivinaste la letra secreta.")
else:
    print(f"Lo siento, esa no es la letra secreta. La letra correcta era: {letra_secreta}.")
