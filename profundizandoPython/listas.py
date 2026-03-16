# Profundizando en listas
# Listas son mutables

nombres1 = ['Juan','Karla','Pedro']
nombres2 = 'Laura María Gonzalo Ernesto'.split()
# Sumar listas
print(f'Sumar listas {nombres1 + nombres2}')
# Extender una lista con otra lisat
nombres1.extend(nombres2)
print(f'Extender la lista1: {nombres1}')

# Lista de números
numeros1 = [10,40,15,4,20,90,4]
print(f'Lista original : {numeros1}')
# Obtener el índice del primer elemento encontrado de una lista
print(f'Índice 4: {numeros1.index(4)}')

# Invertir el orden de los elementos de una lista
numeros1.reverse()
print(f'Lista reversed : {numeros1}')

#Ordenar los elementos de una lista
numeros1.sort()
print(f'Lista ordenada ascendente : {numeros1}')
# Ordenar de manera descendente
numeros1.sort(reverse=True)
print(f'Lista ordenada descendente : {numeros1}')

#Obtener el valor mínimo mínimo y máximo de una lista

print(f'Valor mínimo: {min(numeros1)}')
print(f'Valor mánimo: {max(numeros1)}')

# Copiar los elementos de una lista
#No es una copia profunda, solo referencias
numeros2 = numeros1.copy()
print(numeros1)
print(numeros2)

print(f'Misma referencia? {numeros1 is numeros2}')
print(f'Mismo contenido? {numeros1 == numeros2}')

# Podemos usar el constructor de la lista
numeros2 = list(numeros1)
print(f'Misma referencia? {numeros1 is numeros2}')
print(f'Mismo contenido? {numeros1 == numeros2}')

#slicing
numeros2 = numeros1[:]
print(f'Misma referencia? {numeros1 is numeros2}')
print(f'Mismo contenido? {numeros1 == numeros2}')

#Matrices
matriz = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
print(f'Matriz original: {matriz}')
print(f'Renglón 0, Columna 0: {matriz[0][0]}')
print(f'Renglón 2, Columna 2: {matriz[2][2]}')
matriz[2][0] = 65
print(f'Matriz modificada: {matriz}')