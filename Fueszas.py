import tkinter as tk
from tkinter import ttk, messagebox
import math


def calcular_paralelas():
    try:
        f1 = float(txt_f1.get())
        f2 = float(txt_f2.get())
        distancia = float(txt_distancia.get())

        if f1 <= 0 or f2 <= 0 or distancia <= 0:
            messagebox.showerror(
                "Error",
                "Las fuerzas y la distancia deben ser mayores que cero."
            )
            return

        sentido = combo_sentido.get()

        if sentido == "Mismo sentido":
            fr = f1 + f2

            ac = (f2 * distancia) / fr
            bc = (f1 * distancia) / fr

            resultado_fr = f"{fr:.2f} N"
            resultado_ac = f"{ac:.2f}"
            resultado_bc = f"{bc:.2f}"

        else:
            if f1 == f2:
                messagebox.showerror(
                    "Error",
                    "Si las fuerzas son iguales y tienen sentidos contrarios, "
                    "la resultante es cero."
                )
                return

            fr = abs(f1 - f2)
            ac = (f2 * distancia) / (f1 - f2)
            bc = ac - distancia
            ac_mostrar = abs(ac)
            bc_mostrar = abs(bc)

            resultado_fr = f"{fr:.2f} N"
            resultado_ac = f"{ac_mostrar:.2f}"
            resultado_bc = f"{bc_mostrar:.2f}"

        lbl_fr_paralela.config(text=resultado_fr)
        lbl_ac.config(text=resultado_ac)
        lbl_bc.config(text=resultado_bc)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Ingresa solamente valores numéricos."
        )


def crear_fuerzas():
    try:
        numero = int(txt_num_fuerzas.get())

        if numero <= 0:
            messagebox.showerror(
                "Error",
                "El número de fuerzas debe ser mayor que cero."
            )
            return

        for widget in frame_fuerzas.winfo_children():
            widget.destroy()

        encabezado1 = tk.Label(
            frame_fuerzas,
            text="Fuerza",
            font=("Arial", 11, "bold")
        )
        encabezado1.grid(row=0, column=0, padx=10, pady=5)

        encabezado2 = tk.Label(
            frame_fuerzas,
            text="Magnitud (N)",
            font=("Arial", 11, "bold")
        )
        encabezado2.grid(row=0, column=1, padx=10, pady=5)

        encabezado3 = tk.Label(
            frame_fuerzas,
            text="Dirección (°)",
            font=("Arial", 11, "bold")
        )
        encabezado3.grid(row=0, column=2, padx=10, pady=5)

        entradas.clear()

        for i in range(numero):
            tk.Label(
                frame_fuerzas,
                text=f"F{i + 1}"
            ).grid(row=i + 1, column=0, padx=10, pady=5)

            magnitud = tk.Entry(frame_fuerzas, width=15)
            magnitud.grid(row=i + 1, column=1, padx=10, pady=5)

            direccion = tk.Entry(frame_fuerzas, width=15)
            direccion.grid(row=i + 1, column=2, padx=10, pady=5)

            entradas.append((magnitud, direccion))

        btn_calcular_concurrentes.pack(pady=15)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Ingresa un número entero válido."
        )


def calcular_concurrentes():
    try:
        rx = 0
        ry = 0

        for magnitud, direccion in entradas:

            fuerza = float(magnitud.get())
            angulo = float(direccion.get())

            if fuerza < 0:
                messagebox.showerror(
                    "Error",
                    "La magnitud de una fuerza no puede ser negativa."
                )
                return

            radianes = math.radians(angulo)
            fx = fuerza * math.cos(radianes)
            fy = fuerza * math.sin(radianes)

            rx += fx
            ry += fy

        fr = math.sqrt(rx ** 2 + ry ** 2)

        if fr == 0:
            lbl_fr_concurrente.config(text="0.00 N")
            lbl_direccion.config(text="Indefinida")
            lbl_cuadrante.config(text="Sin sentido")
            return

        angulo_resultante = math.degrees(math.atan2(ry, rx))

        if angulo_resultante < 0:
            angulo_resultante += 360

        if rx > 0 and ry > 0:
            cuadrante = "I - (+X, +Y)"

        elif rx < 0 and ry > 0:
            cuadrante = "II - (-X, +Y)"

        elif rx < 0 and ry < 0:
            cuadrante = "III - (-X, -Y)"

        elif rx > 0 and ry < 0:
            cuadrante = "IV - (+X, -Y)"

        elif rx > 0 and ry == 0:
            cuadrante = "Sobre el eje +X"

        elif rx < 0 and ry == 0:
            cuadrante = "Sobre el eje -X"

        elif rx == 0 and ry > 0:
            cuadrante = "Sobre el eje +Y"

        else:
            cuadrante = "Sobre el eje -Y"

        lbl_fr_concurrente.config(
            text=f"{fr:.2f} N"
        )

        lbl_direccion.config(
            text=f"{angulo_resultante:.2f}°"
        )

        lbl_cuadrante.config(
            text=cuadrante
        )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Revisa que todas las casillas tengan valores numéricos."
        )

ventana = tk.Tk()
ventana.title("Cálculo de Fuerzas")
ventana.geometry("800x650")
ventana.resizable(False, False)

notebook = ttk.Notebook(ventana)
notebook.pack(fill="both", expand=True, padx=10, pady=10)


tab_paralelas = ttk.Frame(notebook)
notebook.add(tab_paralelas, text="Fuerzas Paralelas")

titulo1 = tk.Label(
    tab_paralelas,
    text="FUERZAS PARALELAS",
    font=("Arial", 20, "bold")
)
titulo1.pack(pady=20)


frame_paralelas = tk.Frame(tab_paralelas)
frame_paralelas.pack()


tk.Label(
    frame_paralelas,
    text="F1:"
).grid(row=0, column=0, padx=10, pady=10)

txt_f1 = tk.Entry(frame_paralelas, width=20)
txt_f1.grid(row=0, column=1, padx=10, pady=10)


tk.Label(
    frame_paralelas,
    text="F2:"
).grid(row=1, column=0, padx=10, pady=10)

txt_f2 = tk.Entry(frame_paralelas, width=20)
txt_f2.grid(row=1, column=1, padx=10, pady=10)


tk.Label(
    frame_paralelas,
    text="Distancia:"
).grid(row=2, column=0, padx=10, pady=10)

txt_distancia = tk.Entry(frame_paralelas, width=20)
txt_distancia.grid(row=2, column=1, padx=10, pady=10)


tk.Label(
    frame_paralelas,
    text="Sentido:"
).grid(row=3, column=0, padx=10, pady=10)

combo_sentido = ttk.Combobox(
    frame_paralelas,
    values=[
        "Mismo sentido",
        "Sentidos contrarios"
    ],
    state="readonly",
    width=18
)

combo_sentido.current(0)
combo_sentido.grid(row=3, column=1, padx=10, pady=10)


btn_calcular_paralelas = tk.Button(
    tab_paralelas,
    text="CALCULAR",
    command=calcular_paralelas,
    width=20
)
btn_calcular_paralelas.pack(pady=20)


frame_resultados1 = tk.LabelFrame(
    tab_paralelas,
    text="Salida",
    padx=20,
    pady=15
)

frame_resultados1.pack()


tk.Label(
    frame_resultados1,
    text="FR:"
).grid(row=0, column=0, padx=20, pady=8)

lbl_fr_paralela = tk.Label(
    frame_resultados1,
    text="---",
    font=("Arial", 12, "bold")
)
lbl_fr_paralela.grid(row=0, column=1)


tk.Label(
    frame_resultados1,
    text="AC:"
).grid(row=1, column=0, padx=20, pady=8)

lbl_ac = tk.Label(
    frame_resultados1,
    text="---",
    font=("Arial", 12, "bold")
)
lbl_ac.grid(row=1, column=1)


tk.Label(
    frame_resultados1,
    text="BC:"
).grid(row=2, column=0, padx=20, pady=8)

lbl_bc = tk.Label(
    frame_resultados1,
    text="---",
    font=("Arial", 12, "bold")
)
lbl_bc.grid(row=2, column=1)


tab_concurrentes = ttk.Frame(notebook)
notebook.add(tab_concurrentes, text="Fuerzas Concurrentes")


titulo2 = tk.Label(
    tab_concurrentes,
    text="FUERZAS CONCURRENTES",
    font=("Arial", 20, "bold")
)
titulo2.pack(pady=15)


frame_numero = tk.Frame(tab_concurrentes)
frame_numero.pack()


tk.Label(
    frame_numero,
    text="Número de fuerzas:"
).pack(side="left", padx=10)

txt_num_fuerzas = tk.Entry(
    frame_numero,
    width=10
)
txt_num_fuerzas.pack(side="left", padx=10)


btn_crear = tk.Button(
    frame_numero,
    text="Crear",
    command=crear_fuerzas
)
btn_crear.pack(side="left", padx=10)


frame_fuerzas = tk.Frame(tab_concurrentes)
frame_fuerzas.pack(pady=15)

entradas = []

btn_calcular_concurrentes = tk.Button(
    tab_concurrentes,
    text="CALCULAR RESULTANTE",
    command=calcular_concurrentes,
    width=25
)

frame_resultados2 = tk.LabelFrame(
    tab_concurrentes,
    text="Salida",
    padx=20,
    pady=10
)

frame_resultados2.pack(pady=10)


tk.Label(
    frame_resultados2,
    text="FR:"
).grid(row=0, column=0, padx=20, pady=5)

lbl_fr_concurrente = tk.Label(
    frame_resultados2,
    text="---",
    font=("Arial", 12, "bold")
)
lbl_fr_concurrente.grid(row=0, column=1)


tk.Label(
    frame_resultados2,
    text="Dirección:"
).grid(row=1, column=0, padx=20, pady=5)

lbl_direccion = tk.Label(
    frame_resultados2,
    text="---",
    font=("Arial", 12, "bold")
)
lbl_direccion.grid(row=1, column=1)


tk.Label(
    frame_resultados2,
    text="Cuadrante / Sentido:"
).grid(row=2, column=0, padx=20, pady=5)

lbl_cuadrante = tk.Label(
    frame_resultados2,
    text="---",
    font=("Arial", 12, "bold")
)
lbl_cuadrante.grid(row=2, column=1)


ventana.mainloop()