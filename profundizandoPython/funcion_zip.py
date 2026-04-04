# print(dir(__builtins__))
# help(zip)

numeros = [1,2,3]
letras = ['a','b','c']
mezcla = zip(numeros, letras)
print(mezcla)
print(list(mezcla))
#Se puede mezclar varias listas o una tupla con una lista y las mezclas siempre quedan como tuplas

mezcla = zip(numeros, letras)
print(tuple(mezcla))
