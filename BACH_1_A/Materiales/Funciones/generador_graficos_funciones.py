import os
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "imgs")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def guardar(nombre):
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, f"{nombre}.png"), dpi=140)
    plt.close()
    print(f"✓ Generado: imgs/{nombre}.png")


def sesion_1():
    x = np.linspace(0, 15, 300)
    y_lineal = 1.2 * x + 5
    y_cuad = -x**2 + 10*x - 21

    fig, ax = plt.subplots(figsize=(8, 4.8))
    ax.plot(x, y_lineal, label=r"$f(x)=1{,}2x+5$", color="#0056b3", lw=2.3)
    ax.plot(x, y_cuad, label=r"$B(x)=-x^2+10x-21$", color="#d9534f", lw=2.3)
    ax.scatter([5], [4], color="#d9534f", zorder=5)
    ax.annotate("Máximo (5, 4)", xy=(5, 4), xytext=(6.2, 6), fontsize=9,
                arrowprops=dict(arrowstyle="->", color="#444"))
    ax.set_title("Sesión 1 · Modelización lineal y cuadrática")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    guardar("s1_modelizacion_lineal_cuadratica")


def sesion_2():
    x = np.linspace(-1, 5, 300)
    y = x + 1

    fig, ax = plt.subplots(figsize=(8, 4.8))
    ax.plot(x, y, color="#0056b3", lw=2.3, label=r"$\frac{x^2-1}{x-1}=x+1$ (x≠1)")
    ax.scatter([1], [2], color="white", edgecolor="#0056b3", s=80, zorder=6)
    ax.annotate("Hueco en x=1", xy=(1, 2), xytext=(1.7, 3.3), fontsize=9,
                arrowprops=dict(arrowstyle="->", color="#444"))

    x2 = np.linspace(-1, 7, 300)
    y2 = x2**2 - 6*x2 + 8
    ax.plot(x2, y2, color="#d9534f", lw=2.1, alpha=0.9, label=r"$x^2-6x+8$")
    ax.scatter([3], [-1], color="#d9534f", zorder=6)

    ax.axvline(3, color="#888", ls="--", lw=1)
    ax.set_ylim(-4, 10)
    ax.set_title("Sesión 2 · Continuidad y monotonía")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(loc="upper left")
    guardar("s2_continuidad_monotonia")


def sesion_3():
    t = np.linspace(0, 10, 300)
    capital = 2000 * (1.03 ** t)

    x = np.linspace(3.05, 15, 300)
    logf = np.log(x - 3)

    fig, ax1 = plt.subplots(figsize=(8, 4.8))
    ax1.plot(t, capital, color="#0056b3", lw=2.3, label=r"$C(t)=2000(1{,}03)^t$")
    ax1.set_xlabel("t (años)")
    ax1.set_ylabel("Capital (€)", color="#0056b3")
    ax1.tick_params(axis='y', labelcolor="#0056b3")

    ax2 = ax1.twinx()
    ax2.plot(x, logf, color="#d9534f", lw=2.0, label=r"$\log(x-3)$")
    ax2.axvline(3, color="#d9534f", ls="--", lw=1)
    ax2.set_ylabel("Valor logarítmico", color="#d9534f")
    ax2.tick_params(axis='y', labelcolor="#d9534f")

    lines = ax1.get_lines() + ax2.get_lines()
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc="upper left")
    ax1.set_title("Sesión 3 · Exponencial y logarítmica")
    guardar("s3_exponencial_logaritmica")


def sesion_4():
    x1 = np.linspace(0, 100, 150)
    y1 = np.full_like(x1, 10.0)

    x2 = np.linspace(100, 180, 150)
    y2 = 10 + 0.15 * (x2 - 100)

    fig, ax = plt.subplots(figsize=(8, 4.8))
    ax.plot(x1, y1, color="#0056b3", lw=2.4, label="Hasta 100 kWh")
    ax.plot(x2, y2, color="#d9534f", lw=2.4, label="Tramo > 100 kWh")
    ax.scatter([100], [10], color="#222", zorder=6)
    ax.annotate("Punto de unión\n(continuidad)", xy=(100, 10), xytext=(115, 12.5), fontsize=9,
                arrowprops=dict(arrowstyle="->", color="#444"))

    ax.set_title("Sesión 4 · Función a trozos (tarifa eléctrica)")
    ax.set_xlabel("Consumo x (kWh)")
    ax.set_ylabel("Coste C(x) (€)")
    ax.legend()
    guardar("s4_funcion_trozos_tarifa")


if __name__ == "__main__":
    print("Generando gráficas de Relaciones Funcionales...")
    sesion_1()
    sesion_2()
    sesion_3()
    sesion_4()
    print("Proceso completado.")
