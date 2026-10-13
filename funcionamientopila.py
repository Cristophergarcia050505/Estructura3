
import tkinter as tk
from tkinter import messagebox

# Crear la pila
pila = []

# Agregar un elemento
def agregar():
    elemento = entrada.get()

    if elemento != "":
        pila.append(elemento)
        entrada.delete(0, tk.END)
        dibujar_pila()
    else:
        messagebox.showwarning("Aviso", "Escribe un elemento")

# Eliminar el elemento de arriba
def eliminar():
    if len(pila) > 0:
        pila.pop()
        dibujar_pila()
    else:
        messagebox.showwarning("Aviso", "La pila está vacía")

# Dibujar la pila en pantalla
def dibujar_pila():
    lienzo.delete("all")

    lienzo.create_text(
        150, 20, text="TOPE DE LA PILA",
        font=("Arial", 12, "bold")
    )

    if len(pila) == 0:
        lienzo.create_text(
            150, 200, text="Pila vacía",
            font=("Arial", 14)
        )

    for i, elemento in enumerate(reversed(pila)):
        x1 = 70
        y1 = 50 + i * 45
        x2 = 230
        y2 = y1 + 40

        lienzo.create_rectangle(
            x1, y1, x2, y2,
            fill="lightblue", outline="black"
        )

        lienzo.create_text(
            150, y1 + 20, text=elemento,
            font=("Arial", 12, "bold")
        )

    estado.config(text=f"Elementos en la pila: {len(pila)}")


# Crear la ventana
ventana = tk.Tk()
ventana.title("Funcionamiento de una Pila")
ventana.geometry("400x480")
ventana.resizable(False, False)

titulo = tk.Label(
    ventana, text="PILA - ESTRUCTURA DE DATOS",
    font=("Arial", 14, "bold")
)
titulo.pack(pady=10)

entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack(pady=5)

boton_agregar = tk.Button(
    ventana, text="Agregar (PUSH)",
    command=agregar, bg="lightgreen"
)
boton_agregar.pack(pady=5)

boton_eliminar = tk.Button(
    ventana, text="Eliminar (POP)",
    command=eliminar, bg="salmon"
)
boton_eliminar.pack(pady=5)

lienzo = tk.Canvas(
    ventana, width=300, height=250,
    bg="white"
)
lienzo.pack(pady=5)

estado = tk.Label(
    ventana, text="Elementos en la pila: 0",
    font=("Arial", 11)
)
estado.pack(pady=5)

dibujar_pila()

ventana.mainloop()
