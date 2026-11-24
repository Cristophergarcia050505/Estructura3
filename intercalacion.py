
# METODO DE INTERCALACION

def intercalar(lista1, lista2):
    resultado = []
    i = 0
    j = 0

    # Comparar los elementos de ambas listas
    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar los elementos restantes
    while i < len(lista1):
        resultado.append(lista1[i])
        i += 1

    while j < len(lista2):
        resultado.append(lista2[j])
        j += 1

    return resultado


# PROGRAMA PRINCIPAL

lista1 = [60, 70, 85, 95]
lista2 = [65, 75, 80, 100]

print("METODO DE INTERCALACION")
print("Lista 1:", lista1)
print("Lista 2:", lista2)

resultado = intercalar(lista1, lista2)

print("Lista intercalada:", resultado)
