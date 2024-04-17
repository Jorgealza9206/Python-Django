class Monitor():
    contadorMonitores = 0

    def __init__(self, marca, tamanio):
        Monitor.contadorMonitores += 1
        self._marca = marca
        self._tamanio = tamanio
        self.idMonitor = Monitor.contadorMonitores

    def __str__(self):
        return f'Monitor: Id: {self.contadorMonitores}, marca: {self._marca}, tamaño: {self._tamanio}'

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamanio(self):
        return self._tamanio

    @tamanio.setter
    def tamanio(self,tamanio):
        self._tamanio = tamanio

m1 = Monitor('hp','15 pulgadas')
print(m1)
m1.tamanio = '18 pulgadas'
print(m1.tamanio)
print(m1)