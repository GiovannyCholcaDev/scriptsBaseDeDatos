from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas

opcion = None
while opcion != 4:
    try:
        print("Opciones")
        print("1. Agregar peliculas")
        print("2. Listar peliculas")
        print("3. Eliminar catalogo peliculas")
        print("4. Salir")
        opcion = int(input("Ingresa tu opcion (1-4): "))

        if opcion == 1:
            nombre = input("Nombre de la pelicula: ")
            pelicula = Pelicula(nombre, 'accion')
            CatalogoPeliculas.agregarpelicula(pelicula)
        elif opcion == 2:
            CatalogoPeliculas.listarpelicula()

        elif opcion == 3:
            CatalogoPeliculas.eliminarpeliculas()

    except Exception as e:
        print("Error: " + str(e))
        opcion = None
else:
    print("Cerrando el programa")
