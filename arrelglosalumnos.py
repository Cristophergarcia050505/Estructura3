import random


departamentos = ["Ropa", "Deportes", "Jugueteria"]

meses = [
    "Enero", "Febrero", "Marzo", "Abril",
    "Mayo", "Junio", "Julio", "Agosto",
    "Septiembre", "Octubre", "Noviembre", "Diciembre"
]


ventas = []

for departamento in range(3):
    ventas_mes = []

    for mes in range(12):
        venta = random.randint(1000, 10000)
        ventas_mes.append(venta)

    ventas.append(ventas_mes)


# Método para insertar una venta
def insertar(departamento, mes, venta):
    ventas[departamento][mes] = venta


# Método para buscar una venta
def buscar(departamento, mes):
    return ventas[departamento][mes]


# Método para eliminar una venta
def eliminar(departamento, mes):
    ventas[departamento][mes] = 0



print("VENTAS MENSUALES")
print("---------------------------------------------")

print("Departamento", end=" ")

for mes in meses:
    print(mes, end="       ")

print()

for i in range(3):
    print(departamentos[i], end="        ")

    for j in range(12):
        print(ventas[i][j], end="      ")

    print()


# INSERTAR UNA VENTA
insertar(0, 0, 15000)

print("\nDespués de insertar una venta:")
print("Ropa - Enero:", ventas[0][0])


# BUSCAR UNA VENTA
resultado = buscar(1, 5)

print("\nRESULTADO DE LA BÚSQUEDA")
print("------------------------")
print("Departamento: Deportes")
print("Mes: Junio")
print("Venta:", resultado)


# ELIMINAR UNA VENTA
eliminar(2, 3)

print("\nDespués de eliminar una venta:")
print("Jugueteria - Abril:", ventas[2][3])