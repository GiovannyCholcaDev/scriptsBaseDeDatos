class Pelicula:
    def __init__(self, nombre, tipo):
        self._nombre = nombre
        self._tipo = tipo

    def __str__(self):
        return f"Nombre: {self._nombre}"

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo
