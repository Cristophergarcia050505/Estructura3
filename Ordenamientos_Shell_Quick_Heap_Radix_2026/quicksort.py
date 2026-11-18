"""QuickSort con pivote central y partición de dos índices."""

def quicksort(numeros):
    datos = numeros.copy()

    def ordenar(inicio, fin):
        izquierda, derecha = inicio, fin
        pivote = datos[(inicio + fin) // 2]

        while izquierda <= derecha:
            while datos[izquierda] < pivote:
                izquierda += 1
            while datos[derecha] > pivote:
                derecha -= 1
            if izquierda <= derecha:
                datos[izquierda], datos[derecha] = datos[derecha], datos[izquierda]
                izquierda += 1
                derecha -= 1

        if inicio < derecha:
            ordenar(inicio, derecha)
        if izquierda < fin:
            ordenar(izquierda, fin)

    if datos:
        ordenar(0, len(datos) - 1)
    return datos


if __name__ == "__main__":
    ejemplo = [34, -7, 12, 0, 34, 5]
    print("Original:", ejemplo)
    print("QuickSort:", quicksort(ejemplo))
