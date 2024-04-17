class Dispositivo:

    def __init__(self, tipoEntrada, marca):
        self._tipoEntrada = tipoEntrada
        self._marca = marca

    @property
    def tipoEntrada(self):
        return self._tipoEntrada

    @tipoEntrada.setter
    def tipoEntrada(self, tipoEntrada):
        self._tipoEntrada = tipoEntrada

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca


    def __str__(self):
        return f'marca: {self._marca}, tipo_entrada: {self._tipoEntrada}'

new = Dispositivo('usb','hp')
print(new)
new.marca = 'lenovo'
new.tipoEntrada = 'bluetooth'
print(new)
