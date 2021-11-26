lista = [1,2,3,4,5]
tupla = (1,2,3,4,5)

lista.append(6) ##agregar elementos al final de una lista/array
##[1,2,3,4,5,6]
lista.pop() ##eliminar el último elemento de la lista, a menos que le
            # ingrese en el argumento una posición
            #[1,2,3,4,5]
lista.pop(1) ##elimina de la lista la posición indicada
#[1,3,4,5]
#delete
del lista[1]##elimina de la lista la posición indicada
#[1,4,5]
## lista.length
##lista.count

##de ambas formas, accedo al último elemento de la lista
print(lista[-1])
print(lista[len(lista)-1])

print(lista)

for i in range(5):
    print(i)

diccionario = {"Hombres": 13, "Mujeres": 16}

for i in diccionario:
    print(i)
    print(diccionario[i])

print(diccionario["Hombres"])

diccionario["Mujeres"] = diccionario["Mujeres"] - 1

print(diccionario["Mujeres"])

diccionario["Profesores"] = 2

print(diccionario)

del diccionario["Profesores"]
print(diccionario)

diccionario.pop("Hombres")

print(diccionario)

range(8) ##[0,1,2,3,4,5,6,7]
range(2,6) ## [2,3,4,5]

## (C#) for(int i = 50; i<100; i++){

#mientras
numero = True
while numero:
    print("Sigo dentro del bucle...")
    numero = False