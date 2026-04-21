"""
generador_graficos_S3.py
========================
Trigonometría Aplicada – Sesión 3: La Estrategia de la Doble Observación
IES Teis · 4º ESO · Decreto 156/2022 (Galicia)

Genera cuatro diagramas que ilustran cada ejercicio de la sesión 3.
Cada figura se guarda como PNG en la misma carpeta S3/.

Requisitos:
    pip install matplotlib numpy
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Arc

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

COLOR_STRUCT  = "#0056b3"
COLOR_ANGULO  = "#d9534f"
COLOR_SOLUCION = "#5cb85c"
COLOR_TIERRA  = "#8B6914"
COLOR_AGUA    = "#87CEEB"


def angulo_arc(ax, center, radius, theta1, theta2, color=COLOR_ANGULO, label=""):
    arc = Arc(center, 2*radius, 2*radius, angle=0,
              theta1=theta1, theta2=theta2, color=color, lw=1.5)
    ax.add_patch(arc)
    if label:
        mid = np.radians((theta1 + theta2) / 2)
        ax.text(center[0] + radius*1.45*np.cos(mid),
                center[1] + radius*1.45*np.sin(mid),
                label, color=color, fontsize=9, ha="center", va="center")


def angulo_recto(ax, vertex, size=0.3):
    sq = plt.Polygon([vertex,
                      (vertex[0]+size, vertex[1]),
                      (vertex[0]+size, vertex[1]+size),
                      (vertex[0],      vertex[1]+size)],
                     closed=True, fill=False, edgecolor="black", lw=1)
    ax.add_patch(sq)


# ═══════════════════════════════════════════════════════════
# EJERCICIO 1 – Puente de Rande (doble observación)
# ═══════════════════════════════════════════════════════════
def ejercicio_1():
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_aspect("equal")
    ax.axis("off")
    fig.patch.set_facecolor("#f8f9fa")

    # Escala: ÷ 10   x=170,8m → 17,08  h=98,5m → 9,85
    X = 17.08
    H = 9.85
    D = 10.0   # 100 m separación

    P1 = (0, 0)       # punto más cercano
    P2 = (-D, 0)      # punto más alejado
    BASE = (X, 0)     # base del pilar
    TOP  = (X, H)     # cima del pilar

    # Suelo
    ax.axhline(0, color=COLOR_TIERRA, lw=2)
    ax.fill_between([-D-1, X+2], -0.8, 0, color=COLOR_TIERRA, alpha=0.2)

    # Pilar
    ax.plot([BASE[0], TOP[0]], [BASE[1], TOP[1]], color=COLOR_STRUCT, lw=5,
            solid_capstyle="round", label="Pilar (h = ?)")
    ax.text(BASE[0]+0.4, H/2, r"$h \approx 98{,}5$ m",
            color=COLOR_SOLUCION, fontsize=9, va="center", fontweight="bold")

    # Líneas visuales
    ax.plot([P1[0], TOP[0]], [P1[1], TOP[1]], color=COLOR_ANGULO, lw=1.8,
            ls="-.", label="Visual 30°")
    ax.plot([P2[0], TOP[0]], [P2[1], TOP[1]], color="#e67e22", lw=1.8,
            ls="--", label="Visual 20°")

    # Distancia entre observadores
    ax.annotate("", xy=P1, xytext=P2,
                arrowprops=dict(arrowstyle="<->", color="gray", lw=1.5))
    ax.text(-D/2, -1.2, "100 m", ha="center", color="gray", fontsize=9)

    # x (incógnita intermedia)
    ax.annotate("", xy=BASE, xytext=P1,
                arrowprops=dict(arrowstyle="<->", color=COLOR_SOLUCION, lw=1.3))
    ax.text(X/2, -0.7, r"$x \approx 170{,}8$ m",
            ha="center", color=COLOR_SOLUCION, fontsize=9)

    # Ángulos
    angulo_arc(ax, P1, 3.5, 0,
               np.degrees(np.arctan(H/X)), COLOR_ANGULO, "30°")
    angulo_arc(ax, P2, 3.5, 0,
               np.degrees(np.arctan(H/(X+D))), "#e67e22", "20°")

    # Ángulo recto en la base
    angulo_recto(ax, BASE, size=0.5)

    ax.plot(*P1, "o", color=COLOR_ANGULO, ms=7, zorder=5)
    ax.plot(*P2, "o", color="#e67e22",   ms=7, zorder=5)
    ax.text(P1[0], 0.4, "Obs. 1", ha="center", fontsize=8, color=COLOR_ANGULO)
    ax.text(P2[0], 0.4, "Obs. 2", ha="center", fontsize=8, color="#e67e22")
    ax.plot(*TOP, "^", color=COLOR_STRUCT, ms=10, zorder=5)
    ax.text(TOP[0]+0.5, TOP[1]+0.3, "Cima\npilar", fontsize=8, color=COLOR_STRUCT)

    ax.set_xlim(-D-2, X+3)
    ax.set_ylim(-2, H+2)
    ax.set_title("Ejercicio 1 – Puente de Rande\nDoble observación → Sistema de ecuaciones",
                 fontsize=11, fontweight="bold", color=COLOR_STRUCT)
    ax.legend(loc="upper left", fontsize=9)

    plt.tight_layout()
    plt.savefig("S3_Ej1_Puente_Rande.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ Guardado: S3_Ej1_Puente_Rande.png")


# ═══════════════════════════════════════════════════════════
# EJERCICIO 2 – Monte del Castro
# ═══════════════════════════════════════════════════════════
def ejercicio_2():
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_aspect("equal")
    ax.axis("off")
    fig.patch.set_facecolor("#f8f9fa")

    # x=676,7m  h=315,3m  → ÷ 100 → x=6,77  h=3,15  d=5
    X = 6.767
    H = 3.153
    D = 5.0    # 500 m

    B1 = (0, 0)       # barco más cercano (después de navegar)
    B2 = (-D, 0)      # barco más lejano
    BASE = (X, 0)
    TOP  = (X, H)

    ax.fill_between([-D-1, X+2], -0.6, 0, color=COLOR_AGUA, alpha=0.4)
    ax.axhline(0, color=COLOR_AGUA, lw=1.5)
    ax.text(-D/2, -0.4, "Ría de Vigo", ha="center", color=COLOR_AGUA, fontsize=9)

    # Monte
    monte_x = [BASE[0]-0.5, BASE[0], BASE[0]+0.5]
    monte_y = [0, H, 0]
    ax.fill(monte_x, monte_y, color="#6aaa4b", alpha=0.6, zorder=3)
    ax.plot(monte_x + [monte_x[0]], monte_y + [monte_y[0]],
            color="#3a7a2a", lw=2, zorder=4)
    ax.text(BASE[0]+0.7, H/2, r"$h \approx 315{,}3$ m",
            color=COLOR_SOLUCION, fontsize=9, va="center", fontweight="bold")

    # Líneas visuales
    ax.plot([B1[0], TOP[0]], [0, TOP[1]], color=COLOR_ANGULO, lw=1.8, ls="-.",
            label="Visual 25°")
    ax.plot([B2[0], TOP[0]], [0, TOP[1]], color="#e67e22", lw=1.8, ls="--",
            label="Visual 15°")

    ax.annotate("", xy=B1, xytext=B2,
                arrowprops=dict(arrowstyle="<->", color="gray", lw=1.5))
    ax.text(-D/2, -0.9, "500 m navegados", ha="center", color="gray", fontsize=9)

    angulo_arc(ax, B1, 2.5, 0, np.degrees(np.arctan(H/X)), COLOR_ANGULO, "25°")
    angulo_arc(ax, B2, 2.5, 0, np.degrees(np.arctan(H/(X+D))), "#e67e22", "15°")

    ax.plot(*B1, "s", color=COLOR_ANGULO, ms=8, zorder=5)
    ax.text(B1[0], 0.25, "Barco 1", ha="center", fontsize=8, color=COLOR_ANGULO)
    ax.plot(*B2, "s", color="#e67e22", ms=8, zorder=5)
    ax.text(B2[0], 0.25, "Barco 2", ha="center", fontsize=8, color="#e67e22")

    angulo_recto(ax, BASE, size=0.3)

    ax.set_xlim(-D-1.5, X+2.5)
    ax.set_ylim(-1.5, H+1.5)
    ax.set_title("Ejercicio 2 – Monte del Castro desde la Ría de Vigo\nDoble observación desde el agua",
                 fontsize=11, fontweight="bold", color=COLOR_STRUCT)
    ax.legend(loc="upper left", fontsize=9)

    plt.tight_layout()
    plt.savefig("S3_Ej2_Monte_Castro.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ Guardado: S3_Ej2_Monte_Castro.png")


# ═══════════════════════════════════════════════════════════
# EJERCICIO 3 – Relación Fundamental (triángulo con sen=0,6)
# ═══════════════════════════════════════════════════════════
def ejercicio_3():
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect("equal")
    ax.axis("off")
    fig.patch.set_facecolor("#f8f9fa")

    # Triángulo 6-8-10 (sen=0.6, cos=0.8, tan=0.75)
    O = (0, 0)
    B = (8, 0)
    A = (8, 6)

    triangle = plt.Polygon([O, B, A], closed=True,
                            fill=True, facecolor="#e8f0fe", edgecolor=COLOR_STRUCT, lw=2.5)
    ax.add_patch(triangle)

    # Etiquetas de lados
    ax.text(4, -0.5, r"$\cos\alpha = 0{,}8$  →  adj = 8",
            ha="center", color=COLOR_STRUCT, fontsize=10)
    ax.text(8.3, 3, r"$\mathrm{op} = 6$", va="center", color=COLOR_ANGULO, fontsize=10)
    ax.text(3.5, 3.5, r"$\mathrm{hip} = 10$", ha="center", color=COLOR_SOLUCION,
            fontsize=10, rotation=36.87)

    # Ángulo recto en B
    angulo_recto(ax, B, size=0.4)

    # Ángulo α en O
    angulo_arc(ax, O, 2.0, 0, np.degrees(np.arctan(6/8)), COLOR_ANGULO,
               r"$\alpha$")

    # Valores
    ax.text(4, 7,
            r"$\sin\alpha = 0{,}6 \;\Rightarrow\; \cos\alpha = 0{,}8 \;\Rightarrow\; \tan\alpha = 0{,}75$",
            ha="center", color=COLOR_STRUCT, fontsize=11, fontweight="bold")

    # Relación Fundamental
    ax.text(4, -1.4,
            r"$\sin^2\alpha + \cos^2\alpha = 0{,}36 + 0{,}64 = 1\;\checkmark$",
            ha="center", color="#555", fontsize=10, style="italic")

    ax.set_xlim(-1.5, 11)
    ax.set_ylim(-2, 8.5)
    ax.set_title("Ejercicio 3 – Relación Fundamental de la Trigonometría\n"
                 r"$\sin\alpha = 0{,}6 \Rightarrow$ triángulo 6-8-10",
                 fontsize=11, fontweight="bold", color=COLOR_STRUCT)

    plt.tight_layout()
    plt.savefig("S3_Ej3_Relacion_Fundamental.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ Guardado: S3_Ej3_Relacion_Fundamental.png")


# ═══════════════════════════════════════════════════════════
# EJERCICIO 4 – Helicóptero en la playa de Samil
# ═══════════════════════════════════════════════════════════
def ejercicio_4():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_aspect("equal")
    ax.axis("off")
    fig.patch.set_facecolor("#f8f9fa")

    # h=1267,9m  x=1267,9m  → ÷500 → h=2,536  x=2,536  total=4
    TOTAL = 4.0    # 2000 m
    X1    = 2.536  # distancia desde Obs.1 al punto bajo el helicóptero
    H     = 2.536  # altura (igual a x por tan45°=1)

    OBS1 = (0, 0)
    OBS2 = (TOTAL, 0)
    HELI_GROUND = (X1, 0)
    HELI = (X1, H)

    # Playa
    ax.fill_between([-0.5, TOTAL+0.5], -0.4, 0, color="#f0d080", alpha=0.5)
    ax.axhline(0, color=COLOR_TIERRA, lw=2)
    ax.text(TOTAL/2, -0.6, "Playa de Samil  (2 km)", ha="center",
            color=COLOR_TIERRA, fontsize=9)

    # Helicóptero
    ax.plot(*HELI, "*", color=COLOR_ANGULO, ms=18, zorder=6, label="Helicóptero")
    ax.text(HELI[0]+0.15, HELI[1]+0.2, "Helicóptero", fontsize=9, color=COLOR_ANGULO)

    # Línea vertical
    ax.plot([HELI_GROUND[0], HELI[0]], [0, H], color="gray", lw=1.5, ls=":")
    ax.annotate("", xy=HELI, xytext=HELI_GROUND,
                arrowprops=dict(arrowstyle="<->", color=COLOR_SOLUCION, lw=1.5))
    ax.text(HELI[0]+0.15, H/2, r"$h \approx 1267{,}9$ m",
            color=COLOR_SOLUCION, fontsize=9, va="center", fontweight="bold")

    # Líneas visuales
    ax.plot([OBS1[0], HELI[0]], [0, H], color=COLOR_ANGULO, lw=2, ls="-.",
            label="Visual 45°")
    ax.plot([OBS2[0], HELI[0]], [0, H], color="#e67e22", lw=2, ls="--",
            label="Visual 60°")

    # Distancia total entre observadores
    ax.annotate("", xy=OBS2, xytext=OBS1,
                arrowprops=dict(arrowstyle="<->", color="gray", lw=1.5))
    ax.text(TOTAL/2, -1.0, "2 000 m", ha="center", color="gray", fontsize=9)

    # x e (2000-x)
    ax.annotate("", xy=HELI_GROUND, xytext=OBS1,
                arrowprops=dict(arrowstyle="<->", color=COLOR_ANGULO, lw=1.2))
    ax.text(X1/2, 0.25, r"$x \approx 1267{,}9$ m", ha="center",
            color=COLOR_ANGULO, fontsize=8)
    ax.annotate("", xy=OBS2, xytext=HELI_GROUND,
                arrowprops=dict(arrowstyle="<->", color="#e67e22", lw=1.2))
    ax.text((X1+TOTAL)/2, 0.25, r"$2000-x \approx 732$ m", ha="center",
            color="#e67e22", fontsize=8)

    angulo_arc(ax, OBS1, 1.0, 0, 45, COLOR_ANGULO, "45°")
    angulo_arc(ax, OBS2, 1.0, 90, 180 - np.degrees(np.arctan(H/(TOTAL-X1))),
               "#e67e22", "60°")

    ax.plot(*OBS1, "o", color=COLOR_ANGULO, ms=8, zorder=5)
    ax.text(OBS1[0], 0.35, "Obs. 1", ha="center", fontsize=8, color=COLOR_ANGULO)
    ax.plot(*OBS2, "o", color="#e67e22", ms=8, zorder=5)
    ax.text(OBS2[0], 0.35, "Obs. 2", ha="center", fontsize=8, color="#e67e22")

    angulo_recto(ax, HELI_GROUND, size=0.2)

    ax.set_xlim(-0.8, TOTAL+0.8)
    ax.set_ylim(-1.5, H+1)
    ax.set_title("Ejercicio 4 – Helicóptero de Salvamento en Samil\nDoble observación simétrica",
                 fontsize=11, fontweight="bold", color=COLOR_STRUCT)
    ax.legend(loc="upper right", fontsize=9)

    plt.tight_layout()
    plt.savefig("S3_Ej4_Helicoptero_Samil.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ Guardado: S3_Ej4_Helicoptero_Samil.png")


# ═══════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════
if __name__ == "__main__":
    import os
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    print("Generando gráficas de la Sesión 3 – Trigonometría Aplicada")
    print("=" * 60)

    ejercicio_1()
    ejercicio_2()
    ejercicio_3()
    ejercicio_4()

    print("\n✅ Todos los gráficos generados correctamente en S3/")
