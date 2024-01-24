class NodoDobleEnlace:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.fin = None

    def agregar_elemento(self, dato):
        nuevo_nodo = NodoDobleEnlace(dato)
        if self.cabeza is None:
            print()
            self.cabeza = nuevo_nodo
            self.fin = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.fin
            self.fin.siguiente = nuevo_nodo
            self.fin = nuevo_nodo

    def imprimir_lista_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.siguiente
        print("None")

    def imprimir_lista_atras(self):
        actual = self.fin
        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.anterior
        print("None")

# Ejemplo de uso
mi_lista_doble_enlazada = ListaDobleEnlazada()
mi_lista_doble_enlazada.agregar_elemento(1)
mi_lista_doble_enlazada.agregar_elemento(2)
mi_lista_doble_enlazada.agregar_elemento(3)

print("Lista en sentido directo:")
mi_lista_doble_enlazada.imprimir_lista_adelante()

print("\nLista en sentido inverso:")
mi_lista_doble_enlazada.imprimir_lista_atras()
