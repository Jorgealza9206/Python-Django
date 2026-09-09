# print(dir(__builtins__))
# help(zip)

numeros = [1,2,3]
letras = ['a','b','c','d']
identificadores = 321, 322, 323, 324, 325 #Esto se convierte automáticamente en una tupla
conjunto = {6,4,0,9,8,15,10}
mezcla = zip(numeros, letras, identificadores, conjunto)
#"La función zip en este caso ejecutará hasta el iterable de menor número de elementos
#print(mezcla)
print(list(mezcla))
#Se puede mezclar varias listas o una tupla con una lista y las mezclas siempre quedan como tuplas

# mezcla = zip(numeros, letras)
# print(tuple(mezcla))

#iterar en paralelo
for numero, letra, id, aleatorio in zip(numeros, letras, identificadores, conjunto):
    print(f'Número: {numero}, Letra: {letra}, Id: {id}, Aleatorio: {aleatorio}')

nueva_lista = []

for numero, letra, id, aleatorio in zip(numeros, letras, identificadores, conjunto):
    nueva_lista.append(f'{id}-{numero}-{letra}-{aleatorio}')
    #Crea una lista del primer elemento de cada uno de los elementos del zip en cada iteración
print(nueva_lista)

#unzip
mezcla = [(1,'a'),(2,'b'),(3,'c'),(4,'d')]
numeros, letras = zip(*mezcla) #Se separa primero número en números y letra en letras
print(f'Numeros: {numeros}, Letras: {letras}')

#ordenamiento
letras = ['c','d','a','e','b']
numeros = [3,2,4,1,0]
mezcla = zip(letras, numeros)
#Sin orden
print(tuple(mezcla))
#Ordenar por letra (primer iterable)
print(sorted(zip(letras, numeros))) # En este caso el orden lo marca las letras de manera descendente
print(sorted(zip(numeros, letras))) # En este caso el orden lo marca los números

# Crear un diccionario con zip y dos iterables
llaves = ['Nombre','Apellido','Edad']
valores = ['Juan','Pérez',18]
diccionario = dict(zip(llaves, valores))
print(diccionario)

#Actualizar un elemento de un diccionario
llave = ['Edad'] # Es vital que se llame igual que la llave a la que se va a modificar por que o sino no la cambia y
# se agrega una nueva llave
nueva_edad = [28]
diccionario.update(zip(llave, nueva_edad)) #En este metodo vamos a reemplazar la edad dentro del diccionario
print(diccionario)