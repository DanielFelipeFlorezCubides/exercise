# Escribe un programa que determine si una nota numérica es "Aprobado" o "Reprobado" usando if.

grade = float(input('Please gimme the grade you scored (0/10): '))

if grade < 6.5:
    print('Failed')
else:
    print('Approved')