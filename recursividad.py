# Estructura de carpetas
carpeta_principal = {
    "nombre": "Documentos",
    "contenido": [
        {
            "nombre": "Tareas",
            "contenido": [
                "matematicas.pdf",
                "programacion.py",
                "historia.docx"
            ]
        },
        {
            "nombre": "Proyectos",
            "contenido": [
                {
                    "nombre": "Python",
                    "contenido": [
                        "programa.py",
                        "recursividad.py"
                    ]
                },
                {
                    "nombre": "Java",
                    "contenido": [
                        "juego.java",
                        "clases.java",
                        "Mods de minecraft"
                    ]
                }
            ]
        },
        "horario.png"
    ]
}


def buscar_archivo(carpeta, archivo_buscado, ruta=""):
    
    # Obtenemos el nombre de la carpeta
    nombre_carpeta = carpeta["nombre"]
    
    # Creamos la ruta actual
    ruta_actual = ruta + "/" + nombre_carpeta

    # Revisamos todo lo que contiene la carpeta
    for elemento in carpeta["contenido"]:

        # Si el elemento es otra carpeta
        if isinstance(elemento, dict):

            # Llamada recursiva
            resultado = buscar_archivo(
                elemento,
                archivo_buscado,
                ruta_actual
            )

            # Si encontramos el archivo
            if resultado:
                return resultado

        # Si el elemento es un archivo
        else:

            if elemento == archivo_buscado:
                return ruta_actual + "/" + elemento

    # Si no encontramos el archivo
    return None


# Pedimos al usuario el archivo que quiere buscar
archivo = input("¿Qué archivo quieres buscar?: ")

# Ejecutamos la función
resultado = buscar_archivo(carpeta_principal, archivo)

# Mostramos el resultado
if resultado:
    print("Archivo encontrado:")
    print(resultado)
else:
    print("El archivo no fue encontrado.")