import os
from pathlib import Path


class CatalogoPeliculas:
    ruta_archivo = 'peliculas.txt'

    @classmethod
    def agregarpelicula(cls, pelicula):
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f"{pelicula.nombre}, {pelicula.tipo}\n")
            print('Se agrego la pelicula'.center(50, '-'))

    @classmethod
    def listarpelicula(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
            print('Lectura del archivo'.center(50, '-'))
            print(archivo.read())

    @classmethod
    def eliminarpeliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f"El archivo fue eliminado {cls.ruta_archivo}".center(50, '-'))
