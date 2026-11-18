"""Menú interactivo para elegir cuatro métodos de ordenamiento."""

from shellsort import shellsort
from quicksort import quicksort
from heapsort import heapsort
from radixsort import radixsort


def leer_entero(mensaje, minimo=None):
    while True:
        try:
            numero = int(input(mensaje))
            if minimo is not None and numero < minimo:
                print(f"Escribe un entero mayor o igual que {minimo}.")
                continue
            return numero
        except ValueError:
            print("Entrada inválida: escribe un número entero.")


def pedir_numeros():
    cantidad = leer_entero("¿Cuántos números quieres ordenar? ", minimo=1)
    numeros = []
    for i in range(cantidad):
        numeros.append(leer_entero(f"Número {i + 1}: "))
    return numeros


def main():
    metodos = {
        "1": ("ShellSort", shellsort),
        "2": ("QuickSort", quicksort),
        "3": ("HeapSort", heapsort),
        "4": ("RadixSort", radixsort),
    }

    while True:
        print("\n====== MÉTODOS DE ORDENAMIENTO ======")
        for clave, (nombre, _) in metodos.items():
            print(f"{clave}. {nombre}")
        print("5. Salir")

        opcion = input("Elige una opción (1-5): ").strip()
        if opcion == "5":
            print("Programa finalizado. ¡Hasta luego!")
            break
        if opcion not in metodos:
            print("Opción no válida. Intenta de nuevo.")
            continue

        numeros = pedir_numeros()
        nombre, funcion = metodos[opcion]
        print("\nMétodo elegido:", nombre)
        print("Números originales:", numeros)
        print("Números ordenados: ", funcion(numeros))
        print("Volviendo al menú principal...")


if __name__ == "__main__":
    main()
