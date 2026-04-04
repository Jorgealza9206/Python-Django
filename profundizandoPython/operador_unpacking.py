# * desempaquetar

numeros = [1,2,3]
print(numeros)
print(*numeros) #Imprime cada elemento por separado
print(*numeros, sep=" - ")


def sumar(a,b,c):
    return a+b+c

print(f'Resultado de la suma: {sumar(*numeros)}') #Pasa los parametros inmediatamente

#Extraer algunas partes de una lista
mi_lista = [1,2,3,4,5,6]
a,*b,c,d = mi_lista
print(a,b,c,d) #Con el operador unpacking, si la variable va marcada intenta encajar el máximo número de valores posible para encajar con la asignación

#Unir listas
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [lista1, lista2]
print(lista3)
lista3 = [*lista1, *lista2]
print(lista3)

#Unir diccionarios
dic1 = {'A':1, 'B':2, 'C':3}
dic2 = {'D':4, 'E':5, 'F':6}
dic3 = {**dic1, **dic2}
print(dic3)

#Construir una lista a través de un string
lista = [*'Holanda']
print(lista)
print(*lista)
print(*lista, sep="")
