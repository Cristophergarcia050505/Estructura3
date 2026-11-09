
def warshall(matriz):

    n = len(matriz)

    # Revisar todos los nodos intermedios
    for k in range(n):

        for i in range(n):

            for j in range(n):

                if matriz[i][k] == 1 and matriz[k][j] == 1:

                    matriz[i][j] = 1

    return matriz


# Crear matriz de conexiones
grafo = [
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

# Ejecutar algoritmo
resultado = warshall(grafo)

print("Matriz de caminos:")

for fila in resultado:
    print(fila)
