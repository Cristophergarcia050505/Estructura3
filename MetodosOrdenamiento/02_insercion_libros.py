# Ejercicio 2: Ordenar titulos de libros alfabeticamente con Insercion.
# Se toma cada titulo y se inserta entre los que ya estan ordenados.

def ordenar_insercion(libros):
    datos = libros.copy()

    for i in range(1, len(datos)):
        titulo_actual = datos[i]
        j = i - 1

        while j >= 0 and datos[j].casefold() > titulo_actual.casefold():
            datos[j + 1] = datos[j]
            j -= 1

        datos[j + 1] = titulo_actual
        print(f"Insercion {i}: {datos}")

    return datos


if __name__ == "__main__":
    libros = ["Redes", "Programacion", "Algoritmos", "Sistemas Operativos", "Bases de Datos"]
    print("Libros originales:", libros)
    resultado = ordenar_insercion(libros)
    print("Libros ordenados alfabeticamente:", resultado)
