# Escribe un programa que calcule la calificación final de un estudiante basándose en su calificación y si ha hecho tareas adicionales.
# Solicita la calificación del estudiante y pregunta si hizo tareas adicionales. 
# Si la respuesta es "sí", añade un 5% extra a la calificación, pero si la calificación supera 100, ajústala a 100. 
# Si la respuesta es "no", simplemente muestra la calificación original.


def bonificacion(grade,aditional):
    if aditional == "Y" and grade <100 and grade >= 0: 
        grade = (grade *0.05) + grade
        if grade > 100:
            grade = 100
    print("The final grade is:",grade)

grade = float(input("Type your grade: "))
aditional = input("Does the student got bonifications? (Y/N): ").upper()
bonificacion(grade,aditional)