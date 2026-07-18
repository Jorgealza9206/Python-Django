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


