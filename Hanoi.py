import time

# Funcion para resolver la Torre de Hanoi
def hanoi(n, origen, auxiliar, destino):
    if n == 1:
        return 1

    movimientos1 = hanoi(n - 1, origen, destino, auxiliar)
    movimientos2 = hanoi(n - 1, auxiliar, origen, destino)

    return movimientos1 + 1 + movimientos2


# Programa principal
discos_lista = [5, 10, 30, 64]

for discos in discos_lista:
    inicio = time.perf_counter()

    # Calcula la cantidad de movimientos necesarios
    movimientos = hanoi(discos, "A", "B", "C")

    fin = time.perf_counter()
    tiempo = fin - inicio

    print("---------------------------")
    print("Cantidad de discos:", discos)
    print("Movimientos necesarios:", movimientos)
    print("Tiempo de calculo:", tiempo, "segundos")
