#Unpacking

valores = 1,2,3 # Por defecto0 esto se considera una tupla
print(valores)
print(type(valores))

valor1, valor2, valor3 = 1, 2, 3
print(valor1, valor2, valor3)

valor1, _, valor3 = 1, 2, 3 #Sintaxís especificada para evitar asignar un valor
print(valor1, valor3)

#valor1, valor2, valor3 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 #Error de sintáxis porque python no puede desempaquetar tantas variables
#de esta manera

valor1, valor2, *valor3 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 # El último valor lo asigna a una lista
print(valor1, valor2, valor3)

valor1, valor2, *valor3, valor4, valor5 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# En este caso los dos primeros y dos últimos valores se asignan a las variables correspondientes y en medio queda
# una lista para los restantes
print(valor1, valor2, valor3, valor4, valor5)

#Esta ejecución no cambia nada
valor1, valor2, *valor3, valor4, valor5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(valor1, valor2, valor3, valor4, valor5)
print(type(valor3))

def regresa_varios_datos():
    return 1, 2, 3

valor1, valor2, valor3 = regresa_varios_datos()
print(valor1, valor2, valor3)

valor1, *valores_restantes = regresa_varios_datos() #Novamos a procesar los últimos valores
print(valor1, valores_restantes)
