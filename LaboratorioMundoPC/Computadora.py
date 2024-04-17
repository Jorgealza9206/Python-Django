from Monitor import Monitor


class Computadora:
    contadorComputadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contadorComputadoras += 1
        self.idComputadora = Computadora.contadorComputadoras
        self._nombre = nombre
        self._monitor = monitor

    def __str__(self):
        return f'Id: {self.idComputadora} Nombre: {self._nombre}, Monitor: {Monitor.__str__()}'

c1 = Computadora('Gamer', Monitor('HP','22 pulgadas'),'','')
print(c1)