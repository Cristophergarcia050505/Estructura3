# Práctica: métodos de ordenamiento en Python

Este proyecto implementa **ShellSort**, **QuickSort**, **HeapSort** y **RadixSort**. Cada método tiene su archivo y `main.py` permite elegir cualquiera desde un menú.

## Ejecución

1. Descargar Python 3.
2. Mantener todos los archivos `.py` en la misma carpeta.
3. Abrir una terminal en esa carpeta y ejecutar:

```bash
python main.py
```

4. Elegir 1 a 4, ingresar la cantidad de números y luego cada entero. Elegir **5** para salir.

El programa permite **enteros negativos, cero y repetidos** y vuelve al menú tras mostrar los resultados.

## Archivos

- `shellsort.py`: inserción con saltos decrecientes.
- `quicksort.py`: particiones alrededor de un pivote.
- `heapsort.py`: montículo máximo.
- `radixsort.py`: distribución estable por dígitos, incluidos negativos.
- `main.py`: menú e interacción con el usuario.

Ejemplo: `[34, -7, 12, 0, 34, -51]` -> `[-51, -7, 0, 12, 34, 34]`.

Cada algoritmo también se puede probar por separado con `python nombre_de_archivo.py`.
