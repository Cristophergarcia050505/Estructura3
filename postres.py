
# Lista enlazada de ingredientes
class NodoIngrediente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None


# Lista enlazada de postres
class NodoPostre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ingredientes = None
        self.siguiente = None


class ListaPostres:
    def __init__(self):
        self.cabeza = None

    # Buscar un postre
    def buscar_postre(self, nombre):
        actual = self.cabeza

        while actual is not None:
            if actual.nombre.lower() == nombre.lower():
                return actual
            actual = actual.siguiente

        return None

    # Mostrar todos los postres
    def mostrar_postres(self):
        actual = self.cabeza

        if actual is None:
            print("No hay postres registrados.")
            return

        while actual is not None:
            print(actual.nombre)
            actual = actual.siguiente

    # Dar de alta un postre
    def alta_postre(self, nombre):
        if nombre.strip() == "":
            print("El nombre no puede estar vacío.")
            return

        if self.buscar_postre(nombre) is not None:
            print("El postre ya existe.")
            return

        nuevo = NodoPostre(nombre.strip())

        # Insertar en orden alfabético
        if (self.cabeza is None or
                nuevo.nombre.lower() < self.cabeza.nombre.lower()):
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
        else:
            actual = self.cabeza

            while (actual.siguiente is not None and
                   actual.siguiente.nombre.lower() < nuevo.nombre.lower()):
                actual = actual.siguiente

            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo

        print("Postre registrado correctamente.")

    # Agregar un ingrediente
    def agregar_ingrediente(self, postre, ingrediente):
        nodo = self.buscar_postre(postre)

        if nodo is None:
            print("El postre no existe.")
            return

        if ingrediente.strip() == "":
            print("El ingrediente no puede estar vacío.")
            return

        actual = nodo.ingredientes

        while actual is not None:
            if actual.nombre.lower() == ingrediente.lower():
                print("El ingrediente ya existe.")
                return
            actual = actual.siguiente

        nuevo = NodoIngrediente(ingrediente.strip())
        nuevo.siguiente = nodo.ingredientes
        nodo.ingredientes = nuevo

        print("Ingrediente agregado correctamente.")

    # Mostrar los ingredientes de un postre
    def mostrar_ingredientes(self, postre):
        nodo = self.buscar_postre(postre)

        if nodo is None:
            print("El postre no existe.")
            return

        print("Ingredientes de", nodo.nombre + ":")

        actual = nodo.ingredientes

        if actual is None:
            print("Este postre no tiene ingredientes registrados.")
            return

        while actual is not None:
            print("-", actual.nombre)
            actual = actual.siguiente

    # Eliminar un ingrediente
    def eliminar_ingrediente(self, postre, ingrediente):
        nodo = self.buscar_postre(postre)

        if nodo is None:
            print("El postre no existe.")
            return

        actual = nodo.ingredientes
        anterior = None

        while actual is not None:
            if actual.nombre.lower() == ingrediente.lower():
                if anterior is None:
                    nodo.ingredientes = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente

                print("Ingrediente eliminado.")
                return

            anterior = actual
            actual = actual.siguiente

        print("El ingrediente no existe.")

    # Dar de baja un postre con sus ingredientes
    def baja_postre(self, nombre):
        actual = self.cabeza
        anterior = None

        while actual is not None:
            if actual.nombre.lower() == nombre.lower():
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente

                actual.ingredientes = None
                actual.siguiente = None

                print("Postre eliminado con sus ingredientes.")
                return

            anterior = actual
            actual = actual.siguiente

        print("El postre no existe.")

    # Cargar datos, incluso repetidos, para realizar pruebas
    def cargar_postre_prueba(self, nombre, ingredientes):
        nuevo = NodoPostre(nombre)
        anterior = None
        actual = self.cabeza

        while (actual is not None and
               actual.nombre.lower() <= nombre.lower()):
            anterior = actual
            actual = actual.siguiente

        nuevo.siguiente = actual

        if anterior is None:
            self.cabeza = nuevo
        else:
            anterior.siguiente = nuevo

        for ingrediente in ingredientes:
            nodo = NodoIngrediente(ingrediente)
            nodo.siguiente = nuevo.ingredientes
            nuevo.ingredientes = nodo

    # Eliminar automáticamente postres repetidos
    def eliminar_repetidos(self):
        actual = self.cabeza

        while actual is not None:
            anterior = actual
            repetido = actual.siguiente

            while repetido is not None:
                if repetido.nombre.lower() == actual.nombre.lower():
                    anterior.siguiente = repetido.siguiente
                    repetido.ingredientes = None
                    repetido.siguiente = None
                    repetido = anterior.siguiente
                else:
                    anterior = repetido
                    repetido = repetido.siguiente

            actual = actual.siguiente

        print("Se eliminaron los postres repetidos.")


# Programa principal
postres = ListaPostres()

while True:
    print("\n--- MENÚ DE POSTRES ---")
    print("1. Mostrar postres")
    print("2. Mostrar ingredientes")
    print("3. Agregar ingrediente")
    print("4. Eliminar ingrediente")
    print("5. Dar de alta un postre")
    print("6. Dar de baja un postre")
    print("7. Eliminar postres repetidos")
    print("8. Cargar datos de prueba")
    print("0. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        postres.mostrar_postres()

    elif opcion == "2":
        nombre = input("Nombre del postre: ")
        postres.mostrar_ingredientes(nombre)

    elif opcion == "3":
        nombre = input("Nombre del postre: ")
        ingrediente = input("Nuevo ingrediente: ")
        postres.agregar_ingrediente(nombre, ingrediente)

    elif opcion == "4":
        nombre = input("Nombre del postre: ")
        ingrediente = input("Ingrediente a eliminar: ")
        postres.eliminar_ingrediente(nombre, ingrediente)

    elif opcion == "5":
        nombre = input("Nombre del nuevo postre: ")
        postres.alta_postre(nombre)

    elif opcion == "6":
        nombre = input("Nombre del postre a eliminar: ")
        postres.baja_postre(nombre)

    elif opcion == "7":
        postres.eliminar_repetidos()

    elif opcion == "8":
        postres.cargar_postre_prueba(
            "Pastel", ["Harina", "Huevo", "Azúcar"])
        postres.cargar_postre_prueba(
            "Gelatina", ["Agua", "Grenetina"])
        postres.cargar_postre_prueba(
            "Pastel", ["Chocolate", "Leche"])
        print("Datos de prueba cargados.")

    elif opcion == "0":
        print("Programa terminado.")
        break

    else:
        print("Opción incorrecta.")

