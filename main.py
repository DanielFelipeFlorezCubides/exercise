# Escribe un programa que solicite al usuario una cadena de texto y cuente cuántas vocales (a, e, i, o, u) contiene. 
# Usa un ciclo for para recorrer la cadena y realizar la cuenta.

""" 
a = 0
e = 0
i = 0
o = 0
u = 0
while True:
    try:
        word = input('Pleas type a word: ')
        if word != str:
            raise ValueError()
        
        for i in range(word.lower):
            match word:
                case 'a':
                    a += 1
                case 'e':
                    e += 1
                case 'i':
                    i += 1
                case 'o':
                    o += 1
                case 'u':
                    u += 1
        print(f'''
        The number of vocals in this word are the following:
                \n For a is: {a}
                \n for e is: {e}
                \n for i is: {i}
                \n for o is: {o}
                \n for u is: {u}
        ''')
        break
    except ValueError as e:
        print('Dear user, you can only type words. Please correct it') """

# This was my try

# The following code was corrected by chatgpt
# Programa que cuenta las vocales en una cadena ingresada por el usuario

# Inicializar contadores para cada vocal
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

while True:
    try:
        # Solicitar al usuario que ingrese una palabra
        word = input('Por favor, ingresa una palabra: ').lower()  # Convertir a minúsculas para facilitar la comparación
        
        # Verificar que el input no esté vacío
        if not word.isalpha():  # Comprobar que la entrada solo contenga letras
            raise ValueError()
        
        # Recorrer la cadena y contar las vocales
        for char in word:
            if char == 'a':
                count_a += 1
            elif char == 'e':
                count_e += 1
            elif char == 'i':
                count_i += 1
            elif char == 'o':
                count_o += 1
            elif char == 'u':
                count_u += 1

        # Imprimir el resultado
        print(f'''
        El número de vocales en esta palabra es el siguiente:
            a: {count_a}
            e: {count_e}
            i: {count_i}
            o: {count_o}
            u: {count_u}
        ''')
        break  # Salir del bucle si se ha procesado correctamente

    except ValueError:
        print('Estimado usuario, solo puedes ingresar palabras que contengan letras. Por favor, corrígelo.')
