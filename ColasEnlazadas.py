
# Practica 1.2: Cola con listas enlazadas

# Clase que representa cada nodo
class Node:
    def __init__(self, info):
        self.info = info
        self.next = None


# Clase que representa un pedido
class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print(self):
        print("Cliente:", self.customer)
        print("Cantidad:", self.qtty)
        print("------------")


# Clase Cola
class Queue:
    def __init__(self):
        self.top = None
        self.tail = None
        self.count = 0

    # Regresa el numero de elementos
    def size(self):
        return self.count

    # Verifica si la cola esta vacia
    def isEmpty(self):
        return self.top is None

    # Consulta el primer elemento sin eliminarlo
    def front(self):
        if self.isEmpty():
            return None
        return self.top.info

    # Agrega un elemento al final
    def enqueue(self, info):
        nuevo = Node(info)

        if self.isEmpty():
            self.top = nuevo
            self.tail = nuevo
        else:
            self.tail.next = nuevo
            self.tail = nuevo

        self.count += 1

    # Elimina y devuelve el primer elemento
    def dequeue(self):
        if self.isEmpty():
            return None

        elemento = self.top.info
        self.top = self.top.next
        self.count -= 1

        if self.top is None:
            self.tail = None

        return elemento

    # Imprime todos los elementos de la cola
    def printInfo(self):
        print("\n********** QUEUE DUMP **********")
        print("Tamaño:", self.size())

        nodo = self.top
        posicion = 1

        while nodo is not None:
            print("\n** Elemento", posicion)
            nodo.info.print()
            nodo = nodo.next
            posicion += 1

        print("********************************")

    # Obtiene un elemento sin eliminarlo
    # Las posiciones comienzan en 1
    def getNth(self, pos):
        if pos < 1 or pos > self.count:
            return None

        nodo = self.top
        posicion = 1

        while posicion < pos:
            nodo = nodo.next
            posicion += 1

        return nodo.info


# Programa principal para probar la cola
def TestQueue():
    cola = Queue()

    print("AGREGANDO PEDIDOS")

    pedido1 = Order(20, "Cliente 1")
    cola.enqueue(pedido1)
    cola.printInfo()

    pedido2 = Order(30, "Cliente 2")
    cola.enqueue(pedido2)
    cola.printInfo()

    pedido3 = Order(40, "Cliente 3")
    cola.enqueue(pedido3)
    cola.printInfo()

    pedido4 = Order(50, "Cliente 4")
    cola.enqueue(pedido4)
    cola.printInfo()

    # Probar front
    print("\nPRIMER PEDIDO (FRONT)")
    primero = cola.front()

    if primero is not None:
        primero.print()

    cola.printInfo()

    # Probar getNth
    print("\nTERCER PEDIDO (getNth)")
    tercero = cola.getNth(3)

    if tercero is not None:
        tercero.print()
    else:
        print("Posicion no valida")

    # Probar dequeue
    print("\nELIMINANDO EL PRIMER PEDIDO (DEQUEUE)")
    eliminado = cola.dequeue()

    if eliminado is not None:
        eliminado.print()

    cola.printInfo()

    # Probar cola vacia
    print("\n¿La cola esta vacia?", cola.isEmpty())


if __name__ == "__main__":
    TestQueue()
