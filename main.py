# Escribe un programa que asigne una calificación basada en una nota numérica.
# Solicita una nota numérica y clasifícala como A (90-100), B (80-89), C (70-79), D (60-69), o F (<60).

def grade_classification(grade):
    match grade:
        case g if 90 <= g <= 100:
            return "A"
        case g if 80 <= g <= 89:
            return "B"
        case g if 70 <= g <= 79:
            return "C"
        case g if 60 <= g <= 69:
            return "D"
        case g if 0 <= g <= 59:
            return "F"
        case _:
            print('That number is out of range')

grade = float(input('Please type your grade: '))
classification = grade_classification(grade)
print(f'Your score was: {classification}')