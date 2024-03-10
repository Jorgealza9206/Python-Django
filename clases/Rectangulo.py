class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

base = int(input(f'Proporcione una base: '))
altura = int(input(f'Proporcione una altura: '))

rectangulo1 = Rectangulo(base, altura)
print(f'Área rectángulo: {rectangulo1.calcularArea()}')