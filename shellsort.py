
def shellsort(numeros):
    n = len(numeros)
    salto = n // 2

    while salto > 0:
        for i in range(salto, n):
            temporal = numeros[i]
            j = i

            while j >= salto and numeros[j - salto] > temporal:
                numeros[j] = numeros[j - salto]
                j -= salto

            numeros[j] = temporal

        salto //= 2

    return numeros


# Programa principal
cantidad = int(input("¿Cuántos números deseas ordenar? "))

numeros = []

for i in range(cantidad):
    numero = int(input(f"Ingresa el número {i + 1}: "))
    numeros.append(numero)

print("Números originales:", numeros)

shellsort(numeros)

print("Números ordenados:", numeros)
