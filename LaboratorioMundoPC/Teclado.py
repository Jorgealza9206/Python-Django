from DispositivoEntrada import Dispositivo

class Teclado(Dispositivo):
    contador = 0

    def __init__(self, tipoEntrada, marca):
        Teclado.contador += 1
        self.idTeclado = Teclado.contador
        super().__init__(tipoEntrada, marca)

    def __str__(self):
        return f'Teclado: Id: {self.idTeclado} {super().__str__()}'

if __name__== '__main__':
    t1 = Teclado('bluetooth', 'lenovo')
    print(t1)