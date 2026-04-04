# * desempaquetar

numeros = [1,2,3]
print(numeros)
print(*numeros) #Imprime cada elemento por separado
print(*numeros, sep=" - ")


def sumar(a,b,c):
    return a+b+c

print(f'Resultado de la suma: {sumar(*numeros)}') #Pasa los parametros inmediatamente