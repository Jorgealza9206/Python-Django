def multiplicar_valores(*numeros):
    resultado = 1
    for i in numeros:
        resultado *= i

    return resultado

print(multiplicar_valores(1,5,8,3))
