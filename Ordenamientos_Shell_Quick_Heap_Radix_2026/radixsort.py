"""RadixSort LSD base 10; admite enteros positivos, cero y negativos."""

def _radix_positivos(numeros):
    if not numeros:
        return []

    datos = numeros.copy()
    maximo = max(datos)
    posicion = 1

    while maximo // posicion > 0:
        conteo = [0] * 10
        salida = [0] * len(datos)

        for numero in datos:
            digito = (numero // posicion) % 10
            conteo[digito] += 1

        for i in range(1, 10):
            conteo[i] += conteo[i - 1]

        for i in range(len(datos) - 1, -1, -1):
            numero = datos[i]
            digito = (numero // posicion) % 10
            conteo[digito] -= 1
            salida[conteo[digito]] = numero

        datos = salida
        posicion *= 10

    return datos


def radixsort(numeros):
    negativos = [-n for n in numeros if n < 0]
    no_negativos = [n for n in numeros if n >= 0]

    # Los negativos de mayor valor absoluto van primero: -90 < -5.
    ordenados_negativos = [-n for n in reversed(_radix_positivos(negativos))]
    ordenados_positivos = _radix_positivos(no_negativos)
    return ordenados_negativos + ordenados_positivos


if __name__ == "__main__":
    ejemplo = [34, -7, 12, 0, 34, -51]
    print("Original:", ejemplo)
    print("RadixSort:", radixsort(ejemplo))
