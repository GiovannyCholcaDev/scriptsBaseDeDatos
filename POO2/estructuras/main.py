class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_principio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def eliminar(self, dato):
        actual = self.cabeza
        if actual.dato == dato:
            self.cabeza = actual.siguiente
            return
        while actual.siguiente:
            if actual.siguiente.dato == dato:
                actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=' ')
            actual = actual.siguiente
        print()


# Ejemplo de uso
if __name__ == "__main__":
    lista = ListaEnlazada()
    lista.insertar_al_principio(3)
    lista.insertar_al_principio(2)
    lista.insertar_al_final(4)
    lista.insertar_al_final(5)

    print("Lista enlazada:")
    lista.imprimir()  # Output: 2 3 4 5

    lista.eliminar(3)
    print("Después de eliminar 3:")
    lista.imprimir()  # Output: 2 4 5
