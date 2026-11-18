
# Método de ordenamiento HeapSort

def heapify(numeros, n, i):
    mayor = i
    izquierda = 2 * i + 1
    derecha = 2 * i + 2

    # Comparar con el hijo izquierdo
    if izquierda < n and numeros[izquierda] > numeros[mayor]:
        mayor = izquierda

    # Comparar con el hijo derecho
    if derecha < n and numeros[derecha] > numeros[mayor]:
        mayor = derecha

    # Intercambiar si encontramos un número mayor
    if mayor != i:
        numeros[i], numeros[mayor] = numeros[mayor], numeros[i]
        heapify(numeros, n, mayor)


def heapsort(numeros):
    n = len(numeros)

    # Construir un montículo máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(numeros, n, i)

    # Extraer los números en orden
    for i in range(n - 1, 0, -1):
        numeros[0], numeros[i] = numeros[i], numeros[0]
        heapify(numeros, i, 0)

    return numeros


# Programa principal
if __name__ == "__main__":

    cantidad = int(input("¿Cuántos números deseas ordenar? "))

    numeros = []

    for i in range(cantidad):
        numero = int(input(f"Ingresa el número {i + 1}: "))
        numeros.append(numero)

    print("Números originales:", numeros)

    heapsort(numeros)

    print("Números ordenados:", numeros)
