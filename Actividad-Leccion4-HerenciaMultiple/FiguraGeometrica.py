class FiguraGeometrica:
    def __init__(self, alto, ancho):
        self._alto = alto
        self._ancho = ancho

    @property
    def get_alto(self):
        return self._alto

    @property
    def get_ancho(self):
        return self._ancho

''' Tenemos errores frente a los setter por el momento vamos a ejecutar el codigo evitando hacerlos'''

    # @alto.setter
    # def alto(self, alto):
    #     self._alto = alto
    #
    # @ancho.setter
    # def ancho(self, ancho):
    #     self._ancho = ancho

    def __str__(self):
        return f'La figura tiene un alto de {self._alto} y un ancho de {self._ancho}'