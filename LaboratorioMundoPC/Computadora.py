from Teclado import Teclado
from Monitor import Monitor
from Raton import Raton


class Computadora:
    contadorComputadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contadorComputadoras += 1
        self.idComputadora = Computadora.contadorComputadoras
        self._nombre = nombre
        self._monitor = monitor

    def __str__(self):
        return f'Id: {self.idComputadora} Nombre: {self._nombre}, Monitor: {Monitor().__str__()}'

r1 = Raton('usb','hp')
m1 = Monitor('hp','15 pulgadas')
t1 = Teclado('bluetooth', 'lenovo')
c1 = Computadora('Gamer', Monitor('hp','15 pulgadas'), '', '')
print(c1)