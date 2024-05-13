import os

class CatalogoPeliculas:
    ruta_archivo = 'peliculas.txt'

    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.ruta_archivo,'a',encoding='utf-8') as archivo:
            archivo.write(f'{pelicula.__str__()}\n')
            print(f'Pelicula {pelicula} agregada')

    @classmethod
    def listar_pelicula(cls):
        try:
            with open(cls.ruta_archivo, 'r', encoding='utf-8') as archivo:
                print(archivo.read())
        except:
            print("No hay catálogo creado")

    @classmethod
    def eliminar(cls):
        os.remove(cls.ruta_archivo)
        print('Archivo eliminado con éxito')
