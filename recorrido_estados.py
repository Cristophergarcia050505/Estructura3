
import tkinter as tk
from tkinter import ttk, messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from itertools import permutations
import heapq

# =====================================
# 1. CREAR EL GRAFO
# =====================================

grafo = nx.Graph()

estados = [
    "Yucatan",
    "Campeche",
    "Tabasco",
    "Chiapas",
    "Oaxaca",
    "Puebla",
    "Veracruz"
]

grafo.add_nodes_from(estados)

conexiones = [
    ("Yucatan", "Campeche", 180),
    ("Campeche", "Tabasco", 350),
    ("Tabasco", "Chiapas", 250),
    ("Chiapas", "Oaxaca", 500),
    ("Oaxaca", "Puebla", 340),
    ("Puebla", "Veracruz", 280),
    ("Tabasco", "Veracruz", 420),
    ("Veracruz", "Oaxaca", 450)
]

grafo.add_weighted_edges_from(conexiones)

inicio = "Yucatan"


# =====================================
# 2. FUNCIONES DE LOS RECORRIDOS
# =====================================

def calcular_costo(ruta):

    total = 0

    for i in range(len(ruta) - 1):
        total += grafo[ruta[i]][ruta[i + 1]]["weight"]

    return total


def recorrido_sin_repetir():

    mejor_ruta = None
    menor_costo = float("inf")

    otros_estados = [e for e in estados if e != inicio]

    for orden in permutations(otros_estados):

        ruta = [inicio] + list(orden)

        valido = True

        for i in range(len(ruta) - 1):

            if not grafo.has_edge(ruta[i], ruta[i + 1]):
                valido = False
                break

        if valido:

            costo = calcular_costo(ruta)

            if costo < menor_costo:
                menor_costo = costo
                mejor_ruta = ruta

    return mejor_ruta, menor_costo


def recorrido_con_repeticion():

    posiciones = {
        estado: i for i, estado in enumerate(estados)
    }

    todos = (1 << len(estados)) - 1

    mascara_inicial = 1 << posiciones[inicio]

    pendientes = [
        (0, inicio, mascara_inicial, False, [inicio])
    ]

    visitados = set()

    while pendientes:

        costo, actual, mascara, repetido, ruta = heapq.heappop(
            pendientes
        )

        estado_busqueda = (actual, mascara, repetido)

        if estado_busqueda in visitados:
            continue

        visitados.add(estado_busqueda)

        if mascara == todos and repetido:
            return ruta, costo

        for vecino in grafo.neighbors(actual):

            nuevo_costo = grafo[actual][vecino]["weight"]

            nueva_mascara = mascara | (
                1 << posiciones[vecino]
            )

            ya_visitado = bool(
                mascara & (1 << posiciones[vecino])
            )

            nueva_repeticion = repetido or ya_visitado

            nueva_ruta = ruta + [vecino]

            heapq.heappush(
                pendientes,
                (
                    costo + nuevo_costo,
                    vecino,
                    nueva_mascara,
                    nueva_repeticion,
                    nueva_ruta
                )
            )

    return None, 0


# =====================================
# 3. FUNCIONES DE LA INTERFAZ
# =====================================

def limpiar_resultados():

    resultado.delete("1.0", tk.END)


def mostrar_relaciones():

    limpiar_resultados()

    resultado.insert(tk.END, "ESTADOS Y RELACIONES\n")
    resultado.insert(tk.END, "=" * 40 + "\n\n")

    for estado in grafo.nodes():

        resultado.insert(
            tk.END, estado + "\n"
        )

        for vecino in grafo.neighbors(estado):

            costo = grafo[estado][vecino]["weight"]

            resultado.insert(
                tk.END,
                "   -> " + vecino + " : " + str(costo) + " km\n"
            )

        resultado.insert(tk.END, "\n")


def mostrar_sin_repetir():

    limpiar_resultados()

    resultado.insert(
        tk.END, "RECORRIDO SIN REPETIR ESTADOS\n"
    )

    resultado.insert(tk.END, "=" * 40 + "\n\n")

    ruta, costo = recorrido_sin_repetir()

    if ruta:

        resultado.insert(
            tk.END,
            "Ruta encontrada:\n\n"
        )

        resultado.insert(
            tk.END,
            " -> ".join(ruta) + "\n\n"
        )

        resultado.insert(
            tk.END,
            "Estados visitados: 7\n"
        )

        resultado.insert(
            tk.END,
            "Estados repetidos: 0\n\n"
        )

        resultado.insert(
            tk.END,
            "COSTO TOTAL: " + str(costo) + " km\n"
        )

    else:

        resultado.insert(
            tk.END,
            "No existe un recorrido valido."
        )


def mostrar_con_repeticion():

    limpiar_resultados()

    resultado.insert(
        tk.END, "RECORRIDO CON REPETICION\n"
    )

    resultado.insert(tk.END, "=" * 40 + "\n\n")

    ruta, costo = recorrido_con_repeticion()

    if ruta:

        resultado.insert(
            tk.END,
            "Ruta encontrada:\n\n"
        )

        resultado.insert(
            tk.END,
            " -> ".join(ruta) + "\n\n"
        )

        resultado.insert(
            tk.END,
            "Estados diferentes visitados: 7\n"
        )

        resultado.insert(
            tk.END,
            "Cantidad de visitas: " + str(len(ruta)) + "\n\n"
        )

        resultado.insert(
            tk.END,
            "COSTO TOTAL: " + str(costo) + " km\n"
        )

    else:

        resultado.insert(
            tk.END,
            "No se encontro un recorrido valido."
        )


# =====================================
# 4. DIBUJAR EL GRAFO EN LA INTERFAZ
# =====================================

def dibujar_grafo():

    ax.clear()

    posiciones = nx.spring_layout(grafo, seed=10)

    nx.draw(
        grafo,
        posiciones,
        ax=ax,
        with_labels=True,
        node_color="lightblue",
        node_size=2000,
        font_size=9,
        font_weight="bold",
        edge_color="gray"
    )

    etiquetas = nx.get_edge_attributes(
        grafo, "weight"
    )

    nx.draw_networkx_edge_labels(
        grafo,
        posiciones,
        edge_labels=etiquetas,
        ax=ax,
        font_size=9
    )

    ax.set_title("Conexiones entre los 7 estados de Mexico")

    canvas.draw()


# =====================================
# 5. CREAR VENTANA PRINCIPAL
# =====================================

ventana = tk.Tk()

ventana.title("Sistema de Recorridos - Grafos")
ventana.geometry("1200x750")
ventana.configure(bg="#EAF0F6")


# =====================================
# 6. ENCABEZADO
# =====================================

encabezado = tk.Frame(
    ventana,
    bg="#17365D",
    height=90
)

encabezado.pack(fill="x")

titulo = tk.Label(
    encabezado,
    text="SISTEMA DE RECORRIDOS CON GRAFOS",
    font=("Arial", 21, "bold"),
    bg="#17365D",
    fg="white"
)

titulo.pack(pady=12)

subtitulo = tk.Label(
    encabezado,
    text="Recorrido de 7 estados de la Republica Mexicana",
    font=("Arial", 11),
    bg="#17365D",
    fg="white"
)

subtitulo.pack()


# =====================================
# 7. CONTENEDOR PRINCIPAL
# =====================================

principal = tk.Frame(
    ventana,
    bg="#EAF0F6"
)

principal.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=15
)


# =====================================
# 8. PANEL IZQUIERDO: BOTONES
# =====================================

panel_botones = tk.Frame(
    principal,
    bg="white",
    width=300
)

panel_botones.pack(
    side="left",
    fill="y",
    padx=10
)

panel_botones.pack_propagate(False)

tk.Label(
    panel_botones,
    text="MENU PRINCIPAL",
    font=("Arial", 16, "bold"),
    bg="white",
    fg="#17365D"
).pack(pady=20)


def crear_boton(texto, funcion, color):

    boton = tk.Button(
        panel_botones,
        text=texto,
        command=funcion,
        font=("Arial", 11, "bold"),
        bg=color,
        fg="white",
        activebackground=color,
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        height=2,
        width=27
    )

    boton.pack(pady=9)


crear_boton(
    "1. Mostrar estados y relaciones",
    mostrar_relaciones,
    "#2874A6"
)

crear_boton(
    "2. Recorrido sin repetir",
    mostrar_sin_repetir,
    "#229954"
)

crear_boton(
    "3. Recorrido con repeticion",
    mostrar_con_repeticion,
    "#8E44AD"
)

crear_boton(
    "4. Dibujar el grafo",
    dibujar_grafo,
    "#D68910"
)

crear_boton(
    "5. Limpiar resultados",
    limpiar_resultados,
    "#566573"
)

crear_boton(
    "6. Salir",
    ventana.destroy,
    "#C0392B"
)


# =====================================
# 9. PANEL CENTRAL: RESULTADOS
# =====================================

panel_resultados = tk.Frame(
    principal,
    bg="white"
)

panel_resultados.pack(
    side="left",
    fill="both",
    expand=True,
    padx=10
)

tk.Label(
    panel_resultados,
    text="RESULTADOS",
    font=("Arial", 15, "bold"),
    bg="white",
    fg="#17365D"
).pack(pady=15)

resultado = tk.Text(
    panel_resultados,
    font=("Consolas", 11),
    bg="#F4F6F7",
    fg="#17202A",
    wrap="word",
    padx=12,
    pady=12
)

resultado.pack(
    fill="both",
    expand=True,
    padx=12,
    pady=10
)


# =====================================
# 10. PANEL DERECHO: GRAFO
# =====================================

panel_grafo = tk.Frame(
    principal,
    bg="white",
    width=400
)

panel_grafo.pack(
    side="right",
    fill="both",
    padx=10
)

panel_grafo.pack_propagate(False)

tk.Label(
    panel_grafo,
    text="VISUALIZACION DEL GRAFO",
    font=("Arial", 13, "bold"),
    bg="white",
    fg="#17365D"
).pack(pady=15)

figura, ax = plt.subplots(figsize=(5, 5))

figura.tight_layout()

canvas = FigureCanvasTkAgg(
    figura,
    master=panel_grafo
)

canvas.get_tk_widget().pack(
    fill="both",
    expand=True,
    padx=5,
    pady=5
)

# Dibujar grafo al iniciar
dibujar_grafo()

# Mensaje inicial
resultado.insert(
    tk.END,
    "BIENVENIDO AL SISTEMA DE GRAFOS\n\n"
    "Este programa permite analizar las conexiones\n"
    "entre 7 estados de Mexico.\n\n"
    "Selecciona una opcion del menu izquierdo\n"
    "para comenzar.\n\n"
    "El estado inicial es: Yucatan.\n\n"
    "Los costos representan kilometros de traslado."
)


# =====================================
# 11. EJECUTAR PROGRAMA
# =====================================

ventana.mainloop()
