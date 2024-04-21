from Teclado import Teclado
from Monitor import Monitor, m1
from Raton import Raton


class Computadora:
    contadorComputadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contadorComputadoras += 1
        self.idComputadora = Computadora.contadorComputadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def nombre(self, teclado):
        self._teclado = teclado

    @property
    def raton(self):
        return self._raton

    @raton.setter
    def raton(self, raton):
        self._raton = raton

    def __str__(self):
        return (f'{self._nombre} : {self.idComputadora}'
                f'\n\tMonitor: {Monitor.__str__()}'
                f'\n\tTeclado: {Teclado.__str__()}'
                f'\n\tRatón: {Raton.__str__()}')

r1 = Raton('usb','hp')
m2 = Monitor('hp','15 pulgadas')
t1 = Teclado('bluetooth', 'lenovo')
c1 = Computadora('Gamer', m2, '', '')
print(c1)
c1.monitor = Monitor('dell',"22 pulgadas")
c1.nombre = "Esccritorio"
print(c1)