
# Clase para crear los nodos
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# Clase para crear la lista enlazada
class LinkedList:
    def __init__(self):
        self.cabeza = None

    # Agregar un elemento al final
    def insertar(self, dato):
        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza

            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = nuevo

    # Mostrar todos los elementos
    def mostrar(self):
        actual = self.cabeza

        if actual is None:
            print("La lista esta vacia")
            return

        while actual is not None:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente

        print("None")

    # Buscar un elemento
    def buscar(self, dato):
        actual = self.cabeza

        while actual is not None:
            if actual.dato == dato:
                print("Elemento encontrado:", dato)
                return True

            actual = actual.siguiente

        print("Elemento no encontrado:", dato)
        return False

    # Eliminar un elemento
    def eliminar(self, dato):
        actual = self.cabeza
        anterior = None

        while actual is not None:
            if actual.dato == dato:

                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente

                print("Elemento eliminado:", dato)
                return

            anterior = actual
            actual = actual.siguiente

        print("El elemento no existe:", dato)


# Programa principal
lista = LinkedList()

lista.insertar(10)
lista.insertar(20)
lista.insertar(30)
lista.insertar(40)

print("Lista original:")
lista.mostrar()

print("\nBuscando el numero 30:")
lista.buscar(30)

print("\nEliminando el numero 20:")
lista.eliminar(20)

print("\nLista actualizada:")
lista.mostrar()
