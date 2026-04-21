import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np

# Configuración general
plt.style.use('seaborn-v0_8-whitegrid')
output_folder = ""  # Mismo directorio

def guardar_plot(nombre):
    plt.tight_layout()
    plt.savefig(f"{output_folder}{nombre}.png", dpi=120, bbox_inches='tight')
    plt.close()
    print(f"✓ Generado: {nombre}.png")


# --- Diagrama de Venn para Ejercicio 4 ---
def diagrama_venn_ejercicio4():
    """
    A = {2, 4, 6, 8}
    B = {6, 7, 8, 9}
    A ∩ B = {6, 8}
    """
    fig, ax = plt.subplots(figsize=(7, 5))
    
    # Círculo A (azul)
    circle_A = Circle((1.2, 0), 1, color='steelblue', alpha=0.3, label='A')
    ax.add_patch(circle_A)
    
    # Círculo B (naranja)
    circle_B = Circle((1.8, 0), 1, color='orange', alpha=0.3, label='B')
    ax.add_patch(circle_B)
    
    # Etiquetas
    ax.text(0.8, 0, 'A solo\n{2, 4}', ha='center', va='center', fontsize=10, weight='bold')
    ax.text(1.5, 0, 'A∩B\n{6, 8}', ha='center', va='center', fontsize=10, weight='bold', color='darkgreen')
    ax.text(2.2, 0, 'B solo\n{7, 9}', ha='center', va='center', fontsize=10, weight='bold')
    
    ax.text(1.5, -1.8, '(A∪B)ᶜ = {1, 3, 5, 10}', ha='center', fontsize=9, style='italic', color='gray')
    
    # Rectángulo del espacio muestral
    rect = FancyBboxPatch((0, -1.5), 3, 3, boxstyle="round,pad=0.1", 
                          edgecolor='black', facecolor='none', linewidth=1.5)
    ax.add_patch(rect)
    
    ax.text(1.5, 1.7, 'Ω = {1, 2, ..., 10}', ha='center', fontsize=11, weight='bold')
    
    ax.set_xlim(-0.5, 3.5)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Diagrama de Venn: Ejercicio 4', fontsize=13, weight='bold', pad=15)
    
    guardar_plot("diagrama_venn_ej4")


# --- Espacio muestral visual: PSA Citroën (2 piezas) ---
def espacio_muestral_psa():
    """
    Representación visual del espacio muestral de 2 piezas:
    Ω = {CC, CD, DC, DD}
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    
    resultados = ['CC', 'CD', 'DC', 'DD']
    colores = ['#28a745', '#ffc107', '#ffc107', '#dc3545']  # verde, amarillo, amarillo, rojo
    etiquetas = ['Ambas\nCorrectas', 'Primera C\nSegunda D', 'Primera D\nSegunda C', 'Ambas\nDefectuosas']
    
    x_pos = np.arange(len(resultados))
    
    for i, (res, col, etiq) in enumerate(zip(resultados, colores, etiquetas)):
        rect = FancyBboxPatch((x_pos[i]-0.35, 0), 0.7, 1.2, 
                             boxstyle="round,pad=0.05", 
                             facecolor=col, edgecolor='black', linewidth=2, alpha=0.6)
        ax.add_patch(rect)
        ax.text(x_pos[i], 0.9, res, ha='center', va='center', fontsize=16, weight='bold', color='white')
        ax.text(x_pos[i], 0.4, etiq, ha='center', va='center', fontsize=9, color='white')
    
    # Leyenda de sucesos
    ax.text(1.5, -0.6, 'M = "al menos una defectuosa" = {CD, DC, DD}', 
            ha='center', fontsize=10, bbox=dict(boxstyle='round', facecolor='lightyellow'))
    ax.text(1.5, -1.0, 'N = "ninguna defectuosa" = {CC}', 
            ha='center', fontsize=10, bbox=dict(boxstyle='round', facecolor='lightgreen'))
    
    ax.set_xlim(-0.8, 3.8)
    ax.set_ylim(-1.3, 1.8)
    ax.axis('off')
    ax.set_title('Espacio Muestral: PSA Citroën Vigo (2 piezas)', fontsize=13, weight='bold', pad=10)
    
    guardar_plot("espacio_muestral_psa")


# --- Diagrama Vitrasa (Ampliación) ---
def diagrama_vitrasa():
    """
    Diagrama de Venn para servicios de Vitrasa
    P = primer servicio tarde = {RT, RR}
    Q = segundo servicio tarde = {TR, RR}
    """
    fig, ax = plt.subplots(figsize=(7, 5))
    
    # Círculos
    circle_P = Circle((1.2, 0), 1, color='#ff6b6b', alpha=0.3, label='P (1º tarde)')
    ax.add_patch(circle_P)
    
    circle_Q = Circle((1.8, 0), 1, color='#4ecdc4', alpha=0.3, label='Q (2º tarde)')
    ax.add_patch(circle_Q)
    
    # Etiquetas
    ax.text(0.8, 0, 'P solo\n{RT}', ha='center', va='center', fontsize=10, weight='bold')
    ax.text(1.5, 0, 'P∩Q\n{RR}', ha='center', va='center', fontsize=11, weight='bold', 
            color='darkred', bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
    ax.text(2.2, 0, 'Q solo\n{TR}', ha='center', va='center', fontsize=10, weight='bold')
    
    ax.text(1.5, -1.7, 'Ambos a tiempo: {TT}', ha='center', fontsize=9, style='italic', color='gray')
    
    # Rectángulo
    rect = FancyBboxPatch((0, -1.5), 3, 3, boxstyle="round,pad=0.1", 
                          edgecolor='black', facecolor='none', linewidth=1.5)
    ax.add_patch(rect)
    
    ax.text(1.5, 1.7, 'Ω = {TT, TR, RT, RR}', ha='center', fontsize=11, weight='bold')
    
    ax.set_xlim(-0.5, 3.5)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Vitrasa Línea 12-A: Dos servicios consecutivos', fontsize=13, weight='bold', pad=15)
    
    guardar_plot("diagrama_vitrasa")


# --- Generar todas las gráficas ---
if __name__ == "__main__":
    print("Generando gráficas de Sesión 1: Experimentos Aleatorios y Sucesos\n")
    diagrama_venn_ejercicio4()
    espacio_muestral_psa()
    diagrama_vitrasa()
    print("\n✅ Todas las gráficas generadas correctamente.")
