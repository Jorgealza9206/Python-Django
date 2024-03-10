class Persona2:
    def __init__(self,nombre, apellido, edad, *args, **kwargs):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self.args = args
        self.kwargs = kwargs

    @property #decorador
    def nombre(self):
        print('Llamando método get nombre')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        print('Llamando método set nombre')
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return _edad

    @edad.setter
    def edad(self,edad):
        self._edad = edad

    def mostrarDetalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad} {self.args} {self.kwargs} ')

    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido} ')

if __name__ == '__main__':
    persona1 = Persona2('Cristian', 'Guayacundo', 26)
    # print(persona1._nombre)
    # print(persona1._apellido)
    # print(persona1._edad)

    persona1.mostrarDetalle()

    persona2 = Persona2('Daniel', 'Ruiz', 20, '0000', 1, 5, cargo='Ciberseguridad', almuerzo='12:30')

    persona2.mostrarDetalle()

    print(persona1.nombre)  # Método sin paréntesis por el @property
    persona1.nombre = 'Karen Lizeth'
    print(persona1.nombre)
    persona1.apellido = 'Herrera Huertas'
    persona1.edad = 30
    persona1.mostrarDetalle()