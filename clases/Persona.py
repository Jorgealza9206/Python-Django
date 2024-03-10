class Persona:
    def __init__(self,nombre, apellido, edad, *args, **kwargs):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrarDetalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.args} {self.kwargs}')

persona1 = Persona('Cristian','Guayacundo',26)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona1.mostrarDetalle()

persona2 = Persona('Daniel','Ruiz',20,'0000',1,5, cargo = 'Ciberseguridad', almuerzo = '12:30')

persona2.mostrarDetalle()