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
        return (f'{self._nombre} : {self.idComputadora}'
                f'\n\tMonitor: {m1.__str__()}'
                f'\n\tTeclado: {t1.__str__()}'
                f'\n\tRatón: {r1.__str__()}')

r1 = Raton('usb','hp')
m1 = Monitor('hp','15 pulgadas')
t1 = Teclado('bluetooth', 'lenovo')
c1 = Computadora('Gamer', m1, '', '')
print(c1)