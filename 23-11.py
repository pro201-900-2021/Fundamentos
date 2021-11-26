
def a_numero_positivo(numero):#función o método

    if numero < 0:
        numero = numero * (-1)

    return numero

#snake_case

#PascalCase
#camelCase

numero_ingresado = int(input("Ingrese un número entero: ")) #edad

numero_ingresado = a_numero_positivo(numero_ingresado)


#
if numero_ingresado >= 0 and numero_ingresado < 4:
    print("Usted es un bebé")
elif numero_ingresado >= 4 and numero_ingresado < 7:
    print("Usted es un niño")
elif numero_ingresado >= 7 and numero_ingresado < 18:
    print("Usted es un adolescente")
else:
    print("Usted es mayor")

