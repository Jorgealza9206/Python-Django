class Color:
    def __init__(self, color):
        self._color = color

    @property
    def get_color(self):
        return self._color

''' Tenemos errores frente a los setter por el momento vamos a ejecutar el codigo evitando hacerlos'''
    # @color.setter
    # def set_color(self, color):
    #     self._color = color

    def __str__(self):
        return f'La figura es de color {self._color}'