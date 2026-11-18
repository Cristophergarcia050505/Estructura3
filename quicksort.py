
# Método de ordenamiento QuickSort

def quicksort(numeros):
    if len(numeros) <= 1:
        return numeros

    # Elegimos el pivote
    pivote = numeros[len(numeros) // 2]

    # Dividimos los números en tres grupos
    menores = [x for x in numeros if x < pivote]
    iguales = [x for x in numeros if x == pivote]
    mayores = [x for x in numeros if x > pivote]

    # Ordenamos las partes
    return quicksort(menores) + iguales + quicksort(mayores)


# Programa principal
if __name__ == "__main__":

    cantidad = int(input("¿Cuántos números deseas ordenar? "))

    numeros = []

    for i in range(cantidad):
        numero = int(input(f"Ingresa el número {i + 1}: "))
        numeros.append(numero)

    print("Números originales:", numeros)

    ordenados = quicksort(numeros)

    print("Números ordenados:", ordenados)
