# Escribe un programa que convierta grados Celsius a Fahrenheit o Fahrenheit a Celsius usando match.
# Solicita al usuario que ingrese una temperatura y una escala (C o F). 
# Convierte la temperatura a la escala opuesta usando match.

def conversor(temperature, operation):
    match operation:
        case 'c':
            result = ((temperature - 32) / 1.8)
            return round(result), 'Celsius'
        case 'f':
            result = ((temperature * 1.8) + 32)
            return round(result), 'Farenheit'

temperature = float(input('Please type the initial temperature to convert: '))
operation = input('Please select between Celsius or Farenheit scale(c \ f): ')
result = conversor(temperature, operation)
print(f'Te conversion is: {result}')