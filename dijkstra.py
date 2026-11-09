
def dijkstra(grafo, inicio):

    distancias = {}

    # Asignar distancia infinita a todos los nodos
    for nodo in grafo:
        distancias[nodo] = float("inf")

    # La distancia del nodo inicial es cero
    distancias[inicio] = 0

    visitados = []

    while len(visitados) < len(grafo):

        menor = float("inf")
        nodo_actual = None

        # Buscar el nodo con menor distancia
        for nodo in grafo:
            if nodo not in visitados and distancias[nodo] < menor:
                menor = distancias[nodo]
                nodo_actual = nodo

        if nodo_actual is None:
            break

        visitados.append(nodo_actual)

        # Revisar los nodos vecinos
        for vecino, peso in grafo[nodo_actual]:

            nueva_distancia = distancias[nodo_actual] + peso

            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia

    return distancias


# Crear el grafo
grafo = {
    "A": [("B", 4), ("C", 2)],
    "B": [("A", 4), ("C", 1), ("D", 5)],
    "C": [("A", 2), ("B", 1), ("D", 8)],
    "D": [("B", 5), ("C", 8)]
}

# Ejecutar el algoritmo desde A
resultado = dijkstra(grafo, "A")

print("Distancias más cortas desde A:")

for nodo, distancia in resultado.items():
    print(nodo, ":", distancia)
