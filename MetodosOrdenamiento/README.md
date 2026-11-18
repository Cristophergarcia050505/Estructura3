# Ejercicios de métodos de ordenamiento en Python

Tres ejercicios para la materia de Estructuras de Datos. Los algoritmos se programaron manualmente, sin usar `sort()` ni `sorted()`.

## 1. Burbuja: calificaciones
- **Archivo:** `01_burbuja_calificaciones.py`
- **Objetivo:** ordenar calificaciones de mayor a menor.
- **Entrada:** `[85, 70, 95, 60, 90, 75]`
- **Salida:** `[95, 90, 85, 75, 70, 60]`
- **Cómo funciona:** compara parejas vecinas e intercambia las que están en orden incorrecto.

## 2. Inserción: libros
- **Archivo:** `02_insercion_libros.py`
- **Objetivo:** ordenar títulos alfabéticamente.
- **Entrada:** `["Redes", "Programacion", "Algoritmos", "Sistemas Operativos", "Bases de Datos"]`
- **Salida:** `["Algoritmos", "Bases de Datos", "Programacion", "Redes", "Sistemas Operativos"]`
- **Cómo funciona:** inserta cada título en la parte de la lista que ya está ordenada.

## 3. Selección: precios
- **Archivo:** `03_seleccion_precios.py`
- **Objetivo:** ordenar precios de menor a mayor.
- **Entrada:** `[350, 120, 299, 80, 450, 199]`
- **Salida:** `[80, 120, 199, 299, 350, 450]`
- **Cómo funciona:** encuentra el precio mínimo de la parte no ordenada y lo coloca al frente.

## Ejecución

Desde una terminal abierta en esta carpeta:

```bash
python 01_burbuja_calificaciones.py
python 02_insercion_libros.py
python 03_seleccion_precios.py
```

## Conclusión
Los tres métodos ordenan los datos, pero usan estrategias distintas. Burbuja compara elementos vecinos, Inserción agrega cada elemento en su lugar correcto y Selección busca el mínimo restante. Entender estas diferencias ayuda a aprender ciclos, comparaciones y manejo de listas en Python.
