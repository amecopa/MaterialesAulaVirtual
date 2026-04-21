import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Rectangle
import numpy as np

# Configuración general
plt.style.use('seaborn-v0_8-whitegrid')
output_base = ""  # Carpeta base

def guardar_plot(nombre, carpeta=""):
    ruta = f"{output_base}{carpeta}{nombre}.png" if carpeta else f"{nombre}.png"
    plt.tight_layout()
    plt.savefig(ruta, dpi=130, bbox_inches='tight')
    plt.close()
    print(f"✓ {ruta}")


# ============ SESIÓN 5: ÁRBOLES Y TABLAS ============

def arbol_mercado_berbes():
    """
    Árbol: Mercado del Berbés (Vigo)
    60% fresco, 40% congelado
    Fresco: 90% pasa control
    Congelado: 70% pasa control
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Nodo raíz
    ax.plot(0, 0.5, 'ko', markersize=12)
    ax.text(-0.15, 0.5, 'Inicio', ha='right', va='center', fontsize=10, weight='bold')
    
    # Primera rama: Fresco (arriba)
    ax.plot([0, 3], [0.5, 0.75], 'b-', linewidth=2.5)
    ax.text(1.5, 0.7, 'Fresco\n60%', ha='center', va='bottom', fontsize=9, 
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    ax.plot(3, 0.75, 'bo', markersize=10)
    
    # Primera rama: Congelado (abajo)
    ax.plot([0, 3], [0.5, 0.25], 'r-', linewidth=2.5)
    ax.text(1.5, 0.15, 'Congelado\n40%', ha='center', va='top', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))
    ax.plot(3, 0.25, 'ro', markersize=10)
    
    # Segunda rama desde Fresco
    ax.plot([3, 6], [0.75, 0.85], 'g-', linewidth=2)
    ax.text(4.5, 0.87, 'Pasa\n90%', ha='center', fontsize=8,
            bbox=dict(boxstyle='round', facecolor='lightgreen'))
    ax.plot(6, 0.85, 'go', markersize=8)
    ax.text(6.3, 0.85, '0.6 × 0.9\n= 0.54', ha='left', va='center', fontsize=9, 
            weight='bold', color='darkgreen')
    
    ax.plot([3, 6], [0.75, 0.65], 'orange', linewidth=2, linestyle='--')
    ax.text(4.5, 0.62, 'NO pasa\n10%', ha='center', fontsize=8,
            bbox=dict(boxstyle='round', facecolor='#ffe4b5'))
    ax.plot(6, 0.65, 'o', color='orange', markersize=8)
    ax.text(6.3, 0.65, '0.6 × 0.1\n= 0.06', ha='left', va='center', fontsize=9)
    
    # Segunda rama desde Congelado
    ax.plot([3, 6], [0.25, 0.35], 'g-', linewidth=2)
    ax.text(4.5, 0.37, 'Pasa\n70%', ha='center', fontsize=8,
            bbox=dict(boxstyle='round', facecolor='lightgreen'))
    ax.plot(6, 0.35, 'go', markersize=8)
    ax.text(6.3, 0.35, '0.4 × 0.7\n= 0.28', ha='left', va='center', fontsize=9,
            weight='bold', color='darkgreen')
    
    ax.plot([3, 6], [0.25, 0.15], 'orange', linewidth=2, linestyle='--')
    ax.text(4.5, 0.12, 'NO pasa\n30%', ha='center', fontsize=8,
            bbox=dict(boxstyle='round', facecolor='#ffe4b5'))
    ax.plot(6, 0.15, 'o', color='orange', markersize=8)
    ax.text(6.3, 0.15, '0.4 × 0.3\n= 0.12', ha='left', va='center', fontsize=9)
    
    ax.set_xlim(-0.5, 7.5)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('Diagrama de Árbol: Mercado del Berbés (Vigo)', fontsize=13, weight='bold')
    
    guardar_plot("arbol_berbes", "S5/")


def tabla_luces_navidad():
    """
    Tabla de contingencia para 10000 luces de Navidad de Vigo
    80% LED, 20% No-LED
    LED falla 5%, No-LED falla 15%
    """
    fig, ax = plt.subplots(figsize=(7, 4))
    
    # Datos
    data = [
        ['', 'Falla', 'No falla', 'Total'],
        ['LED', '400', '7600', '8000'],
        ['No-LED', '300', '1700', '2000'],
        ['Total', '700', '9300', '10000']
    ]
    
    # Colores
    colors = [
        ['#0056b3']*4,  # Header
        ['white']*4,
        ['white']*4,
        ['#e8f0fe']*4   # Totales
    ]
    
    # Crear tabla
    table = ax.table(cellText=data, cellColours=colors,
                     cellLoc='center', loc='center',
                     bbox=[0, 0, 1, 1])
    
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 2.2)
    
    # Estilo del header
    for i in range(4):
        cell = table[(0, i)]
        cell.set_text_props(weight='bold', color='white')
        cell.set_facecolor('#0056b3')
    
    # Estilo de la primera columna
    for i in range(1, 4):
        cell = table[(i, 0)]
        cell.set_text_props(weight='bold')
        cell.set_facecolor('#cce0ff')
    
    # Bordes
    for key, cell in table.get_celld().items():
        cell.set_edgecolor('black')
        cell.set_linewidth(1.5)
    
    ax.axis('off')
    ax.set_title('Tabla de Contingencia: Luces de Navidad de Vigo (10000 luces)',
                 fontsize=12, weight='bold', pad=20)
    
    guardar_plot("tabla_luces_navidad", "S5/")


# ============ SESIÓN 6 y 7: ÁRBOLES CON PROBABILIDAD TOTAL Y BAYES ============

def arbol_conservas_vigo():
    """
    Árbol para P. total: 3 fábricas de conservas de Vigo
    Fábrica A: 60%, defecto 2%
    Fábrica B: 30%, defecto 5%
    Fábrica C: 10%, defecto 10%
    """
    fig, ax = plt.subplots(figsize=(11, 7))
    
    # Nodo raíz
    ax.plot(0, 0.5, 'ko', markersize=14)
    
    # Fábrica A (arriba)
    ax.plot([0, 3], [0.5, 0.8], 'b-', linewidth=3)
    ax.text(1.5, 0.88, 'Fábrica A\n60%', ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='#b3d9ff'))
    ax.plot(3, 0.8, 'bo', markersize=11)
    
    # Fábrica B (medio)
    ax.plot([0, 3], [0.5, 0.5], 'g-', linewidth=3)
    ax.text(1.5, 0.58, 'Fábrica B\n30%', ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='#c6efce'))
    ax.plot(3, 0.5, 'go', markersize=11)
    
    # Fábrica C (abajo)
    ax.plot([0, 3], [0.5, 0.2], 'r-', linewidth=3)
    ax.text(1.5, 0.12, 'Fábrica C\n10%', ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='#ffc7ce'))
    ax.plot(3, 0.2, 'ro', markersize=11)
    
    # Ramas desde A
    ax.plot([3, 6.5], [0.8, 0.88], 'red', linewidth=2, linestyle='--')
    ax.text(4.8, 0.91, 'Defecto\n2%', ha='center', fontsize=8)
    ax.plot(6.5, 0.88, 'o', color='red', markersize=8)
    ax.text(7, 0.88, '0.6 × 0.02 = 0.012', ha='left', fontsize=9, weight='bold')
    
    ax.plot([3, 6.5], [0.8, 0.72], 'green', linewidth=2)
    ax.text(4.8, 0.69, 'OK\n98%', ha='center', fontsize=8)
    ax.plot(6.5, 0.72, 'go', markersize=8)
    
    # Ramas desde B
    ax.plot([3, 6.5], [0.5, 0.58], 'red', linewidth=2, linestyle='--')
    ax.text(4.8, 0.61, 'Defecto\n5%', ha='center', fontsize=8)
    ax.plot(6.5, 0.58, 'o', color='red', markersize=8)
    ax.text(7, 0.58, '0.3 × 0.05 = 0.015', ha='left', fontsize=9, weight='bold')
    
    ax.plot([3, 6.5], [0.5, 0.42], 'green', linewidth=2)
    ax.text(4.8, 0.39, 'OK\n95%', ha='center', fontsize=8)
    ax.plot(6.5, 0.42, 'go', markersize=8)
    
    # Ramas desde C
    ax.plot([3, 6.5], [0.2, 0.28], 'red', linewidth=2, linestyle='--')
    ax.text(4.8, 0.31, 'Defecto\n10%', ha='center', fontsize=8)
    ax.plot(6.5, 0.28, 'o', color='red', markersize=8)
    ax.text(7, 0.28, '0.1 × 0.1 = 0.010', ha='left', fontsize=9, weight='bold')
    
    ax.plot([3, 6.5], [0.2, 0.12], 'green', linewidth=2)
    ax.text(4.8, 0.09, 'OK\n90%', ha='center', fontsize=8)
    ax.plot(6.5, 0.12, 'go', markersize=8)
    
    # Recuadro resumen
    ax.text(3.5, 0.02, 'P(Defecto) = 0.012 + 0.015 + 0.010 = 0.037 = 3.7%',
            ha='center', fontsize=11, weight='bold',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
    
    ax.set_xlim(-0.5, 9)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('Probabilidad Total: Conservas de Vigo (3 fábricas)',
                 fontsize=13, weight='bold')
    
    guardar_plot("arbol_conservas_vigo", "S6/")


def arbol_bayes_test():
    """
    Árbol para Bayes: Test de control en PSA Vigo
    Prevalencia defecto: 1%
    Sensibilidad (detecta defecto si existe): 95%
    Especificidad (da negativo si no hay defecto): 97%
    """
    fig, ax = plt.subplots(figsize=(11, 6))
    
    # Nodo raíz
    ax.plot(0, 0.5, 'ko', markersize=14)
    
    # Defecto (arriba, rojo)
    ax.plot([0, 3], [0.5, 0.7], 'r-', linewidth=3)
    ax.text(1.5, 0.77, 'Defecto\n1%', ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='#ffc7ce'))
    ax.plot(3, 0.7, 'ro', markersize=11)
    
    # No defecto (abajo, verde)
    ax.plot([0, 3], [0.5, 0.3], 'g-', linewidth=3)
    ax.text(1.5, 0.23, 'No defecto\n99%', ha='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='#c6efce'))
    ax.plot(3, 0.3, 'go', markersize=11)
    
    # Desde Defecto
    ax.plot([3, 6.5], [0.7, 0.78], 'orange', linewidth=2.5)
    ax.text(4.8, 0.81, 'Test +\n95%', ha='center', fontsize=9)
    ax.plot(6.5, 0.78, 'o', color='orange', markersize=9)
    ax.text(7.1, 0.78, '0.01 × 0.95\n= 0.0095', ha='left', fontsize=9, weight='bold', color='darkred')
    
    ax.plot([3, 6.5], [0.7, 0.62], 'gray', linewidth=2, linestyle='--')
    ax.text(4.8, 0.59, 'Test −\n5%', ha='center', fontsize=9)
    ax.plot(6.5, 0.62, 'o', color='gray', markersize=9)
    
    # Desde No defecto
    ax.plot([3, 6.5], [0.3, 0.38], 'orange', linewidth=2.5)
    ax.text(4.8, 0.41, 'Test + (FP)\n3%', ha='center', fontsize=9)
    ax.plot(6.5, 0.38, 'o', color='orange', markersize=9)
    ax.text(7.1, 0.38, '0.99 × 0.03\n= 0.0297', ha='left', fontsize=9, weight='bold', color='darkred')
    
    ax.plot([3, 6.5], [0.3, 0.22], 'green', linewidth=2)
    ax.text(4.8, 0.19, 'Test −\n97%', ha='center', fontsize=9)
    ax.plot(6.5, 0.22, 'go', markersize=9)
    
    # Recuadro Bayes
    ax.text(3.5, 0.05, 'P(Defecto | Test +) = 0.0095 / (0.0095 + 0.0297) ≈ 24,2%',
            ha='center', fontsize=10, weight='bold',
            bbox=dict(boxstyle='round', facecolor='#fff3cd', edgecolor='orange', linewidth=2))
    
    ax.set_xlim(-0.5, 9.5)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('Teorema de Bayes: Test de Control PSA Vigo',
                 fontsize=13, weight='bold')
    
    guardar_plot("arbol_bayes_test", "S7/")


# ============ GENERAR TODAS LAS GRÁFICAS ============

if __name__ == "__main__":
    print("\n🎨 Generando gráficas para Probabilidad 4º ESO\n")
    print("=" * 50)
    
    print("\n📂 Sesión 5: Árboles y Tablas")
    arbol_mercado_berbes()
    tabla_luces_navidad()
    
    print("\n📂 Sesión 6: Probabilidad Total")
    arbol_conservas_vigo()
    
    print("\n📂 Sesión 7: Teorema de Bayes")
    arbol_bayes_test()
    
    print("\n" + "=" * 50)
    print("✅ Todas las gráficas generadas correctamente.\n")
