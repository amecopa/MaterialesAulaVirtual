#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de gráficos SVG para Sesiones 9-14: PROBABILIDAD
Bloque II - Estadística y Probabilidad 1º Bach MACS
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, FancyArrow
import numpy as np

# Configuración global
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
plt.rcParams['figure.dpi'] = 100

# Crear carpeta graficos si no existe
import os
os.makedirs('graficos', exist_ok=True)

# ========== SESIÓN 9: Experimentos aleatorios y espacio muestral ==========

def s9_diagrama_venn_basico():
    """Diagrama Venn mostrando espacio muestral y sucesos"""
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    
    # Espacio muestral (rectángulo)
    rect = FancyBboxPatch((0.1, 0.1), 0.8, 0.8, 
                          boxstyle="round,pad=0.01", 
                          edgecolor='black', facecolor='#f0f0f0', 
                          linewidth=2)
    ax.add_patch(rect)
    ax.text(0.15, 0.85, 'Ω (Espacio Muestral)', fontsize=14, fontweight='bold')
    
    # Suceso A
    circle_a = Circle((0.35, 0.45), 0.15, color='#ff9999', alpha=0.6, label='Suceso A')
    ax.add_patch(circle_a)
    ax.text(0.35, 0.45, 'A', fontsize=16, ha='center', va='center', fontweight='bold')
    
    # Suceso B
    circle_b = Circle((0.6, 0.45), 0.15, color='#9999ff', alpha=0.6, label='Suceso B')
    ax.add_patch(circle_b)
    ax.text(0.6, 0.45, 'B', fontsize=16, ha='center', va='center', fontweight='bold')
    
    # Suceso imposible (vacío)
    ax.text(0.75, 0.25, '∅', fontsize=14, style='italic')
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('Conceptos básicos: Espacio Muestral y Sucesos', fontsize=14, pad=20)
    
    plt.tight_layout()
    plt.savefig('graficos/s9_diagrama_venn.svg', format='svg', bbox_inches='tight')
    plt.close()
    print("✓ S9 Gráfico: diagrama_venn.svg")

# ========== SESIÓN 10: Definiciones de probabilidad ==========

def s10_comparacion_definiciones():
    """Comparación gráfica de las tres definiciones de probabilidad"""
    fig, axes = plt.subplots(1, 3, figsize=(14, 4))
    
    # Definición Clásica (Laplace)
    ax = axes[0]
    casos_fav = 3
    casos_tot = 10
    colors = ['#4CAF50']*casos_fav + ['#E0E0E0']*(casos_tot-casos_fav)
    ax.bar(range(casos_tot), [1]*casos_tot, color=colors, edgecolor='black')
    ax.set_title('CLÁSICA (Laplace)\nP = Casos favorables / Casos posibles', 
                 fontsize=11, fontweight='bold')
    ax.set_ylabel('Equiprobables')
    ax.set_xlabel(f'P = {casos_fav}/{casos_tot} = 0.30')
    ax.set_xticks([])
    ax.set_ylim(0, 1.2)
    
    # Definición Frecuencial
    ax = axes[1]
    experimentos = np.arange(10, 1001, 10)
    prob_teorica = 0.3
    frecuencias = prob_teorica + np.random.normal(0, 0.05/np.sqrt(experimentos/100), len(experimentos))
    ax.plot(experimentos, frecuencias, color='#2196F3', linewidth=2, label='Frecuencia observada')
    ax.axhline(y=prob_teorica, color='red', linestyle='--', linewidth=2, label=f'P teórica = {prob_teorica}')
    ax.set_title('FRECUENCIAL\nP = lim (n→∞) Frecuencia relativa', 
                 fontsize=11, fontweight='bold')
    ax.set_xlabel('Número de experimentos')
    ax.set_ylabel('Frecuencia relativa')
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)
    ax.set_ylim(0.15, 0.45)
    
    # Definición Subjetiva
    ax = axes[2]
    categorias = ['Experto 1', 'Experto 2', 'Experto 3', 'Consenso']
    probabilidades = [0.35, 0.28, 0.32, 0.30]
    bars = ax.barh(categorias, probabilidades, color='#FF9800', edgecolor='black')
    ax.set_title('SUBJETIVA\nP = Grado de creencia razonada', 
                 fontsize=11, fontweight='bold')
    ax.set_xlabel('Probabilidad asignada')
    ax.set_xlim(0, 0.5)
    for i, v in enumerate(probabilidades):
        ax.text(v + 0.01, i, f'{v:.2f}', va='center', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('graficos/s10_tres_definiciones.svg', format='svg', bbox_inches='tight')
    plt.close()
    print("✓ S10 Gráfico: tres_definiciones.svg")

# ========== SESIÓN 11: Operaciones con sucesos ==========

def s11_operaciones_venn():
    """Diagramas de Venn para operaciones: unión, intersección, complementario"""
    fig, axes = plt.subplots(2, 3, figsize=(12, 8))
    
    def draw_circles(ax, highlight='none'):
        """Dibuja dos círculos y resalta según la operación"""
        # Espacio muestral
        rect = Rectangle((0, 0), 1, 1, facecolor='white', edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        
        # Círculos base
        theta = np.linspace(0, 2*np.pi, 100)
        x1, y1 = 0.35 + 0.15*np.cos(theta), 0.5 + 0.15*np.sin(theta)
        x2, y2 = 0.65 + 0.15*np.cos(theta), 0.5 + 0.15*np.sin(theta)
        
        if highlight == 'union':
            ax.fill(x1, y1, color='#ff9999', alpha=0.7)
            ax.fill(x2, y2, color='#ff9999', alpha=0.7)
        elif highlight == 'interseccion':
            # Solo la intersección
            x_int = np.linspace(0.43, 0.57, 100)
            y_top = 0.5 + np.sqrt(0.15**2 - (x_int - 0.35)**2)
            y_bot = 0.5 - np.sqrt(0.15**2 - (x_int - 0.35)**2)
            for x in x_int:
                in_circle2 = (x - 0.65)**2 + (0.5 - 0.5)**2 <= 0.15**2
                if in_circle2 and 0.43 <= x <= 0.57:
                    y1_val = 0.5 + np.sqrt(max(0, 0.15**2 - (x - 0.35)**2))
                    y2_val = 0.5 - np.sqrt(max(0, 0.15**2 - (x - 0.35)**2))
                    ax.plot([x, x], [y2_val, y1_val], color='#9999ff', linewidth=1.5, alpha=0.8)
        elif highlight == 'complementario_a':
            # Todo menos A
            ax.fill([0, 1, 1, 0], [0, 0, 1, 1], color='#ffff99', alpha=0.5)
            ax.fill(x1, y1, color='white')
        elif highlight == 'diferencia':
            # A - B (A sin la intersección)
            ax.fill(x1, y1, color='#ff9999', alpha=0.7)
            # Quitar intersección
            x_int = np.linspace(0.43, 0.57, 100)
            for x in x_int:
                in_circle2 = (x - 0.65)**2 <= 0.15**2
                if in_circle2:
                    y1_val = 0.5 + np.sqrt(max(0, 0.15**2 - (x - 0.35)**2))
                    y2_val = 0.5 - np.sqrt(max(0, 0.15**2 - (x - 0.35)**2))
                    ax.plot([x, x], [y2_val, y1_val], color='white', linewidth=1.5)
        
        # Bordes de los círculos
        ax.plot(x1, y1, 'k-', linewidth=2)
        ax.plot(x2, y2, 'k-', linewidth=2)
        ax.text(0.28, 0.5, 'A', fontsize=14, fontweight='bold')
        ax.text(0.72, 0.5, 'B', fontsize=14, fontweight='bold')
        ax.text(0.05, 0.93, 'Ω', fontsize=12)
        ax.set_xlim(-0.05, 1.05)
        ax.set_ylim(-0.05, 1.05)
        ax.axis('off')
    
    # Fila 1
    draw_circles(axes[0, 0], 'union')
    axes[0, 0].set_title('A ∪ B (UNIÓN)\n"A o B"', fontsize=11, fontweight='bold')
    
    draw_circles(axes[0, 1], 'interseccion')
    axes[0, 1].set_title('A ∩ B (INTERSECCIÓN)\n"A y B"', fontsize=11, fontweight='bold')
    
    draw_circles(axes[0, 2], 'complementario_a')
    axes[0, 2].set_title('Ā (COMPLEMENTARIO)\n"No A"', fontsize=11, fontweight='bold')
    
    # Fila 2
    draw_circles(axes[1, 0], 'diferencia')
    axes[1, 0].set_title('A − B (DIFERENCIA)\n"A pero no B"', fontsize=11, fontweight='bold')
    
    # Incompatibles
    ax = axes[1, 1]
    rect = Rectangle((0, 0), 1, 1, facecolor='white', edgecolor='black', linewidth=2)
    ax.add_patch(rect)
    circle_a = Circle((0.3, 0.5), 0.12, color='#ff9999', edgecolor='black', linewidth=2)
    circle_b = Circle((0.7, 0.5), 0.12, color='#9999ff', edgecolor='black', linewidth=2)
    ax.add_patch(circle_a)
    ax.add_patch(circle_b)
    ax.text(0.3, 0.5, 'A', fontsize=14, ha='center', va='center', fontweight='bold')
    ax.text(0.7, 0.5, 'B', fontsize=14, ha='center', va='center', fontweight='bold')
    ax.text(0.5, 0.2, 'A ∩ B = ∅', fontsize=12, ha='center', style='italic')
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.05, 1.05)
    ax.axis('off')
    axes[1, 1].set_title('INCOMPATIBLES', fontsize=11, fontweight='bold')
    
    # Leyes de Morgan
    ax = axes[1, 2]
    ax.text(0.5, 0.7, 'Leyes de De Morgan:', fontsize=12, ha='center', fontweight='bold')
    ax.text(0.5, 0.5, r'$\overline{A \cup B} = \bar{A} \cap \bar{B}$', 
            fontsize=14, ha='center', bbox=dict(boxstyle='round', facecolor='#ffffcc'))
    ax.text(0.5, 0.25, r'$\overline{A \cap B} = \bar{A} \cup \bar{B}$', 
            fontsize=14, ha='center', bbox=dict(boxstyle='round', facecolor='#ffffcc'))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    axes[1, 2].set_title('PROPIEDADES', fontsize=11, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('graficos/s11_operaciones_sucesos.svg', format='svg', bbox_inches='tight')
    plt.close()
    print("✓ S11 Gráfico: operaciones_sucesos.svg")

# ========== SESIÓN 12: Regla de Laplace y combinatoria ==========

def s12_arbol_combinatoria():
    """Diagrama de árbol para combinatoria básica"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 7))
    
    # Título
    ax.text(0.5, 0.95, 'TÉCNICAS DE RECUENTO', fontsize=14, ha='center', fontweight='bold')
    
    # Variaciones
    y_base = 0.75
    ax.add_patch(FancyBboxPatch((0.05, y_base-0.08), 0.25, 0.12, 
                                boxstyle="round,pad=0.01", 
                                edgecolor='#2196F3', facecolor='#e3f2fd', linewidth=2))
    ax.text(0.175, y_base, 'VARIACIONES', fontsize=11, ha='center', fontweight='bold')
    ax.text(0.175, y_base-0.05, r'$V_n^m = \frac{n!}{(n-m)!}$', fontsize=10, ha='center')
    ax.text(0.175, y_base-0.15, 'Importa orden', fontsize=8, ha='center', style='italic')
    ax.text(0.175, y_base-0.20, 'Sin repetición', fontsize=8, ha='center', style='italic')
    
    # Permutaciones
    ax.add_patch(FancyBboxPatch((0.375, y_base-0.08), 0.25, 0.12, 
                                boxstyle="round,pad=0.01", 
                                edgecolor='#4CAF50', facecolor='#e8f5e9', linewidth=2))
    ax.text(0.5, y_base, 'PERMUTACIONES', fontsize=11, ha='center', fontweight='bold')
    ax.text(0.5, y_base-0.05, r'$P_n = n!$', fontsize=10, ha='center')
    ax.text(0.5, y_base-0.15, 'm = n (todos)', fontsize=8, ha='center', style='italic')
    ax.text(0.5, y_base-0.20, 'Caso especial de V', fontsize=8, ha='center', style='italic')
    
    # Combinaciones
    ax.add_patch(FancyBboxPatch((0.7, y_base-0.08), 0.25, 0.12, 
                                boxstyle="round,pad=0.01", 
                                edgecolor='#FF9800', facecolor='#fff3e0', linewidth=2))
    ax.text(0.825, y_base, 'COMBINACIONES', fontsize=11, ha='center', fontweight='bold')
    ax.text(0.825, y_base-0.05, r'$C_n^m = \binom{n}{m} = \frac{n!}{m!(n-m)!}$', fontsize=10, ha='center')
    ax.text(0.825, y_base-0.15, 'NO importa orden', fontsize=8, ha='center', style='italic')
    ax.text(0.825, y_base-0.20, 'Sin repetición', fontsize=8, ha='center', style='italic')
    
    # Ejemplo comparativo
    y_ej = 0.35
    ax.text(0.5, y_ej+0.1, 'EJEMPLO: Elegir 2 letras de {A, B, C}', 
            fontsize=10, ha='center', fontweight='bold', 
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.3))
    
    # Variaciones
    ax.text(0.175, y_ej-0.05, 'Con orden:', fontsize=9, ha='center', style='italic')
    ax.text(0.175, y_ej-0.10, 'AB, BA, AC, CA,', fontsize=8, ha='center',family='monospace')
    ax.text(0.175, y_ej-0.15, 'BC, CB', fontsize=8, ha='center', family='monospace')
    ax.text(0.175, y_ej-0.22, r'$V_3^2 = \frac{3!}{1!} = 6$', fontsize=9, ha='center', 
            bbox=dict(boxstyle='round', facecolor='#e3f2fd'))
    
    # Combinaciones
    ax.text(0.825, y_ej-0.05, 'Sin orden:', fontsize=9, ha='center', style='italic')
    ax.text(0.825, y_ej-0.10, '{A,B}, {A,C},', fontsize=8, ha='center', family='monospace')
    ax.text(0.825, y_ej-0.15, '{B,C}', fontsize=8, ha='center', family='monospace')
    ax.text(0.825, y_ej-0.22, r'$C_3^2 = \binom{3}{2} = 3$', fontsize=9, ha='center', 
            bbox=dict(boxstyle='round', facecolor='#fff3e0'))
    
    # Regla general
    ax.text(0.5, 0.05, '💡 Pregunta clave: ¿Importa el orden? SÍ→Variaciones | NO→Combinaciones', 
            fontsize=10, ha='center', 
            bbox=dict(boxstyle='round', facecolor='#ffcccc', edgecolor='red', linewidth=2))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('graficos/s12_combinatoria.svg', format='svg', bbox_inches='tight')
    plt.close()
    print("✓ S12 Gráfico: combinatoria.svg")

# ========== SESIÓN 13: Probabilidad condicionada ==========

def s13_arbol_probabilidad():
    """Árbol de probabilidad para prob. condicionada"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    
    # Configuración
    ax.text(0.5, 0.95, 'ÁRBOL DE PROBABILIDAD - Ejemplo: Test médico', 
            fontsize=13, ha='center', fontweight='bold')
    
    # Nodo inicial
    ax.plot([0.1], [0.5], 'ko', markersize=15)
    ax.text(0.05, 0.5, 'Inicio', fontsize=10, ha='right', va='center')
    
    # Primera ramificación: Enfermo / Sano
    ax.plot([0.1, 0.35], [0.5, 0.7], 'b-', linewidth=2)
    ax.plot([0.1, 0.35], [0.5, 0.3], 'b-', linewidth=2)
    
    ax.text(0.22, 0.65, 'P(E)=0.01', fontsize=9, ha='center', 
            bbox=dict(boxstyle='round', facecolor='#ffe6e6'))
    ax.text(0.22, 0.35, 'P(S)=0.99', fontsize=9, ha='center', 
            bbox=dict(boxstyle='round', facecolor='#e6ffe6'))
    
    ax.plot([0.35], [0.7], 'ro', markersize=12)
    ax.text(0.35, 0.75, 'Enfermo', fontsize=10, ha='center', fontweight='bold', color='red')
    ax.plot([0.35], [0.3], 'go', markersize=12)
    ax.text(0.35, 0.25, 'Sano', fontsize=10, ha='center', fontweight='bold', color='green')
    
    # Segunda ramificación desde Enfermo
    ax.plot([0.35, 0.65], [0.7, 0.8], 'r-', linewidth=1.5)
    ax.plot([0.35, 0.65], [0.7, 0.6], 'r-', linewidth=1.5, linestyle='--')
    
    ax.text(0.5, 0.78, 'P(+|E)=0.95', fontsize=8, ha='center', 
            bbox=dict(boxstyle='round', facecolor='yellow'))
    ax.text(0.5, 0.63, 'P(−|E)=0.05', fontsize=8, ha='center', 
            bbox=dict(boxstyle='round', facecolor='lightgray'))
    
    ax.plot([0.65], [0.8], 'o', color='orange', markersize=10)
    ax.text(0.72, 0.8, 'Test +', fontsize=9, va='center', fontweight='bold')
    ax.plot([0.65], [0.6], 'o', color='gray', markersize=10)
    ax.text(0.72, 0.6, 'Test −', fontsize=9, va='center')
    
    # Segunda ramificación desde Sano
    ax.plot([0.35, 0.65], [0.3, 0.4], 'g-', linewidth=1.5, linestyle='--')
    ax.plot([0.35, 0.65], [0.3, 0.2], 'g-', linewidth=1.5)
    
    ax.text(0.5, 0.37, 'P(+|S)=0.02', fontsize=8, ha='center', 
            bbox=dict(boxstyle='round', facecolor='lightgray'))
    ax.text(0.5, 0.23, 'P(−|S)=0.98', fontsize=8, ha='center', 
            bbox=dict(boxstyle='round', facecolor='lightgreen'))
    
    ax.plot([0.65], [0.4], 'o', color='gray', markersize=10)
    ax.text(0.72, 0.4, 'Test +', fontsize=9, va='center')
    ax.plot([0.65], [0.2], 'o', color='lightgreen', markersize=10)
    ax.text(0.72, 0.2, 'Test −', fontsize=9, va='center', fontweight='bold')
    
    # Cálculos finales
    ax.text(0.9, 0.8, '0.01×0.95 = 0.0095', fontsize=8, ha='center', family='monospace')
    ax.text(0.9, 0.6, '0.01×0.05 = 0.0005', fontsize=8, ha='center', family='monospace')
    ax.text(0.9, 0.4, '0.99×0.02 = 0.0198', fontsize=8, ha='center', family='monospace')
    ax.text(0.9, 0.2, '0.99×0.98 = 0.9702', fontsize=8, ha='center', family='monospace')
    
    # Leyenda
    ax.text(0.5, 0.05, 'P(E|+) = P(E∩+)/P(+) = 0.0095/(0.0095+0.0198) = 0.324', 
            fontsize=10, ha='center', 
            bbox=dict(boxstyle='round', facecolor='#fff9c4', edgecolor='orange', linewidth=2))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('graficos/s13_arbol_probabilidad.svg', format='svg', bbox_inches='tight')
    plt.close()
    print("✓ S13 Gráfico: arbol_probabilidad.svg")

# ========== SESIÓN 14: Teorema de Bayes ==========

def s14_bayes_visual():
    """Representación visual del Teorema de Bayes"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Gráfico 1: Probabilidad total
    ax1.text(0.5, 0.95, 'TEOREMA DE LA PROBABILIDAD TOTAL', 
             fontsize=12, ha='center', fontweight='bold')
    
    # Partición del espacio
    colors = ['#ffcccc', '#ccffcc', '#ccccff', '#ffffcc']
    labels = ['A₁', 'A₂', 'A₃', 'A₄']
    widths = [0.25, 0.30, 0.20, 0.25]
    x_start = 0.1
    
    for i, (w, c, l) in enumerate(zip(widths, colors, labels)):
        rect = Rectangle((x_start, 0.5), w, 0.35, facecolor=c, edgecolor='black', linewidth=2)
        ax1.add_patch(rect)
        ax1.text(x_start + w/2, 0.675, l, fontsize=14, ha='center', va='center', fontweight='bold')
        ax1.text(x_start + w/2, 0.45, f'P({l})={w:.2f}', fontsize=9, ha='center')
        x_start += w
    
    ax1.text(0.05, 0.675, 'Ω', fontsize=12, ha='right', va='center', fontweight='bold')
    
    # Suceso B atravesando particiones
    b_rect = Rectangle((0.15, 0.55), 0.55, 0.15, facecolor='orange', 
                       alpha=0.5, edgecolor='red', linewidth=3, linestyle='--')
    ax1.add_patch(b_rect)
    ax1.text(0.425, 0.625, 'B', fontsize=14, ha='center', va='center', 
             fontweight='bold', color='red')
    
    ax1.text(0.5, 0.25, r'$P(B) = \sum_{i=1}^{n} P(A_i) \cdot P(B|A_i)$', 
             fontsize=13, ha='center',
             bbox=dict(boxstyle='round', facecolor='yellow', edgecolor='red', linewidth=2))
    
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0.2, 1)
    ax1.axis('off')
    
    # Gráfico 2: Teorema de Bayes
    ax2.text(0.5, 0.95, 'TEOREMA DE BAYES', 
             fontsize=12, ha='center', fontweight='bold')
    
    ax2.text(0.5, 0.75, r'Conocemos P(B|A), queremos P(A|B)', 
             fontsize=11, ha='center', style='italic')
    
    # Fórmula principal
    formula_y = 0.55
    ax2.text(0.5, formula_y, r'$P(A_i|B) = \frac{P(A_i) \cdot P(B|A_i)}{P(B)}$', 
             fontsize=16, ha='center',
             bbox=dict(boxstyle='round', facecolor='#e3f2fd', edgecolor='blue', linewidth=3))
    
    # Desglose
    ax2.text(0.5, 0.35, r'$P(A_i|B) = \frac{P(A_i) \cdot P(B|A_i)}{\sum_{j=1}^{n} P(A_j) \cdot P(B|A_j)}$', 
             fontsize=14, ha='center',
             bbox=dict(boxstyle='round', facecolor='#fff3e0'))
    
    # Interpretación
    ax2.text(0.5, 0.15, '📊 Invierte la dirección del condicionamiento', 
             fontsize=10, ha='center')
    ax2.text(0.5, 0.08, '(De "B dado A" a "A dado B")', 
             fontsize=9, ha='center', style='italic')
    
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis('off')
    
    plt.tight_layout()
    plt.savefig('graficos/s14_teorema_bayes.svg', format='svg', bbox_inches='tight')
    plt.close()
    print("✓ S14 Gráfico: teorema_bayes.svg")

# ========== EJECUCIÓN PRINCIPAL ==========

if __name__ == '__main__':
    print("\n" + "="*60)
    print("   GENERANDO GRÁFICOS SESIONES 9-14: PROBABILIDAD")
    print("="*60 + "\n")
    
    s9_diagrama_venn_basico()
    s10_comparacion_definiciones()
    s11_operaciones_venn()
    s12_arbol_combinatoria()
    s13_arbol_probabilidad()
    s14_bayes_visual()
    
    print("\n" + "="*60)
    print("   ✅ TODOS LOS GRÁFICOS GENERADOS EXITOSAMENTE")
    print("="*60 + "\n")
