
from Cuadrado import *
from Rectangulo import Rectangulo

print('Creación objeto Cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(5,'verde')
cuadrado1.alto = 9
print(f'La figura tiene un area de {cuadrado1.area()}')
print(cuadrado1)

print('Creación objeto Rectangulo'.center(50,'-'))
rectangulo1 = Rectangulo(9,2,'azul')
rectangulo1.alto = 15
print(f'La figura tiene un area de {rectangulo1.area()}')
print(rectangulo1)

#Method Resolution Order
print(Cuadrado.mro())