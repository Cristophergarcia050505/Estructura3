
# METODO DE MEZCLA EQUILIBRADA

# Identificar secuencias ordenadas
def detectar_tramos(lista):
    if not lista:
        return []

    tramos = [[lista[0]]]

    for numero in lista[1:]:
        if numero >= tramos[-1][-1]:
            tramos[-1].append(numero)
        else:
            tramos.append([numero])

    return tramos


# Combinar dos secuencias ordenadas
def mezclar(lista1, lista2):
    resultado = []
    i = 0
    j = 0

    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])

    return resultado


# Leer las secuencias de un archivo
def leer_archivo(nombre):
    with open(nombre, "r") as archivo:
        return [
            list(map(int, linea.split(",")))
            for linea in archivo if linea.strip()
        ]


# Metodo de Mezcla Equilibrada
def mezcla_equilibrada(lista):
    tramos = detectar_tramos(lista)
    pasada = 1

    while len(tramos) > 1:

        # Distribuir las secuencias en dos archivos
        with open("auxiliar1.txt", "w") as archivo1, \
             open("auxiliar2.txt", "w") as archivo2:

            for i, tramo in enumerate(tramos):
                archivo = archivo1 if i % 2 == 0 else archivo2
                archivo.write(
                    ",".join(map(str, tramo)) + "\n"
                )

        # Leer los archivos auxiliares
        grupos1 = leer_archivo("auxiliar1.txt")
        grupos2 = leer_archivo("auxiliar2.txt")

        # Mezclar las secuencias
        tramos = []

        for i in range(len(grupos1)):
            if i < len(grupos2):
                nuevo = mezclar(grupos1[i], grupos2[i])
            else:
                nuevo = grupos1[i]

            tramos.append(nuevo)

        print("Pasada", pasada, ":", tramos)
        pasada += 1

    return tramos[0] if tramos else []


# PROGRAMA PRINCIPAL

numeros = [42, 18, 73, 25, 60, 10, 91, 35]

print("METODO DE MEZCLA EQUILIBRADA")
print("Numeros originales:", numeros)

resultado = mezcla_equilibrada(numeros)

print("Numeros ordenados:", resultado)