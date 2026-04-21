"""
generador_graficos_S2.py
========================
Trigonometría Aplicada – Sesión 2: Navegación y Alturas
IES Teis · 4º ESO · Decreto 156/2022 (Galicia)

Genera cuatro diagramas a escala que ilustran cada ejercicio de la sesión 2.
Cada figura se guarda como PNG en la misma carpeta S2/.

Requisitos:
    pip install matplotlib numpy
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Arc, FancyArrowPatch

# ─────────────────────────────────────────────────────────
# Configuración global de estilo
# ─────────────────────────────────────────────────────────
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

COLOR_STRUCT  = "#0056b3"   # azul institucional
COLOR_ANGULO  = "#d9534f"   # rojo para ángulos
COLOR_SOLUCION = "#5cb85c"  # verde para el resultado
COLOR_TIERRA  = "#8B6914"   # marrón tierra
COLOR_AGUA    = "#87CEEB"   # azul agua


def angulo_arc(ax, center, radius, theta1, theta2, color=COLOR_ANGULO, label=""):
    """Dibuja un arco de ángulo y opcionalmente su etiqueta."""
    arc = Arc(center, 2 * radius, 2 * radius,
              angle=0, theta1=theta1, theta2=theta2,
              color=color, lw=1.5)
    ax.add_patch(arc)
    if label:
        mid_angle = np.radians((theta1 + theta2) / 2)
        ax.text(center[0] + radius * 1.35 * np.cos(mid_angle),
                center[1] + radius * 1.35 * np.sin(mid_angle),
                label, color=color, fontsize=10, ha="center", va="center")


def angulo_recto(ax, vertex, size=0.8):
    """Dibuja el símbolo del ángulo recto (cuadrado pequeño)."""
    dx, dy = size, size
    square = plt.Polygon([
        vertex,
        (vertex[0] + dx, vertex[1]),
        (vertex[0] + dx, vertex[1] + dy),
        (vertex[0], vertex[1] + dy),
    ], closed=True, fill=False, edgecolor="black", lw=1)
    ax.add_patch(square)


# ═══════════════════════════════════════════════════════════
# EJERCICIO 1 – Faro de Alcabre (ángulo de depresión)
# ═══════════════════════════════════════════════════════════
def ejercicio_1():
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.set_aspect("equal")
    ax.axis("off")
    fig.patch.set_facecolor("#f8f9fa")

    # Escala: 1 unidad = 10 metros
    FARO_H = 2.5    # 25 m
    DIST   = 11.79  # 117,9 m (resultado)

    # ── Mar ──
    ax.fill_between([0, DIST + 2], -0.5, 0, color=COLOR_AGUA, alpha=0.4)
    ax.axhline(0, color=COLOR_AGUA, lw=1.5)
    ax.text(DIST / 2, -0.35, "Nivel del mar", ha="center", color=COLOR_AGUA, fontsize=9)

    # ── Faro ──
    ax.fill_betweenx([0, FARO_H], -0.4, 0.4, color=COLOR_TIERRA, alpha=0.6)
    ax.plot([0, 0], [0, FARO_H], color=COLOR_STRUCT, lw=3, label="Faro (25 m)")
    ax.text(-0.6, FARO_H / 2, "25 m", ha="right", va="center",
            color=COLOR_STRUCT, fontsize=10, rotation=90)

    # ── Linterna (punto de observación) ──
    ax.plot(0, FARO_H, "o", color=COLOR_STRUCT, ms=8)
    ax.text(0.3, FARO_H + 0.15, "Linterna\n(obs.)", fontsize=9, color=COLOR_STRUCT)

    # ── Línea horizontal desde la linterna ──
    ax.plot([0, DIST + 1.5], [FARO_H, FARO_H], "--", color="gray", lw=1)
    ax.text(DIST + 1.6, FARO_H, "Horizontal", fontsize=8, color="gray", va="center")

    # ── Línea visual al mar (hipotenusa) ──
    ax.plot([0, DIST], [FARO_H, 0], color=COLOR_ANGULO, lw=2, ls="-.",
            label="Línea visual")

    # ── Cateto horizontal (resultado d) ──
    ax.annotate("", xy=(DIST, 0), xytext=(0, 0),
                arrowprops=dict(arrowstyle="<->", color=COLOR_SOLUCION, lw=1.5))
    ax.text(DIST / 2, -0.7, r"$d = ?$   ($\approx 117{,}9$ m)",
            ha="center", color=COLOR_SOLUCION, fontsize=10, fontweight="bold")

    # ── Batea ──
    ax.plot(DIST, 0, "s", color=COLOR_STRUCT, ms=10, zorder=5)
    ax.text(DIST + 0.2, 0.2, "Batea", fontsize=9, color=COLOR_STRUCT)

    # ── Ángulo de depresión ──
    angulo_arc(ax, (0, FARO_H), 1.8, -12, 0, COLOR_ANGULO, r"$12°$" + "\n(depresión)")

    # ── Ángulo recto ──
    angulo_recto(ax, (0, 0))

    ax.set_xlim(-1.5, DIST + 3)
    ax.set_ylim(-1.2, FARO_H + 1.2)
    ax.set_title("Ejercicio 1 – Faro de Alcabre\nÁngulo de depresión → Tangente",
                 fontsize=12, fontweight="bold", color=COLOR_STRUCT)
    ax.legend(loc="upper right", fontsize=9)

    plt.tight_layout()
    plt.savefig("S2_Ej1_Faro_Alcabre.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ Guardado: S2_Ej1_Faro_Alcabre.png")


# ═══════════════════════════════════════════════════════════
# EJERCICIO 2 – Torre de alta tensión en Valadares
# ═══════════════════════════════════════════════════════════
def ejercicio_2():
    fig, ax = plt.subplots(figsize=(6, 7))
    ax.set_aspect("equal")
    ax.axis("off")
    fig.patch.set_facecolor("#f8f9fa")

    H = 2.598   # 25,98 m (resultado, escala ÷ 10)
    L = 3.0     # 30 m cable

    # Coordenadas del triángulo
    BASE = (0, 0)
    TOP  = (0, H)
    ANC  = (np.sqrt(L**2 - H**2), 0)  # punto anclaje en suelo

    # ── Suelo ──
    ax.axhline(0, color=COLOR_TIERRA, lw=2, xmin=-0.05, xmax=0.95)
    ax.fill_between([-0.5, ANC[0] + 0.5], -0.3, 0, color=COLOR_TIERRA, alpha=0.25)

    # ── Torre (cateto opuesto = altura) ──
    ax.plot([BASE[0], TOP[0]], [BASE[1], TOP[1]],
            color=COLOR_STRUCT, lw=5, solid_capstyle="round", label="Torre (h=?)")
    ax.text(-0.25, H / 2, r"$h = ?$" + "\n(≈ 25,98 m)", ha="right", va="center",
            color=COLOR_SOLUCION, fontsize=10, fontweight="bold")

    # ── Cable de seguridad (hipotenusa) ──
    ax.plot([ANC[0], TOP[0]], [ANC[1], TOP[1]],
            color=COLOR_ANGULO, lw=2.5, ls="--", label="Cable 30 m")
    mid_cable = ((ANC[0] + TOP[0]) / 2 + 0.15, (ANC[1] + TOP[1]) / 2 + 0.1)
    ax.text(*mid_cable, "30 m", color=COLOR_ANGULO, fontsize=10, rotation=-60)

    # ── Cateto horizontal ──
    ax.plot([BASE[0], ANC[0]], [0, 0], color="gray", lw=1.5, ls=":")

    # ── Técnico ──
    ax.plot(*TOP, "o", color=COLOR_STRUCT, ms=10, zorder=5)
    ax.text(0.2, TOP[1] + 0.1, "Técnico", fontsize=9, color=COLOR_STRUCT)

    # ── Punto de anclaje ──
    ax.plot(*ANC, "^", color=COLOR_TIERRA, ms=10, zorder=5)
    ax.text(ANC[0] + 0.1, -0.2, "Anclaje", fontsize=9, color=COLOR_TIERRA, ha="center")

    # ── Ángulo en el anclaje (60°) ──
    angulo_arc(ax, ANC, 0.7, 90 + (90 - 60), 180, COLOR_ANGULO, r"$60°$")

    # ── Ángulo recto en la base de la torre ──
    angulo_recto(ax, BASE, size=0.25)

    ax.set_xlim(-1, ANC[0] + 1)
    ax.set_ylim(-0.6, H + 0.8)
    ax.set_title("Ejercicio 2 – Torre de alta tensión (Valadares)\nSeno: cateto opuesto / hipotenusa",
                 fontsize=11, fontweight="bold", color=COLOR_STRUCT)
    ax.legend(loc="upper right", fontsize=9)

    plt.tight_layout()
    plt.savefig("S2_Ej2_Torre_Valadares.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ Guardado: S2_Ej2_Torre_Valadares.png")


# ═══════════════════════════════════════════════════════════
# EJERCICIO 3 – Grúa en Navantia / Barreras
# ═══════════════════════════════════════════════════════════
def ejercicio_3():
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_aspect("equal")
    ax.axis("off")
    fig.patch.set_facecolor("#f8f9fa")

    angle_deg = 45
    L = 5.0   # 50 m → escala ÷ 10
    D = L * np.cos(np.radians(angle_deg))  # 35,35 m
    H = L * np.sin(np.radians(angle_deg))

    ORIG = (0, 0)
    TIP  = (D, H)

    # ── Suelo ──
    ax.axhline(0, color=COLOR_TIERRA, lw=2)
    ax.fill_between([-0.5, D + 1.5], -0.4, 0, color=COLOR_TIERRA, alpha=0.2)

    # ── Base de la grúa ──
    ax.fill_betweenx([0, 0.8], -0.4, 0.4, color="gray", alpha=0.5)
    ax.text(0, -0.3, "Base grúa", ha="center", fontsize=9, color="gray")

    # ── Brazo de la grúa (hipotenusa) ──
    ax.plot([ORIG[0], TIP[0]], [ORIG[1], TIP[1]],
            color=COLOR_STRUCT, lw=4, solid_capstyle="round", label="Brazo 50 m")
    ax.text(D / 2 - 0.3, H / 2 + 0.3, "50 m", color=COLOR_STRUCT, fontsize=10,
            rotation=angle_deg)

    # ── Cateto horizontal (resultado) ──
    ax.annotate("", xy=(TIP[0], 0), xytext=(ORIG[0], 0),
                arrowprops=dict(arrowstyle="<->", color=COLOR_SOLUCION, lw=1.8))
    ax.text(D / 2, -0.6, r"$d = ?$   ($\approx 35{,}35$ m)",
            ha="center", color=COLOR_SOLUCION, fontsize=10, fontweight="bold")

    # ── Cateto vertical (altura) ──
    ax.plot([TIP[0], TIP[0]], [0, TIP[1]], color="gray", lw=1.5, ls=":")
    ax.text(TIP[0] + 0.15, TIP[1] / 2, f"{H*10:.1f} m", color="gray", fontsize=9, va="center")

    # ── Pieza suspendida ──
    ax.plot(*TIP, "s", color=COLOR_ANGULO, ms=12, zorder=5)
    ax.text(TIP[0] + 0.2, TIP[1] + 0.2, "Pieza\n(casco)", fontsize=9, color=COLOR_ANGULO)

    # ── Ángulo en la base ──
    angulo_arc(ax, ORIG, 1.2, 0, angle_deg, COLOR_ANGULO, r"$45°$")

    # ── Ángulo recto en la proyección vertical ──
    angulo_recto(ax, (TIP[0], 0), size=0.25)

    ax.set_xlim(-1, D + 1.5)
    ax.set_ylim(-0.9, H + 1)
    ax.set_title("Ejercicio 3 – Grúa en Navantia / Barreras\nCoseno: cateto contiguo / hipotenusa",
                 fontsize=11, fontweight="bold", color=COLOR_STRUCT)
    ax.legend(loc="upper left", fontsize=9)

    plt.tight_layout()
    plt.savefig("S2_Ej3_Grua_Navantia.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ Guardado: S2_Ej3_Grua_Navantia.png")


# ═══════════════════════════════════════════════════════════
# EJERCICIO 4 – Ángulo de ascenso del avión (Peinador)
# ═══════════════════════════════════════════════════════════
def ejercicio_4():
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_aspect("equal")
    ax.axis("off")
    fig.patch.set_facecolor("#f8f9fa")

    # Escala: ÷ 1000 → unidades
    H = 1.2   # 1200 m
    D = 4.5   # 4500 m
    alpha_deg = np.degrees(np.arctan(H / D))  # ≈ 14,93°

    ORIG = (0, 0)
    END  = (D, H)

    # ── Suelo / pista ──
    ax.fill_between([-0.3, D + 0.5], -0.2, 0, color=COLOR_TIERRA, alpha=0.3, label="Pista Peinador")
    ax.axhline(0, color=COLOR_TIERRA, lw=2)

    # ── Pista de despegue ──
    ax.fill_betweenx([0, 0.1], -0.2, 0.8, color="gray", alpha=0.5)
    ax.text(0.3, -0.3, "Peinador", ha="center", fontsize=9, color="gray")

    # ── Trayectoria del avión (hipotenusa) ──
    ax.plot([ORIG[0], END[0]], [ORIG[1], END[1]],
            color=COLOR_STRUCT, lw=2.5, ls="-.", label="Trayectoria avión")

    # ── Avión ──
    ax.plot(*END, ">", color=COLOR_STRUCT, ms=14, zorder=5)
    ax.text(END[0] + 0.1, END[1] + 0.1, "Avión\n(1 200 m)", fontsize=9, color=COLOR_STRUCT)

    # ── Cateto vertical ──
    ax.annotate("", xy=(END[0], END[1]), xytext=(END[0], 0),
                arrowprops=dict(arrowstyle="<->", color=COLOR_ANGULO, lw=1.8))
    ax.text(END[0] + 0.12, END[1] / 2, "1 200 m",
            color=COLOR_ANGULO, fontsize=10, va="center")

    # ── Cateto horizontal ──
    ax.annotate("", xy=(END[0], 0), xytext=(ORIG[0], 0),
                arrowprops=dict(arrowstyle="<->", color=COLOR_SOLUCION, lw=1.8))
    ax.text(D / 2, -0.45, "4 500 m", ha="center", color=COLOR_SOLUCION, fontsize=10)

    # ── Ángulo de ascenso ──
    angulo_arc(ax, ORIG, 1.0, 0, alpha_deg, COLOR_ANGULO,
               r"$\alpha = ?$" + f"\n(≈ {alpha_deg:.2f}°)")

    # ── Ángulo recto ──
    angulo_recto(ax, (END[0], 0), size=0.18)

    ax.set_xlim(-0.5, D + 1)
    ax.set_ylim(-0.7, H + 0.7)
    ax.set_title("Ejercicio 4 – Despegue en Peinador\n"
                 r"$\alpha = \arctan(1200/4500) \approx 14{,}93°$",
                 fontsize=11, fontweight="bold", color=COLOR_STRUCT)
    ax.legend(loc="upper left", fontsize=9)

    plt.tight_layout()
    plt.savefig("S2_Ej4_Avion_Peinador.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ Guardado: S2_Ej4_Avion_Peinador.png")


# ═══════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════
if __name__ == "__main__":
    import os
    # Aseguramos que las imágenes se guardan en la misma carpeta que el script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    print("Generando gráficas de la Sesión 2 – Trigonometría Aplicada")
    print("=" * 60)

    ejercicio_1()
    ejercicio_2()
    ejercicio_3()
    ejercicio_4()

    print("\n✅ Todos los gráficos generados correctamente en S2/")
