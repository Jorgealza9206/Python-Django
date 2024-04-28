from Teclado import Teclado
from Monitor import Monitor
from Raton import Raton


class Computadora(Monitor,Teclado,Raton):
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
        return (f'\t{self._nombre} : {self.idComputadora}'
                f'\n\t\tMonitor: {self._monitor}'
                f'\n\t\tTeclado: {self._teclado}'
                f'\n\t\tRatón: {self._raton}')

r1 = Raton('usb', 'hp')
m2 = Monitor('hp', '15 pulgadas')
t1 = Teclado('bluetooth', 'lenovo')
c1 = Computadora('Gamer', m2, t1, r1)

if __name__ == '__main__':
    print(c1)
    c1.monitor = Monitor('dell', "22 pulgadas")
    c1.nombre = "Esccritorio"
    print(c1)