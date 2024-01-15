def imprimirNumeros(numero):
    if numero == 1:
        print(numero)
    elif numero < 1:
        print('')
    else:
        print(numero)
        imprimirNumeros(numero-1)

numero = int(input("Indique el numero\n"))
imprimirNumeros(numero)

