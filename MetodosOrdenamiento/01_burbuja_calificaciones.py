# Ejercicio 1: Ordenar calificaciones de mayor a menor con Burbuja.
# Se comparan calificaciones vecinas y se intercambian si es necesario.

def ordenar_burbuja(calificaciones):
    datos = calificaciones.copy()
    n = len(datos)

    for i in range(n - 1):
        hubo_intercambio = False
        for j in range(n - 1 - i):
            if datos[j] < datos[j + 1]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
                hubo_intercambio = True

        print(f"Pasada {i + 1}: {datos}")
        if not hubo_intercambio:
            break

    return datos


if __name__ == "__main__":
    calificaciones = [85, 70, 95, 60, 90, 75]
    print("Calificaciones originales:", calificaciones)
    resultado = ordenar_burbuja(calificaciones)
    print("Calificaciones ordenadas (mayor a menor):", resultado)
