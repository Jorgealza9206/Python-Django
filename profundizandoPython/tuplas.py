# Profundizando en tuplas

# Declarar variables
a, b = 'Hola', 'Adiós'
print(a,b) #En esta linea hacemops unpacking de la tupla
# swap (intercambio)
a, b = b, a
print(a,b)

# Regresar múltiples valores en una función
def minmax(elementos):
    return min(elementos), max(elementos)

min, max = minmax([1,2,3,4,5])
print(f'Valor minimo: {min}, Valor maximo: {max}')

# Regresar lña sumna de una tupla
resultado = sum([1,2,3,4,5])
print(f'Resultado: {resultado}')

def sumar(*args): # Recordar que el asterisco indica que podemos poner múltiples variables en nuestra función
    return sum(args)

resultado = sumar(1,2,3,4,5) # Para esta función se usan únicamente variables, no listas, no tuplas
print(f'Resultado: {resultado}')