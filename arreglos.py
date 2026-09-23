import random

# Cantidad de alumnos y materias
alumnos = 100000
materias = 100

# Crear la matriz
matriz = []

for alumno in range(alumnos):
    calificaciones = []

    for materia in range(materias):
        calificacion = random.randint(60, 100)
        calificaciones.append(calificacion)

    matriz.append(calificaciones)


# Mostrar los alumnos y sus calificaciones
print("ALUMNO   MATEMATICAS1   ESPAÑOL2   PROGRAMACION3     FINANZAS4   POO5   INGLES6")
print("-----------------------------------------------")

for i in range(alumnos):
    print(i + 1, "     ", matriz[i])


# Buscar al alumno  y materia 
alumno = 4524
materia = 98

print("\nRESULTADO DE LA BÚSQUEDA")
print("------------------------")
print("Alumno:", alumno)
print("Materia:", materia)
print("Calificación:", matriz[alumno - 1][materia - 1])