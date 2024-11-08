# Escribe un programa que, dado un número del 1 al 7, imprima el día correspondiente de la semana usando match.
# Solicita al usuario un número del 1 al 7 y muestra el día de la semana correspondiente (1 = Lunes, 7 = Domingo).

def semana(number):
    match number:
        case 1:
            monday = 'Today is Monday!'
            print(monday)
        case 2:
            tuesday = 'Today is Tuesday!'
            print(tuesday)
        case 3:
            wednesday = 'Today is Wednesday!'
            print(wednesday)
        case 4:
            thursday = 'Today is Thursday!'
            print(thursday)
        case 5:
            friday = 'Today is Friday!'
            print(friday)
        case 6:
            saturday = 'Today is Saturday!'
            print(saturday)
        case 7:
            sunday = 'Today is Sunday!'
            print(sunday)

number = int(input('Please type a number from 1 to 7: '))
semana(number)