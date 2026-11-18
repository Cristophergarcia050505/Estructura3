
# Método de ordenamiento RadixSort

def radix_positivos(numeros):
    if not numeros:
        return []

    numeros = numeros.copy()
    maximo = max(numeros)
    posicion = 1

    while maximo // posicion > 0:
        grupos = [[] for i in range(10)]

        # Agrupar los números según sus dígitos
        for numero in numeros:
            digito = (numero // posicion) % 10
            grupos[digito].append(numero)

        # Unir los grupos en orden
        numeros = []

        for grupo in grupos:
            numeros.extend(grupo)

        posicion *= 10

    return numeros


def radixsort(numeros):
    # Separar números negativos y no negativos
    negativos = [-n for n in numeros if n < 0]
    positivos = [n for n in numeros if n >= 0]

    # Ordenar ambos grupos
    negativos = radix_positivos(negativos)
    positivos = radix_positivos(positivos)

    # Recuperar los números negativos en orden
    negativos = [-n for n in reversed(negativos)]

    return negativos + positivos


# Programa principal
if __name__ == "__main__":

    cantidad = int(input("¿Cuántos números deseas ordenar? "))

    numeros = []

    for i in range(cantidad):
        numero = int(input(f"Ingresa el número {i + 1}: "))
        numeros.append(numero)

    print("Números originales:", numeros)

    ordenados = radixsort(numeros)

    print("Números ordenados:", ordenados)