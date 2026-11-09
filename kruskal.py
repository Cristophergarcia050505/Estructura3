
def kruskal(nodos, aristas):

    # Ordenar las conexiones de menor a mayor peso
    aristas.sort(key=lambda x: x[2])

    padre = {}

    # Cada nodo comienza siendo su propio padre
    for nodo in nodos:
        padre[nodo] = nodo

    def buscar(nodo):

        if padre[nodo] != nodo:
            padre[nodo] = buscar(padre[nodo])

        return padre[nodo]

    arbol = []
    peso_total = 0

    # Revisar todas las conexiones
    for origen, destino, peso in aristas:

        raiz1 = buscar(origen)
        raiz2 = buscar(destino)

        # Comprobar que no se forme un ciclo
        if raiz1 != raiz2:

            arbol.append((origen, destino, peso))

            peso_total += peso

            padre[raiz1] = raiz2

    return arbol, peso_total


# Crear los nodos
nodos = ["A", "B", "C", "D"]

# Crear las conexiones con sus pesos
aristas = [
    ("A", "B", 4),
    ("A", "C", 2),
    ("B", "C", 1),
    ("B", "D", 5),
    ("C", "D", 8)
]

# Ejecutar algoritmo
arbol, total = kruskal(nodos, aristas)

print("Conexiones seleccionadas:")

for conexion in arbol:
    print(conexion)

print("Peso total:", total)
