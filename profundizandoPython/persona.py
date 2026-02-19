class Persona:
    def __init__(self, nombre, apellido):  # Método constructor
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):  # Método que imprime
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, id: {hex(id(self)).upper()}'

if __name__ == '__main__':
    persona1 = Persona('Juan', 'Pérez')
    print(persona1)

def mostrar_mensaje(mensaje):
    print(mensaje)
