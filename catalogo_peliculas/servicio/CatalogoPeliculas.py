import os

class CatalogoPeliculas:
    ruta_archivo = 'peliculas.txt'

    def agregar_pelicula(self, pelicula):
        with open(self.ruta_archivo,'a',encoding='utf-8') as archivo:
            archivo.write(f'{pelicula.__str__()}\n')
            print(f'Pelicula {pelicula} agregada')

    def listar_pelicula(self):
        try:
            with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
                print(archivo.read())
        except:
            print("No hay catálogo creado")


    def eliminar(self):
        os.remove(self.ruta_archivo)
        print('Archivo eliminado con éxito')
