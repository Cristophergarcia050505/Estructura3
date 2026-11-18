"""Ordenamiento ShellSort: inserción con saltos decrecientes."""

def shellsort(numeros):
    datos = numeros.copy()
    salto = len(datos) // 2

    while salto > 0:
        for i in range(salto, len(datos)):
            actual = datos[i]
            j = i
            while j >= salto and datos[j - salto] > actual:
                datos[j] = datos[j - salto]
                j -= salto
            datos[j] = actual
        salto //= 2

    return datos


if __name__ == "__main__":
    ejemplo = [34, -7, 12, 0, 34, 5]
    print("Original:", ejemplo)
    print("ShellSort:", shellsort(ejemplo))
