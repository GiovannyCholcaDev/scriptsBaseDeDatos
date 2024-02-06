class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_al_principio(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def eliminar(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                return
            actual = actual.siguiente

    def imprimir_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=' ')
            actual = actual.siguiente
        print()

    def imprimir_atras(self):
        actual = self.cola
        while actual:
            print(actual.dato, end=' ')
            actual = actual.anterior
        print()


# Ejemplo de uso
if __name__ == "__main__":
    lista = ListaDoblementeEnlazada()
    lista.insertar_al_principio(3)
    lista.insertar_al_principio(2)
    lista.insertar_al_final(4)
    lista.insertar_al_final(5)

    print("Lista doblemente enlazada (adelante):")
    lista.imprimir_adelante()  # Output: 2 3 4 5

    print("Lista doblemente enlazada (atras):")
    lista.imprimir_atras()  # Output: 5 4 3 2

    lista.eliminar(3)
    print("Después de eliminar 3:")
    lista.imprimir_adelante()  # Output: 2 4 5
