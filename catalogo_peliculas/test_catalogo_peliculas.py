from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas
import time

nuevocatalogo = CatalogoPeliculas()

while(True):
    print('''Opciones:
    1. Agregar pelicula
    2. Listar peliculas
    3. Eliminar catálogo de peliculas
    4. Salir''')

    opcion = int(input('Escribe tu opción (1-4): '))

    if opcion == 1:
        pelicula = Pelicula(input('Ingresa el nombre de la pelicula: '))
        nuevocatalogo.agregar_pelicula(pelicula)
    elif opcion == 2:
        nuevocatalogo.listar_pelicula()
    elif opcion == 3:
        nuevocatalogo.eliminar()
    elif opcion == 4:
        break
    else:
        continue

    time.sleep(3)

