"""
generador_graficos_S4.py
========================
Trigonometría Aplicada – Sesión 4: El Desafío Final – Geometría y Entorno
IES Teis · 4º ESO · Decreto 156/2022 (Galicia)

Genera cuatro diagramas que ilustran cada ejercicio de la sesión 4.
Cada figura se guarda como PNG en la misma carpeta S4/.

Requisitos:
    pip install matplotlib numpy
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, FancyArrowPatch

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

COLOR_STRUCT   = "#0056b3"
COLOR_ANGULO   = "#d9534f"
COLOR_SOLUCION = "#5cb85c"
COLOR_TIERRA   = "#8B6914"
COLOR_GOLD     = "#f0c040"


def angulo_arc(ax, center, radius, theta1, theta2, color=COLOR_ANGULO, label=""):
    arc = Arc(center, 2*radius, 2*radius, angle=0,
              theta1=theta1, theta2=theta2, color=color, lw=1.5)
    ax.add_patch(arc)
    if label:
        mid = np.radians((theta1 + theta2) / 2)
        ax.text(center[0] + radius*1.5*np.cos(mid),
                center[1] + radius*1.5*np.sin(mid),
                label, color=color, fontsize=9, ha="center", va="center")


def angulo_recto(ax, vertex, size=0.3):
    sq = plt.Polygon([vertex,
                      (vertex[0]+size, vertex[1]),
                      (vertex[0]+size, vertex[1]+size),
                      (vertex[0],      vertex[1]+size)],
                     closed=True, fill=False, edgecolor="black", lw=1)
    ax.add_patch(sq)


# ═══════════════════════════════════════════════════════════
# EJERCICIO 1 – La Gran Noria de Vigo
# ═══════════════════════════════════════════════════════════
def ejercicio_1():
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_aspect("equal")
    ax.axis("off")
    fig.patch.set_facecolor("#f8f9fa")

    R = 5
    N = 32
    angles = np.linspace(0, 2*np.pi, N, endpoint=False)
    xs = R * np.cos(angles)
    ys = R * np.sin(angles)

    # Círculo principal
    circle = plt.Circle((0, 0), R, fill=False, edgecolor=COLOR_STRUCT,
                         lw=2, linestyle="--", alpha=0.5)
    ax.add_patch(circle)

    # Góndolas
    ax.scatter(xs, ys, s=40, color=COLOR_ANGULO, zorder=5)

    # Resaltar un lado (L entre góndola 0 y 1)
    ax.plot([xs[0], xs[1]], [ys[0], ys[1]], color=COLOR_SOLUCION, lw=3,
            zorder=6, label=r"$L \approx 6{,}07$ m")
    mid_x = (xs[0]+xs[1])/2
    mid_y = (ys[0]+ys[1])/2
    ax.text(mid_x*1.25, mid_y*1.25, r"$L \approx 6{,}07$ m",
            color=COLOR_SOLUCION, fontsize=9.5, fontweight="bold", ha="center")

    # Radios al par resaltado
    ax.plot([0, xs[0]], [0, ys[0]], color=COLOR_STRUCT, lw=1.5, ls="-.")
    ax.plot([0, xs[1]], [0, ys[1]], color=COLOR_STRUCT, lw=1.5, ls="-.")
    ax.text(xs[0]*0.5 - 0.4, ys[0]*0.5 + 0.1, "r = 31 m",
            color=COLOR_STRUCT, fontsize=9)

    # Centro
    ax.plot(0, 0, "o", color=COLOR_STRUCT, ms=8, zorder=6)

    # Ángulo central
    angulo_arc(ax, (0, 0), 1.5, np.degrees(angles[0]), np.degrees(angles[1]),
               COLOR_ANGULO, r"$11{,}25°$")

    # Bisectriz (triángulo rectángulo mitad)
    mid_angle = (angles[0] + angles[1]) / 2
    bx, by = R * np.cos(mid_angle), R * np.sin(mid_angle)
    ax.plot([0, bx], [0, by], color=COLOR_ANGULO, lw=1.5, ls=":",
            label="Bisectriz (5,625°)")
    angulo_arc(ax, (0, 0), 2.5, np.degrees(angles[0]), np.degrees(mid_angle),
               "#e67e22", r"$5{,}625°$")

    ax.set_xlim(-R-1.5, R+1.5)
    ax.set_ylim(-R-1.5, R+2)
    ax.set_title("Ejercicio 1 – La Gran Noria de Vigo (r = 31 m, 32 góndolas)\n"
                 r"$L = 2r \cdot \sin(180°/32) \approx 6{,}07$ m",
                 fontsize=11, fontweight="bold", color=COLOR_STRUCT)
    ax.legend(loc="lower right", fontsize=9)

    plt.tight_layout()
    plt.savefig("S4_Ej1_Noria_Vigo.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ Guardado: S4_Ej1_Noria_Vigo.png")


# ═══════════════════════════════════════════════════════════
# EJERCICIO 2 – Cables de Navidad
# ═══════════════════════════════════════════════════════════
def ejercicio_2():
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_aspect("equal")
    ax.axis("off")
    fig.patch.set_facecolor("#f8f9fa")

    H = 10.0   # altura del poste (metros)
    angulos = [30, 45, 60]
    colores  = [COLOR_ANGULO, "#e67e22", COLOR_SOLUCION]
    longitudes = [H / np.sin(np.radians(a)) for a in angulos]

    # Suelo
    ax.axhline(0, color=COLOR_TIERRA, lw=2)
    ax.fill_between([-22, 2], -0.8, 0, color=COLOR_TIERRA, alpha=0.2)

    # Poste
    ax.plot([0, 0], [0, H], color=COLOR_STRUCT, lw=6, solid_capstyle="round",
            label="Poste (10 m)")
    ax.text(0.4, H/2, "10 m", color=COLOR_STRUCT, fontsize=10,
            va="center")

    # Cables
    for i, (ang, col, L) in enumerate(zip(angulos, colores, longitudes)):
        # punto anclaje en suelo
        d = H / np.tan(np.radians(ang))
        xa = -d
        ax.plot([0, xa], [H, 0], color=col, lw=2.5, ls="-.",
                label=f"Cable {ang}° → {L:.2f} m")
        ax.plot(xa, 0, "^", color=col, ms=10, zorder=5)
        ax.text(xa, -1.1 - i*0.8, f"Anclaje {ang}°\n{L:.2f} m",
                ha="center", color=col, fontsize=8.5)
        angulo_arc(ax, (xa, 0), 2.5, 90 - ang + 90, 180, col,
                   f"{ang}°")

    angulo_recto(ax, (0, 0), size=0.7)
    ax.plot(0, H, "o", color=COLOR_STRUCT, ms=10, zorder=6)
    ax.text(0.5, H+0.3, "Punto\nde salida", fontsize=8, color=COLOR_STRUCT)

    # Total
    total = sum(longitudes)
    ax.text(-10, H + 1.5,
            f"Total cable = {longitudes[0]:.2f} + {longitudes[1]:.2f} + {longitudes[2]:.2f} = {total:.2f} m",
            ha="center", color=COLOR_STRUCT, fontsize=10, fontweight="bold")

    ax.set_xlim(-22, 3)
    ax.set_ylim(-4.5, H+3)
    ax.set_title("Ejercicio 2 – Cables de figuras luminosas de Navidad\n"
                 r"$L = h / \sin(\alpha)$",
                 fontsize=11, fontweight="bold", color=COLOR_STRUCT)
    ax.legend(loc="lower right", fontsize=8.5)

    plt.tight_layout()
    plt.savefig("S4_Ej2_Cables_Navidad.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ Guardado: S4_Ej2_Cables_Navidad.png")


# ═══════════════════════════════════════════════════════════
# EJERCICIO 3 – Parcela triangular IFEVI
# ═══════════════════════════════════════════════════════════
def ejercicio_3():
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_aspect("equal")
    ax.axis("off")
    fig.patch.set_facecolor("#f8f9fa")

    # ÷ 30: a=4, b=5, gamma=40°
    a = 4.0   # 120m
    b = 5.0   # 150m
    gamma = 40

    A = (0, 0)
    B = (b, 0)
    C = (a * np.cos(np.radians(gamma)), a * np.sin(np.radians(gamma)))

    # Triángulo relleno
    triangle = plt.Polygon([A, B, C], closed=True,
                            facecolor="#d4edda", edgecolor=COLOR_STRUCT, lw=2.5)
    ax.add_patch(triangle)

    # Altura desde C a AB
    H_val = a * np.sin(np.radians(gamma))
    foot = (C[0], 0)

    ax.plot([C[0], foot[0]], [C[1], foot[1]], color=COLOR_ANGULO, lw=2, ls="--",
            label=f"h = {H_val*30:.2f} m")
    angulo_recto(ax, foot, size=0.2)
    ax.text(C[0]+0.15, H_val/2,
            f"h = {H_val*30:.1f} m", color=COLOR_ANGULO,
            fontsize=9.5, va="center", fontweight="bold")

    # Etiquetas de lados
    ax.text(b/2, -0.35, f"b = 150 m", ha="center", color=COLOR_STRUCT, fontsize=10)
    ax.text(C[0]/2 - 0.45, C[1]/2 + 0.1,
            f"a = 120 m", color=COLOR_STRUCT, fontsize=10, rotation=gamma)

    # Ángulo γ en A
    angulo_arc(ax, A, 1.2, 0, gamma, COLOR_ANGULO, r"$40°$")

    # Área
    area = 0.5 * b * H_val * 30 * 30   # desescalar: ×30 cada dim → ×900
    ax.text((A[0]+B[0]+C[0])/3, (A[1]+B[1]+C[1])/3 - 0.2,
            f"Área ≈ 5784,75 m²",
            ha="center", color=COLOR_SOLUCION, fontsize=11, fontweight="bold")

    ax.set_xlim(-0.8, b+0.8)
    ax.set_ylim(-0.8, H_val+1)
    ax.set_title("Ejercicio 3 – Parcela triangular en el IFEVI\n"
                 r"Área $= \frac{1}{2} \cdot b \cdot h = \frac{1}{2} \cdot 150 \cdot 77{,}13 \approx 5784{,}75$ m²",
                 fontsize=11, fontweight="bold", color=COLOR_STRUCT)
    ax.legend(loc="upper right", fontsize=9)

    plt.tight_layout()
    plt.savefig("S4_Ej3_Parcela_IFEVI.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ Guardado: S4_Ej3_Parcela_IFEVI.png")


# ═══════════════════════════════════════════════════════════
# EJERCICIO 4 – Distancia entre boyas (Paseo de Alfonso XII)
# ═══════════════════════════════════════════════════════════
def ejercicio_4():
    fig, ax = plt.subplots(figsize=(9, 7))
    ax.set_aspect("equal")
    ax.axis("off")
    fig.patch.set_facecolor("#f8f9fa")

    # Escalado ÷ 100
    OA = 4.0    # 400 m
    OB = 6.0    # 600 m
    GAMMA = 35  # grados

    O = (0, 0)
    A = (OA * np.cos(np.radians(GAMMA)), OA * np.sin(np.radians(GAMMA)))
    B = (OB, 0)

    # Mar
    ax.fill_between([-0.5, OB+0.5], -0.3, max(A[1]+0.5, 0.5),
                    color=COLOR_TIERRA.replace("8B6914", "87CEEB"), alpha=0.0)
    ax.fill_between([-0.5, OB+1], -0.3, 0.1, color="#87CEEB", alpha=0.35)
    ax.axhline(0, color="#87CEEB", lw=1.5, alpha=0.7)

    # Triángulo OAB
    triangle = plt.Polygon([O, A, B], closed=True,
                            facecolor="#e8f4fd", edgecolor=COLOR_STRUCT, lw=2)
    ax.add_patch(triangle)

    # Altura desde A a OB
    h_val = OA * np.sin(np.radians(GAMMA))   # 2.294
    base1  = OA * np.cos(np.radians(GAMMA))  # 3.276
    base2  = OB - base1                       # 2.724
    foot  = (base1, 0)

    ax.plot([A[0], foot[0]], [A[1], foot[1]], color=COLOR_ANGULO, lw=2,
            ls="--", label=f"h = {h_val*100:.1f} m")
    angulo_recto(ax, foot, size=0.2)
    ax.text(A[0]+0.15, A[1]/2, f"h = {h_val*100:.1f} m",
            color=COLOR_ANGULO, fontsize=9, va="center", fontweight="bold")

    # Proyecciones
    ax.annotate("", xy=foot, xytext=O,
                arrowprops=dict(arrowstyle="<->", color="#e67e22", lw=1.3))
    ax.text(base1/2, -0.35, f"base₁ = {base1*100:.1f} m",
            ha="center", color="#e67e22", fontsize=8.5)
    ax.annotate("", xy=B, xytext=foot,
                arrowprops=dict(arrowstyle="<->", color="#9b59b6", lw=1.3))
    ax.text(base1 + base2/2, -0.35, f"base₂ = {base2*100:.1f} m",
            ha="center", color="#9b59b6", fontsize=8.5)

    # Distancia AB
    AB = np.sqrt(h_val**2 + base2**2)
    ax.plot([A[0], B[0]], [A[1], B[1]], color=COLOR_SOLUCION, lw=3, zorder=6,
            label=f"AB ≈ {AB*100:.1f} m")
    ax.text((A[0]+B[0])/2 + 0.2, (A[1]+B[1])/2 + 0.15,
            f"AB ≈ {AB*100:.1f} m",
            color=COLOR_SOLUCION, fontsize=10, fontweight="bold")

    # Puntos
    ax.plot(*O, "o", color=COLOR_STRUCT, ms=10, zorder=7)
    ax.text(-0.15, 0.25, "Topógrafo\n(Alfonso XII)", ha="right",
            fontsize=8.5, color=COLOR_STRUCT)
    ax.plot(*A, "D", color=COLOR_ANGULO, ms=10, zorder=7, label="Boya A (400 m)")
    ax.text(A[0]+0.1, A[1]+0.2, "Boya A", fontsize=9, color=COLOR_ANGULO)
    ax.plot(*B, "D", color="#9b59b6", ms=10, zorder=7, label="Boya B (600 m)")
    ax.text(B[0]+0.1, B[1]+0.1, "Boya B", fontsize=9, color="#9b59b6")

    # Ángulo γ=35° en O
    angulo_arc(ax, O, 1.5, 0, GAMMA, COLOR_ANGULO, "35°")

    # Líneas OA y OB
    ax.text(A[0]/2 - 0.3, A[1]/2 + 0.15, "400 m",
            color=COLOR_STRUCT, fontsize=9, rotation=GAMMA)
    ax.text(OB/2, -0.8, "600 m", ha="center", color=COLOR_STRUCT, fontsize=9)

    ax.set_xlim(-0.8, OB+0.8)
    ax.set_ylim(-1.2, A[1]+1.2)
    ax.set_title("Ejercicio 4 – Distancia entre boyas (Paseo de Alfonso XII)\n"
                 r"$AB = \sqrt{h^2 + \text{base}_2^2} \approx 356{,}1$ m",
                 fontsize=11, fontweight="bold", color=COLOR_STRUCT)
    ax.legend(loc="upper right", fontsize=8.5)

    plt.tight_layout()
    plt.savefig("S4_Ej4_Boyas_Ria.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ Guardado: S4_Ej4_Boyas_Ria.png")


# ═══════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════
if __name__ == "__main__":
    import os
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    print("Generando gráficas de la Sesión 4 – Trigonometría Aplicada")
    print("=" * 60)

    ejercicio_1()
    ejercicio_2()
    ejercicio_3()
    ejercicio_4()

    print("\n✅ Todos los gráficos generados correctamente en S4/")
