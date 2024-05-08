class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        print('Obtenemos el recurso'.center(50,'-'))
        self.nombre = open(self.nombre, 'r', encoding='utf-8')
        retur self.nombre

    def __exit__(self, tipo_excepcion, valor, traza_error):
        