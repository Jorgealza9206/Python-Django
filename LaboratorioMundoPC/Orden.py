from Computadora import c1, Computadora
from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado


class Orden:
    contadorOrdenes = 0

    def __init__(self, computadoras):
        Orden.contadorOrdenes += 1
        self._idOrden = Orden.contadorOrdenes
        self._computadoras = list(computadoras)

    def agregarComputadora(self,computadora):
        self._computadoras.append(computadora)

    @property
    def computadoras(self):
        return self._computadoras

    @computadoras.setter
    def computadoras(self, computadoras):
        self._computadoras = list(computadoras)

    def __str__(self):
        computadoras_str = ''

        for computadora in self._computadoras:
            computadoras_str += '' + computadora.__str__() + '\n'

        return (f'Orden: {self._idOrden}, computadoras:\n'
              f'{computadoras_str}')

if __name__ == '__main__':
    r1 = Raton('usb','genius')
    t1 = Teclado('bluetooth','lenovo')
    m1 = Monitor('samsung','22 pulgadas')
    c2 = Computadora('Escritorio', m1, t1, r1)
    orden1 = Orden([c1,c2])
    print(c1)
    print(orden1)