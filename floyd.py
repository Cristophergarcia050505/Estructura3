
def floyd(matriz):

    n = len(matriz)

    # Revisar todos los nodos como posibles intermedios
    for k in range(n):

        for i in range(n):

            for j in range(n):

                nueva_distancia = matriz[i][k] + matriz[k][j]

                if nueva_distancia < matriz[i][j]:

                    matriz[i][j] = nueva_distancia

    return matriz


# INF representa que no existe una conexión directa
INF = float("inf")

# Crear matriz de distancias
grafo = [
    [0,   5,   INF, 10],
    [INF, 0,   3,   INF],
    [INF, INF, 0,   1],
    [INF, INF, INF, 0]
]

# Ejecutar algoritmo
resultado = floyd(grafo)

print("Matriz de distancias mínimas:")

for fila in resultado:
    print(fila)
