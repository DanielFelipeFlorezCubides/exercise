# Utiliza match para implementar una calculadora simple.

def calculator(number_1, number_2, operation):
    match operation:

        case '+':
            sum = number_1 + number_2
            print(sum)
        case '-':
           minus = number_1 - number_2
           print(minus)
        case 'x':
            times = number_1 * number_2
            print(times)
        case '/':
            division = number_1 / number_2
            print(division)
        case _:
            print('''Operation didn't recognize''')

operation = input('Please tell me which operation you wanna execute( + , - , x , /): ')
number_1 = int(input('Please gimme a number: '))
number_2 = int(input('Please gimme another number: '))
    
calculator(number_1, number_2,operation)
