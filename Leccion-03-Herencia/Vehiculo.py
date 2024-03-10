class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'El vehiculo es de color {self.color} y tiene {self.ruedas} ruedas'

class Bicicleta(Vehiculo):
    def __init__(self,color,ruedas,tipo):
        super().__init__(color,ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'Bicicleta tipo {self.tipo}, {super().__str__()}'
        #return f'La bicileta es de color {super().__init__(color)}'

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'Coche tiene una velocidad de {self.velocidad}, {super().__str__()}'