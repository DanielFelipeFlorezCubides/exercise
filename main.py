# Escribe un programa que calcule el número de créditos totales de un estudiante 
# en base a las materias cursadas y el puntaje obtenido en cada una.
# Solicita al usuario ingresar el número de materias que ha cursado. 
# Para cada materia, solicita el puntaje y determina si ha aprobado o no (>= 60). 
# Luego, calcula el número total de créditos del estudiante (cada materia aprobada otorga 3 créditos).

n = int(input('Type the subjects number you were coursing: '))
credits = 0

for i in range(n):
    grade = int(input(f'Type your grade on {i+1} subject (0 - 100): '))
    
    if grade >= 60:
        credits = credits + 3

print(f'The credits number you reached were: {credits}')