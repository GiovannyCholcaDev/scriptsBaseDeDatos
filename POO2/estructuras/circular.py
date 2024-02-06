class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cabeza.siguiente = self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza

    def eliminar(self, dato):
        if not self.cabeza:
            return
        if self.cabeza.dato == dato:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = self.cabeza.siguiente
            self.cabeza = self.cabeza.siguiente
        else:
            previo = None
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                previo = actual
                actual = actual.siguiente
                if actual.dato == dato:
                    previo.siguiente = actual.siguiente
                    actual = actual.siguiente

    def imprimir(self):
        if not self.cabeza:
            return
        actual = self.cabeza
        while True:
            print(actual.dato, end=' ')
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        print()


# Ejemplo de uso
if __name__ == "__main__":
    lista = ListaCircular()
    lista.insertar(1)
    lista.insertar(2)
    lista.insertar(3)
    lista.insertar(4)

    print("Lista circular:")
    lista.imprimir()  # Output: 1 2 3 4

    lista.eliminar(3)
    print("Después de eliminar 3:")
    lista.imprimir()  # Output: 1 2 4
