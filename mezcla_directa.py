
# METODO DE MEZCLA DIRECTA

def mezclar(lista, inicio, medio, fin):
    izquierda = lista[inicio:medio]
    derecha = lista[medio:fin]

    i = 0
    j = 0
    k = inicio

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            lista[k] = izquierda[i]
            i += 1
        else:
            lista[k] = derecha[j]
            j += 1
        k += 1

    while i < len(izquierda):
        lista[k] = izquierda[i]
        i += 1
        k += 1

    while j < len(derecha):
        lista[k] = derecha[j]
        j += 1
        k += 1


def mezcla_directa(lista):
    tamaño = 1
    n = len(lista)

    while tamaño < n:
        for inicio in range(0, n, 2 * tamaño):
            medio = min(inicio + tamaño, n)
            fin = min(inicio + 2 * tamaño, n)

            mezclar(lista, inicio, medio, fin)

        tamaño *= 2

    return lista


# PROGRAMA PRINCIPAL

precios = [450, 120, 780, 230, 90, 560, 310, 150]

print("METODO DE MEZCLA DIRECTA")
print("Precios originales:", precios)

mezcla_directa(precios)

print("Precios ordenados:", precios)