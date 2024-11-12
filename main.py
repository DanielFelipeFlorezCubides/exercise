# Escribe un programa que calcule el salario neto de un empleado después de aplicar impuestos.
# Solicita al usuario su salario bruto y su país de residencia. 
# Calcula el salario neto aplicando impuestos: el 20% para residentes de "País A", 
# el 15% para "País B" y el 10% para "País C". Si el país no está en la lista, aplica un 25% de impuestos.

wage = float(input("Type your wage: "))
country = input("Type your country (A,B,C) countries that are not listed will be deducted with 25%: ")

if country.upper() == "A":
    print("Taxes payment of 20'%' has made")
    discount = wage * 0.20
    new_wage = wage - discount
    print(f"Your income is: {new_wage}")
elif country.upper() == "B":
    print("Taxes payment of 15'%' has made")
    discount = wage * 0.15
    new_wage = wage - discount
    print(f"Your income is: {new_wage}")
elif country.upper() == "C":
    print("Taxes payment of 10'%' has made")
    discount = wage * 0.10
    new_wage = wage - discount
    print(f"Your income is: {new_wage}")
else:
    print("Taxes payment of 25'%' has made")
    discount = wage * 0.25
    new_wage = wage - discount
    print(f"Your income is: {new_wage}")