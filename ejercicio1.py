'''
Escribir un programa que almacene la cadena de caracteres "" en una variable, pregunte al usuario por la
contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable
sin tener en cuenta mayúsculas y minúsculas.
'''

variable = "yosoy145"
otra_variable = "yosoy145"

print("Ingrese su contraseña: ")
otra_variable = input()

# = <- establecemos valores, le damos valores a las variables
# == <- comparando y preguntando si ambos lados son iguales -> Verdadero o falso

# === <-- identidad, compara si ambos lados(ambos objetos) son idénticos

if variable == otra_variable:
    print("La contraseña ingresada coincide!")
else:
    print("La contraseña ingresada no coincide!")

#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

variable = int(input("Ingrese un número entero: "))

if variable % 2 == 0:
    print("El número es par!")
elif variable % 2 != 0:
    print("El número es impar!")

##Ingresar un número del 1 al 7 e imprimir por pantalla a que día de la semana corresponde

variable = int(input("Ingrese un número que represente el día de la semana!"))

if variable == 1:
    print("Es día Lunes")
elif variable == 2:
    print("Es día Martes")
elif variable == 3:
    print("Es día Miércoles")
elif variable == 4:
    print("Es día Jueves")
elif variable == 5:
    print("Es día Viernes")
elif variable == 6:
    print("Es día Sábado")
elif variable == 7:
    print("Es día Domingo")
else:
    print("No hay día para el número")

tupla_dias = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo")

variable = int(input("Ingrese un número que represente el día de la semana!"))

print("Es día ", tupla_dias[variable-1])

