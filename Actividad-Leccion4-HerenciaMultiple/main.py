
from Cuadrado import *
from Rectangulo import Rectangulo

print('Creación objeto Cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(-5,'verde')
print(f'La figura tiene un area de {cuadrado1.area()}')
print(cuadrado1)

print('Creación objeto Rectangulo'.center(50,'-'))
rectangulo1 = Rectangulo(14,2,'azul')
print(f'La figura tiene un area de {rectangulo1.area()}')
print(rectangulo1)