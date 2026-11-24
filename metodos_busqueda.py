# Métodos de búsqueda en Python

# 1. Búsqueda secuencial
def busqueda_secuencial():
    alumnos = ["Carlos", "Ana", "Pedro", "Luis", "Maria"]

    print("\nLista de alumnos:", alumnos)
    nombre = input("Ingresa el nombre del alumno: ")

    for i in range(len(alumnos)):
        if alumnos[i].lower() == nombre.lower():
            print("Alumno encontrado en la posición:", i + 1)
            return

    print("Alumno no encontrado.")


# 2. Búsqueda binaria
def busqueda_binaria():
    numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    print("\nLista de números:", numeros)
    objetivo = int(input("Ingresa el número que deseas buscar: "))

    inicio = 0
    fin = len(numeros) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if numeros[medio] == objetivo:
            print("Número encontrado en la posición:", medio + 1)
            return

        elif numeros[medio] < objetivo:
            inicio = medio + 1

        else:
            fin = medio - 1

    print("Número no encontrado.")


# 3. Búsqueda Hash
def busqueda_hash():
    productos = {
        "101": "Computadora",
        "102": "Teclado",
        "103": "Mouse",
        "104": "Monitor",
        "105": "Audífonos"
    }

    print("\nProductos disponibles:")

    for codigo, producto in productos.items():
        print(codigo, "-", producto)

    clave = input("Ingresa el código del producto: ")

    if clave in productos:
        print("Producto encontrado:", productos[clave])
    else:
        print("Producto no encontrado.")


# Menú principal
while True:
    print("\n==============================")
    print("     MÉTODOS DE BÚSQUEDA")
    print("==============================")
    print("1. Búsqueda Secuencial")
    print("2. Búsqueda Binaria")
    print("3. Búsqueda Hash")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        busqueda_secuencial()

    elif opcion == "2":
        busqueda_binaria()

    elif opcion == "3":
        busqueda_hash()

    elif opcion == "4":
        print("Programa finalizado.")
        break

    else:
        print("Opción incorrecta.")