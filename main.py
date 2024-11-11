# Escribe un programa que clasifique a una persona en función de su edad.
# Solicita la edad de la persona e indica si es niño (0-12 años), 
# adolescente (13-17 años), adulto (18-64 años) o anciano (65 años o más).

age = int(input('Plese type your age: '))

if age <= 12:
    print('''You're a kid''')
elif age > 12 and age <= 17:
    print('''You're a teenager''')
elif age > 17 and age <= 64:
    print('''You're an adult''')
elif age > 64 and age <= 120:
    print('''You're a senior''')
else:
    print('Error, a human cannot live more than 120 years')