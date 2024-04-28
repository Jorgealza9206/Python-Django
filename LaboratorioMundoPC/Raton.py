from DispositivoEntrada import Dispositivo
class Raton(Dispositivo):
    contador = 0

    def __init__(self, tipoEntrada, marca):
        Raton.contador += 1
        self.idRaton = Raton.contador
        super().__init__(tipoEntrada,marca)

    def __str__(self):
        return f'Ratón: Id: {self.idRaton} {super ().__str__()}'


if __name__== '__main__':
    r1 = Raton('usb', 'hp')
    print(r1)
