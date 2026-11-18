"""HeapSort con montículo máximo (max-heap)."""

def heapsort(numeros):
    datos = numeros.copy()
    n = len(datos)

    def ajustar(raiz, limite):
        while True:
            mayor = raiz
            izquierdo = 2 * raiz + 1
            derecho = 2 * raiz + 2

            if izquierdo < limite and datos[izquierdo] > datos[mayor]:
                mayor = izquierdo
            if derecho < limite and datos[derecho] > datos[mayor]:
                mayor = derecho
            if mayor == raiz:
                break

            datos[raiz], datos[mayor] = datos[mayor], datos[raiz]
            raiz = mayor

    for i in range(n // 2 - 1, -1, -1):
        ajustar(i, n)

    for final in range(n - 1, 0, -1):
        datos[0], datos[final] = datos[final], datos[0]
        ajustar(0, final)

    return datos


if __name__ == "__main__":
    ejemplo = [34, -7, 12, 0, 34, 5]
    print("Original:", ejemplo)
    print("HeapSort:", heapsort(ejemplo))
