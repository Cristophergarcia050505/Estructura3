
class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, dato):
        self.elementos.append(dato)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0


# Crear una cola para cada servicio
colas = {
    1: Cola(),
    2: Cola(),
    3: Cola()
}

# Contador de turnos para cada servicio
turnos = {
    1: 1,
    2: 1,
    3: 1
}

print("SISTEMA DE ATENCION - SEGUROS")
print("Servicios disponibles: 1, 2 y 3")
print("C1, C2, C3: registrar cliente")
print("A1, A2, A3: atender cliente")
print("X: salir del programa")

while True:
    comando = input("\nIngrese un comando: ").upper().strip()

    if comando == "X":
        print("Sistema cerrado.")
        break

    if len(comando) < 2:
        print("Comando no valido.")
        continue

    letra = comando[0]

    try:
        servicio = int(comando[1:])
    except ValueError:
        print("Comando no valido.")
        continue

    if servicio not in colas:
        print("El servicio no existe.")
        continue

    if letra == "C":
        numero = turnos[servicio]
        colas[servicio].encolar(numero)

        print("Cliente registrado.")
        print("Servicio:", servicio)
        print("Numero de atencion:", numero)

        turnos[servicio] += 1

    elif letra == "A":
        cliente = colas[servicio].desencolar()

        if cliente is None:
            print("No hay clientes en este servicio.")
        else:
            print("Atendiendo al cliente numero:", cliente)
            print("Servicio:", servicio)

    else:
        print("Comando no reconocido.")
