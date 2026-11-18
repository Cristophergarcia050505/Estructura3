# Ejercicio 3: Ordenar precios de menor a mayor con Seleccion.
# Se busca el menor precio restante y se coloca al inicio de la zona no ordenada.

def ordenar_seleccion(precios):
    datos = precios.copy()
    n = len(datos)

    for i in range(n - 1):
        posicion_minima = i

        for j in range(i + 1, n):
            if datos[j] < datos[posicion_minima]:
                posicion_minima = j

        if posicion_minima != i:
            datos[i], datos[posicion_minima] = datos[posicion_minima], datos[i]

        print(f"Seleccion {i + 1}: {datos}")

    return datos


if __name__ == "__main__":
    precios = [350, 120, 299, 80, 450, 199]
    print("Precios originales:", precios)
    resultado = ordenar_seleccion(precios)
    print("Precios ordenados (menor a mayor):", resultado)
