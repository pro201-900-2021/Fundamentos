#Datos
    #"Hola"
    #5
    #7+8
    #["hola", "chao", 6]

#In/Out

print("Hola Mundo!")

#dato = input("Ingrese un dato: ")

'''
numero = 45
numero2 = 85

print(numero + numero2)

print(type(numero))

numero = "Cuarenta y cinco"

print(type(numero))

numero = 5.6

print(type(numero))

numero = []

print(type(numero))

integer = 4294967295

print(type(integer))
'''
##Una lista puede guardar elementos de tipos de dato variados, no así en lenguajes como c# o Java,
#donde las listas o arrays solo soportan un tipo de dato
##No se necesita inicializar con un número determinado
lista_de_muchas_cosas = [2, 5, 6, "hola", True, 8.3, ["otra", "lista"]]

print(lista_de_muchas_cosas)

##función append para agregar al final de la lista
lista_de_muchas_cosas.append(89)
lista_de_muchas_cosas.append("Estoy aprendiendo python")

print(lista_de_muchas_cosas)

#Puedo acceder a elementos de la lista a través de su index con la nomenclatura -lista[index]-
guardar_numero = lista_de_muchas_cosas[8]

print(guardar_numero)

##Puedo acceder al elemento a traves del index y modificarlo. (a menos que sea una tupla)
lista_de_muchas_cosas[8] = "Sigo aprendiendo pyhton"

print(lista_de_muchas_cosas)


'''
Strings
'''
# un string es básicamente una lista inmutable de carácteres
mi_string = "Oración de Prueba" # ["O", "r", "a", "c", "i", "ó", "n"]
print(mi_string)
# por lo tanto puedo acceder a las posiciones de los carácteres, pero no puedo cambiarlas individualmente
print(mi_string[3])
#mi_string[0] = "H" => Ésto no se puede hacer, ya que consideramos un string como una lista inmutable

##Las tuplas son listas inmutables, en el momento que se declaran e inicializan, quedarán de esa forma hasta el término de código
tupla_de_muchas_cosas = (2, 5, 6, "hola", True, 8.3, ["otra", "lista"])

##Y puedo acceder a sus elementos de la misma forma que las listas
print(tupla_de_muchas_cosas[0])

#{key: value}
#{clave: valor}
#{llave: valor}
#Dictionary<string, int> dic = new Dictonary<string, int>() {};

#Diccionarios son listas, pero en lugar de usar un índice(index), utilizamos clave:valor
diccionario = { "Monday": "Lunes", "Wednesday": "Miércoles", "Friday": "Viernes", "Saturday": "Sábado" }

##Y puedo trabajar con ellos al igual que las listas, pero en lugar de usar el índice, utilizo la clave para acceder o editar

print(diccionario)
print(diccionario["Monday"])

diccionario["Monday"] = 1

print(diccionario)

numero = int(input("Ingrese un número: "))

if numero > 50:
    print("Es Verdadero")
else:
    print("Es falso")


if numero == 1:
    print("Mi número es Uno")
elif numero == 2:
    print("Mi número es Dos")
elif numero == 3:
    print("Mi número es Tres")
else:#default del if
    print("El número no es ni uno ni dos ni tres")

