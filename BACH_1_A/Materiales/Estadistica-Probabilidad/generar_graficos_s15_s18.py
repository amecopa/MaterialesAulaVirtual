#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de gráficos SVG para Sesiones 15-18: INFERENCIA ESTADÍSTICA
Bloque III - Estadística y Probabilidad 1º Bach MACS
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle, FancyBboxPatch, Ellipse, FancyArrowPatch
import numpy as np

# Configuración global
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
plt.rcParams['figure.dpi'] = 100

import os
os.makedirs('graficos', exist_ok=True)

# Funciones para distribución normal (sin scipy)
def normal_pdf(x, mu=0, sigma=1):
    """Función de densidad de probabilidad normal"""
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

# ========== SESIÓN 15: Muestreo y distribuciones muestrales ==========

def s15_muestreo_poblacion():
    """Visualización de población vs muestra"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Población
    ax1.set_title('POBLACIÓN (N)', fontsize=13, fontweight='bold')
    np.random.seed(42)
    x_pob = np.random.normal(170, 10, 1000)
    ax1.hist(x_pob, bins=30, color='#2196F3', alpha=0.7, edgecolor='black')
    ax1.axvline(x_pob.mean(), color='red', linestyle='--', linewidth=2, label=f'μ = {x_pob.mean():.1f}')
    ax1.set_xlabel('Altura (cm)')
    ax1.set_ylabel('Frecuencia')
    ax1.legend()
    ax1.grid(alpha=0.3)
    
    # Muestra
    ax2.set_title('MUESTRA (n = 50)', fontsize=13, fontweight='bold')
    muestra = np.random.choice(x_pob, size=50, replace=False)
    ax2.hist(muestra, bins=10, color='#4CAF50', alpha=0.7, edgecolor='black')
    ax2.axvline(muestra.mean(), color='red', linestyle='--', linewidth=2, label=f'x̄ = {muestra.mean():.1f}')
    ax2.set_xlabel('Altura (cm)')
    ax2.set_ylabel('Frecuencia')
    ax2.legend()
    ax2.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('graficos/s15_poblacion_muestra.svg', format='svg', bbox_inches='tight')
    plt.close()
    print("✓ S15 Gráfico 1: poblacion_muestra.svg")

def s15_teorema_central_limite():
    """Demostración visual del Teorema Central del Límite"""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Distribución poblacional UNIFORME
    ax = axes[0, 0]
    poblacion = np.random.uniform(0, 10, 10000)
    ax.hist(poblacion, bins=50, color='#FF9800', alpha=0.7, edgecolor='black')
    ax.set_title('Población: Uniforme(0,10)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Frecuencia')
    
    # Distribución de medias muestrales n=5
    ax = axes[0, 1]
    medias_n5 = [np.random.uniform(0, 10, 5).mean() for _ in range(1000)]
    ax.hist(medias_n5, bins=30, color='#9C27B0', alpha=0.7, edgecolor='black', density=True)
    x = np.linspace(3, 7, 100)
    ax.plot(x, normal_pdf(x, 5, np.std(medias_n5)), 'r-', linewidth=2, label='Normal teórica')
    ax.set_title('Distribución de x̄ (n=5)', fontsize=11, fontweight='bold')
    ax.legend()
    
    # Distribución de medias muestrales n=30
    ax = axes[1, 0]
    medias_n30 = [np.random.uniform(0, 10, 30).mean() for _ in range(1000)]
    ax.hist(medias_n30, bins=30, color='#3F51B5', alpha=0.7, edgecolor='black', density=True)
    x = np.linspace(4, 6, 100)
    ax.plot(x, normal_pdf(x, 5, np.std(medias_n30)), 'r-', linewidth=2, label='Normal teórica')
    ax.set_title('Distribución de x̄ (n=30)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Densidad')
    ax.set_xlabel('Media muestral')
    ax.legend()
    
    # Distribución de medias muestrales n=100
    ax = axes[1, 1]
    medias_n100 = [np.random.uniform(0, 10, 100).mean() for _ in range(1000)]
    ax.hist(medias_n100, bins=30, color='#009688', alpha=0.7, edgecolor='black', density=True)
    x = np.linspace(4.5, 5.5, 100)
    ax.plot(x, normal_pdf(x, 5, np.std(medias_n100)), 'r-', linewidth=2, label='Normal teórica')
    ax.set_title('Distribución de x̄ (n=100)', fontsize=11, fontweight='bold')
    ax.set_xlabel('Media muestral')
    ax.legend()
    
    fig.suptitle('TEOREMA CENTRAL DEL LÍMITE: Mayor n → Más normal', fontsize=14, fontweight='bold', y=1.00)
    plt.tight_layout()
    plt.savefig('graficos/s15_teorema_central_limite.svg', format='svg', bbox_inches='tight')
    plt.close()
    print("✓ S15 Gráfico 2: teorema_central_limite.svg")

# ========== SESIÓN 16: Estimación e intervalos ==========

def s16_estimacion_puntual_vs_intervalo():
    """Comparación estimación puntual vs intervalo"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Estimación puntual
    ax1.set_xlim(160, 180)
    ax1.set_ylim(0, 1)
    ax1.arrow(170, 0.5, 0, -0.3, head_width=1, head_length=0.05, fc='red', ec='red', linewidth=3)
    ax1.plot([170], [0.15], 'ro', markersize=15)
    ax1.text(170, 0.7, 'x̄ = 170 cm', fontsize=14, ha='center', fontweight='bold')
    ax1.text(170, 0.05, 'Estimación\nPUNTUAL', fontsize=12, ha='center', 
             bbox=dict(boxstyle='round', facecolor='#ffcccc'))
    ax1.set_title('ESTIMADOR PUNTUAL', fontsize=13, fontweight='bold')
    ax1.set_xlabel('Altura media (cm)')
    ax1.set_xticks([160, 165, 170, 175, 180])
    ax1.set_yticks([])
    ax1.axhline(0.15, color='gray', linestyle='--', alpha=0.3)
    
    # Intervalo de confianza
    ax2.set_xlim(160, 180)
    ax2.set_ylim(0, 1)
    ic_inf, ic_sup = 167, 173
    ax2.plot([ic_inf, ic_sup], [0.5, 0.5], 'b-', linewidth=8, alpha=0.5, label='IC 95%')
    ax2.plot([ic_inf], [0.5], 'b|', markersize=20, markeredgewidth=3)
    ax2.plot([ic_sup], [0.5], 'b|', markersize=20, markeredgewidth=3)
    ax2.plot([170], [0.5], 'ro', markersize=10)
    ax2.text(170, 0.7, 'Intervalo: [167, 173]', fontsize=13, ha='center', fontweight='bold')
    ax2.text(170, 0.25, 'Estimación por\nINTERVALO', fontsize=12, ha='center',
             bbox=dict(boxstyle='round', facecolor='#ccccff'))
    ax2.text(170, 0.1, '95% confianza:\nμ ∈ [167, 173]', fontsize=10, ha='center', style='italic')
    ax2.set_title('INTERVALO DE CONFIANZA', fontsize=13, fontweight='bold')
    ax2.set_xlabel('Altura media (cm)')
    ax2.set_xticks([160, 165, 170, 175, 180])
    ax2.set_yticks([])
    
    plt.tight_layout()
    plt.savefig('graficos/s16_puntual_vs_intervalo.svg', format='svg', bbox_inches='tight')
    plt.close()
    print("✓ S16 Gráfico: puntual_vs_intervalo.svg")

# ========== SESIÓN 17: Intervalos de confianza ==========

def s17_interpretacion_ic():
    """Interpretación de intervalos de confianza"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    
    # Parámetro poblacional verdadero
    mu_real = 170
    ax.axvline(mu_real, color='red', linestyle='--', linewidth=3, label='μ real (desconocido)', zorder=10)
    
    # Simular 20 muestras con sus ICs
    np.random.seed(123)
    n_muestras = 20
    capturan = 0
    
    for i in range(n_muestras):
        muestra = np.random.normal(mu_real, 10, 30)
        x_barra = muestra.mean()
        s = muestra.std(ddof=1)
        error = 1.96 * s / np.sqrt(30)
        ic_inf = x_barra - error
        ic_sup = x_barra + error
        
        # Verificar si captura μ
        captura = (ic_inf <= mu_real <= ic_sup)
        if captura:
            capturan += 1
            color = 'blue'
            alpha = 0.6
        else:
            color = 'red'
            alpha = 0.9
        
        # Dibujar intervalo
        y_pos = n_muestras - i
        ax.plot([ic_inf, ic_sup], [y_pos, y_pos], color=color, linewidth=2, alpha=alpha)
        ax.plot([ic_inf], [y_pos], '|', color=color, markersize=10, markeredgewidth=2)
        ax.plot([ic_sup], [y_pos], '|', color=color, markersize=10, markeredgewidth=2)
        ax.plot([x_barra], [y_pos], 'o', color=color, markersize=6)
    
    ax.set_ylim(0, n_muestras + 1)
    ax.set_xlabel('Altura (cm)', fontsize=12)
    ax.set_ylabel('Muestra #', fontsize=12)
    ax.set_title(f'20 Intervalos de Confianza al 95%\n{capturan}/20 capturan μ = {mu_real} cm ({capturan/n_muestras*100:.0f}%)', 
                 fontsize=13, fontweight='bold')
    ax.grid(alpha=0.3, axis='x')
    
    # Leyenda
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], color='red', linewidth=3, linestyle='--', label='μ real = 170 cm'),
        Line2D([0], [0], color='blue', linewidth=2, label='IC que captura μ'),
        Line2D([0], [0], color='red', linewidth=2, label='IC que NO captura μ')
    ]
    ax.legend(handles=legend_elements, loc='upper right')
    
    plt.tight_layout()
    plt.savefig('graficos/s17_interpretacion_ic.svg', format='svg', bbox_inches='tight')
    plt.close()
    print("✓ S17 Gráfico 1: interpretacion_ic.svg")

def s17_nivel_confianza_amplitud():
    """Relación nivel de confianza y amplitud del IC"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    # Datos de ejemplo
    x_barra = 170
    s = 10
    n = 30
    
    niveles = [90, 95, 99]
    z_valores = [1.645, 1.96, 2.576]
    colores = ['#4CAF50', '#2196F3', '#FF9800']
    
    for i, (nivel, z, color) in enumerate(zip(niveles, z_valores, colores)):
        error = z * s / np.sqrt(n)
        ic_inf = x_barra - error
        ic_sup = x_barra + error
        amplitud = ic_sup - ic_inf
        
        y_pos = 3 - i
        ax.plot([ic_inf, ic_sup], [y_pos, y_pos], color=color, linewidth=10, alpha=0.6)
        ax.plot([ic_inf], [y_pos], '|', color=color, markersize=20, markeredgewidth=4)
        ax.plot([ic_sup], [y_pos], '|', color=color, markersize=20, markeredgewidth=4)
        ax.plot([x_barra], [y_pos], 'ko', markersize=8)
        
        ax.text(x_barra + 8, y_pos, f'{nivel}% confianza\nAmplitud: {amplitud:.1f} cm', 
                fontsize=10, va='center', bbox=dict(boxstyle='round', facecolor=color, alpha=0.3))
    
    ax.axvline(x_barra, color='black', linestyle='--', alpha=0.5, label='x̄ = 170')
    ax.set_ylim(0.5, 3.5)
    ax.set_xlim(160, 185)
    ax.set_xlabel('Altura (cm)', fontsize=12)
    ax.set_yticks([1, 2, 3])
    ax.set_yticklabels(['99%', '95%', '90%'])
    ax.set_ylabel('Nivel de confianza', fontsize=12)
    ax.set_title('Mayor confianza → Mayor amplitud del intervalo', fontsize=13, fontweight='bold')
    ax.grid(alpha=0.3, axis='x')
    
    plt.tight_layout()
    plt.savefig('graficos/s17_confianza_amplitud.svg', format='svg', bbox_inches='tight')
    plt.close()
    print("✓ S17 Gráfico 2: confianza_amplitud.svg")

# ========== SESIÓN 18: Contraste de hipótesis ==========

def s18_regiones_decision():
    """Regiones de aceptación y rechazo en contraste de hipótesis"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    
    # Distribución bajo H0
    x = np.linspace(-4, 4, 1000)
    y = normal_pdf(x, 0, 1)
    
    ax.plot(x, y, 'b-', linewidth=2, label='Distribución bajo H₀')
    ax.fill_between(x, 0, y, alpha=0.3, color='lightblue')
    
    # Región de rechazo (bilateral α=0.05)
    alpha = 0.05
    z_crit = 1.96
    
    # Cola izquierda
    x_izq = x[x <= -z_crit]
    y_izq = normal_pdf(x_izq, 0, 1)
    ax.fill_between(x_izq, 0, y_izq, alpha=0.6, color='red', label=f'Región rechazo (α={alpha})')
    
    # Cola derecha
    x_der = x[x >= z_crit]
    y_der = normal_pdf(x_der, 0, 1)
    ax.fill_between(x_der, 0, y_der, alpha=0.6, color='red')
    
    # Valores críticos
    ax.axvline(-z_crit, color='red', linestyle='--', linewidth=2)
    ax.axvline(z_crit, color='red', linestyle='--', linewidth=2)
    ax.text(-z_crit, -0.05, f'-{z_crit}', ha='center', fontsize=11, fontweight='bold')
    ax.text(z_crit, -0.05, f'+{z_crit}', ha='center', fontsize=11, fontweight='bold')
    
    # Etiquetas de regiones
    ax.text(0, 0.2, 'REGIÓN DE\nACEPTACIÓN\n(No rechazar H₀)', 
            ha='center', fontsize=12, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    ax.text(-3, 0.05, f'α/2 = {alpha/2}', ha='center', fontsize=10, color='red', fontweight='bold')
    ax.text(3, 0.05, f'α/2 = {alpha/2}', ha='center', fontsize=10, color='red', fontweight='bold')
    
    ax.set_xlabel('Estadístico de contraste (z)', fontsize=12)
    ax.set_ylabel('Densidad', fontsize=12)
    ax.set_title('CONTRASTE BILATERAL: Regiones de decisión (α = 0.05)', fontsize=13, fontweight='bold')
    ax.legend(loc='upper left')
    ax.set_ylim(-0.08, 0.45)
    ax.grid(alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('graficos/s18_regiones_decision.svg', format='svg', bbox_inches='tight')
    plt.close()
    print("✓ S18 Gráfico 1: regiones_decision.svg")

def s18_errores_tipo_i_ii():
    """Visualización de errores Tipo I y Tipo II"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Error Tipo I (α): Rechazar H0 siendo verdadera
    x = np.linspace(-4, 4, 1000)
    y_h0 = normal_pdf(x, 0, 1)
    
    ax1.plot(x, y_h0, 'b-', linewidth=2, label='H₀: μ = μ₀')
    ax1.fill_between(x, 0, y_h0, alpha=0.2, color='blue')
    
    z_crit = 1.96
    x_rechazo = x[x >= z_crit]
    y_rechazo = normal_pdf(x_rechazo, 0, 1)
    ax1.fill_between(x_rechazo, 0, y_rechazo, alpha=0.8, color='red', 
                     label='Error Tipo I (α)')
    
    ax1.axvline(z_crit, color='red', linestyle='--', linewidth=2)
    ax1.text(z_crit + 0.5, 0.2, f'α = 0.025\n(rechazamos H₀\nerróneamente)', 
             fontsize=10, bbox=dict(boxstyle='round', facecolor='#ffcccc'))
    ax1.set_title('ERROR TIPO I (Falso Positivo)', fontsize=12, fontweight='bold')
    ax1.set_xlabel('Estadístico')
    ax1.set_ylabel('Densidad')
    ax1.legend()
    ax1.grid(alpha=0.3)
    
    # Error Tipo II (β): No rechazar H0 siendo falsa
    mu_alternativa = 2.5
    y_h1 = normal_pdf(x, mu_alternativa, 1)
    
    ax2.plot(x, y_h0, 'b--', linewidth=2, alpha=0.5, label='H₀: μ = μ₀')
    ax2.plot(x, y_h1, 'g-', linewidth=2, label='H₁: μ = μ₁ (verdadera)')
    ax2.fill_between(x, 0, y_h1, alpha=0.2, color='green')
    
    # Región de no rechazo bajo H0
    x_no_rechazo = x[x <= z_crit]
    y_h1_beta = normal_pdf(x_no_rechazo, mu_alternativa, 1)
    ax2.fill_between(x_no_rechazo, 0, y_h1_beta, alpha=0.8, color='orange',
                     label='Error Tipo II (β)')
    
    ax2.axvline(z_crit, color='red', linestyle='--', linewidth=2)
    ax2.text(0.5, 0.15, 'β\n(no rechazamos H₀\npero es falsa)', 
             fontsize=10, bbox=dict(boxstyle='round', facecolor='#ffddcc'))
    ax2.set_title('ERROR TIPO II (Falso Negativo)', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Estadístico')
    ax2.legend()
    ax2.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('graficos/s18_errores_tipo_i_ii.svg', format='svg', bbox_inches='tight')
    plt.close()
    print("✓ S18 Gráfico 2: errores_tipo_i_ii.svg")

# ========== EJECUCIÓN PRINCIPAL ==========

if __name__ == '__main__':
    print("\n" + "="*65)
    print("   GENERANDO GRÁFICOS SESIONES 15-18: INFERENCIA ESTADÍSTICA")
    print("="*65 + "\n")
    
    s15_muestreo_poblacion()
    s15_teorema_central_limite()
    s16_estimacion_puntual_vs_intervalo()
    s17_interpretacion_ic()
    s17_nivel_confianza_amplitud()
    s18_regiones_decision()
    s18_errores_tipo_i_ii()
    
    print("\n" + "="*65)
    print("   ✅ TODOS LOS GRÁFICOS BLOQUE III GENERADOS EXITOSAMENTE")
    print("="*65 + "\n")
