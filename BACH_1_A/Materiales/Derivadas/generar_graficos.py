"""
Generador de gráficas para las sesiones de Derivadas
Matemáticas Aplicadas a las CCSS I - 1º Bachillerato
IES de Teis - Vigo

Este script genera todas las visualizaciones necesarias para las 4 sesiones sobre derivadas.
Las gráficas se guardan en la carpeta imgs/ dentro del directorio Derivadas/
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# Configuración general
plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.3

# Crear carpeta de destino si no existe
output_dir = 'imgs'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"📁 Carpeta '{output_dir}/' creada")


# ============================================================================
# SESIÓN 1: TASA DE VARIACIÓN MEDIA E INSTANTÁNEA
# ============================================================================

def grafica_s1_tvm_tvi():
    """
    Gráfica que ilustra la diferencia entre TVM (recta secante) y TVI (recta tangente)
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Función ejemplo: f(x) = 0.2x^2 + 1
    x = np.linspace(0, 10, 200)
    f = 0.2 * x**2 + 1
    
    # Gráfica 1: TVM (recta secante)
    a, b = 2, 7
    fa, fb = 0.2*a**2 + 1, 0.2*b**2 + 1
    tvm = (fb - fa) / (b - a)
    
    # Recta secante: y - fa = tvm(x - a)
    x_secante = np.linspace(1, 8, 100)
    y_secante = fa + tvm * (x_secante - a)
    
    ax1.plot(x, f, 'b-', linewidth=2, label=r'$f(x) = 0{,}2x^2 + 1$')
    ax1.plot([a, b], [fa, fb], 'ro', markersize=8)
    ax1.plot(x_secante, y_secante, 'r--', linewidth=2, label=f'Recta secante (TVM = {tvm:.2f})')
    ax1.annotate(f'A({a}, {fa:.1f})', (a, fa), xytext=(a-1, fa-1), fontsize=10)
    ax1.annotate(f'B({b}, {fb:.1f})', (b, fb), xytext=(b+0.3, fb+1), fontsize=10)
    ax1.set_xlabel('x')
    ax1.set_ylabel('f(x)')
    ax1.set_title('Tasa de Variación Media (TVM)\nPendiente de la recta secante')
    ax1.legend()
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 23)
    
    # Gráfica 2: TVI (recta tangente)
    c = 5
    fc = 0.2*c**2 + 1
    # Derivada: f'(x) = 0.4x, luego f'(5) = 2
    tvi = 0.4 * c
    
    # Recta tangente
    x_tangente = np.linspace(3, 7, 100)
    y_tangente = fc + tvi * (x_tangente - c)
    
    ax2.plot(x, f, 'b-', linewidth=2, label=r'$f(x) = 0{,}2x^2 + 1$')
    ax2.plot(c, fc, 'go', markersize=10)
    ax2.plot(x_tangente, y_tangente, 'g--', linewidth=2, label=f"Recta tangente en x={c} (TVI = f'({c}) = {tvi:.1f})")
    ax2.annotate(f'C({c}, {fc:.1f})', (c, fc), xytext=(c-1.5, fc-2), fontsize=10)
    ax2.set_xlabel('x')
    ax2.set_ylabel('f(x)')
    ax2.set_title('Tasa de Variación Instantánea (TVI)\nPendiente de la recta tangente')
    ax2.legend()
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 23)
    
    plt.tight_layout()
    filename = os.path.join(output_dir, 's1_tvm_tvi.png')
    plt.savefig(filename, dpi=150)
    print(f"✅ Guardada: {filename}")
    plt.close()


def grafica_s1_peinador():
    """
    Gráfica simulada de evolución de pasajeros en el aeropuerto de Peinador
    """
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Simulación de datos (curva no lineal con estacionalidad)
    meses = np.arange(0, 25, 1)
    # Modelo: crecimiento cuadrático + estacionalidad sinusoidal
    pasajeros = 80 + 3*meses + 0.15*meses**2 + 15*np.sin(2*np.pi*meses/12)
    
    ax.plot(meses, pasajeros, 'o-', linewidth=2, markersize=6, color='darkblue', label='Pasajeros mensuales')
    
    # Resaltar algunos tramos de mayor pendiente
    # Tramo 1: meses 3-6 (primavera-verano)
    m1, m2 = 3, 6
    p1, p2 = pasajeros[m1], pasajeros[m2]
    ax.plot([m1, m2], [p1, p2], 'r--', linewidth=2, alpha=0.7)
    ax.annotate('Período de alto\ncrecimiento', xy=((m1+m2)/2, (p1+p2)/2), 
                xytext=(8, 110), fontsize=10, color='red',
                arrowprops=dict(arrowstyle='->', color='red', lw=1.5))
    
    # Tramo 2: meses 15-18 (otro pico)
    m3, m4 = 15, 18
    p3, p4 = pasajeros[m3], pasajeros[m4]
    ax.plot([m3, m4], [p3, p4], 'orange', linestyle='--', linewidth=2, alpha=0.7)
    
    ax.set_xlabel('Meses desde el inicio del estudio', fontsize=11)
    ax.set_ylabel('Pasajeros (miles)', fontsize=11)
    ax.set_title('Evolución de pasajeros en el Aeropuerto de Peinador (simulación)', fontsize=13, fontweight='bold')
    ax.legend(fontsize=10)
    ax.set_xlim(-1, 25)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    filename = os.path.join(output_dir, 's1_peinador.png')
    plt.savefig(filename, dpi=150)
    print(f"✅ Guardada: {filename}")
    plt.close()


# ============================================================================
# SESIÓN 3: CRECIMIENTO Y CURVATURA
# ============================================================================

def grafica_s3_crecimiento_curvatura():
    """
    Gráfica que ilustra crecimiento, decrecimiento, concavidad y convexidad
    """
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Función cúbica: f(x) = x^3 - 3x^2 - 9x + 5
    x = np.linspace(-3, 6, 500)
    f = x**3 - 3*x**2 - 9*x + 5
    f_prime = 3*x**2 - 6*x - 9
    f_double_prime = 6*x - 6
    
    # Puntos críticos (f' = 0): x = -1, x = 3
    x_max = -1
    x_min = 3
    f_max = x_max**3 - 3*x_max**2 - 9*x_max + 5
    f_min = x_min**3 - 3*x_min**2 - 9*x_min + 5
    
    # Punto de inflexión (f'' = 0): x = 1
    x_infl = 1
    f_infl = x_infl**3 - 3*x_infl**2 - 9*x_infl + 5
    
    # Gráfica principal
    ax.plot(x, f, 'b-', linewidth=3, label=r"$f(x) = x^3 - 3x^2 - 9x + 5$")
    
    # Marcar puntos críticos
    ax.plot(x_max, f_max, 'ro', markersize=12, label=f'Máximo relativo ({x_max}, {f_max:.0f})')
    ax.plot(x_min, f_min, 'go', markersize=12, label=f'Mínimo relativo ({x_min}, {f_min:.0f})')
    ax.plot(x_infl, f_infl, 'mo', markersize=12, label=f'Punto de inflexión ({x_infl}, {f_infl:.0f})')
    
    # Indicar zonas de crecimiento/decrecimiento con flechas
    ax.annotate('', xy=(-2.5, -10), xytext=(-2.8, -10), 
                arrowprops=dict(arrowstyle='->', lw=2, color='green'))
    ax.text(-2.65, -13, 'Creciente\n(f\' > 0)', fontsize=10, ha='center', color='green')
    
    ax.annotate('', xy=(0, 0), xytext=(2, 0), 
                arrowprops=dict(arrowstyle='->', lw=2, color='red'))
    ax.text(1, -3, 'Decreciente\n(f\' < 0)', fontsize=10, ha='center', color='red')
    
    ax.annotate('', xy=(4.5, -5), xytext=(5, -5), 
                arrowprops=dict(arrowstyle='->', lw=2, color='green'))
    ax.text(4.75, -8, 'Creciente\n(f\' > 0)', fontsize=10, ha='center', color='green')
    
    # Indicar curvatura
    ax.text(-2, 18, 'Cóncava ∩\n(f\'\' < 0)', fontsize=11, ha='center', 
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    ax.text(4, 18, 'Convexa ∪\n(f\'\' > 0)', fontsize=11, ha='center', 
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
    
    ax.axhline(0, color='k', linewidth=0.5)
    ax.axvline(0, color='k', linewidth=0.5)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('f(x)', fontsize=12)
    ax.set_title('Análisis de Crecimiento y Curvatura', fontsize=14, fontweight='bold')
    ax.legend(fontsize=10, loc='lower left')
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-25, 20)
    
    plt.tight_layout()
    filename = os.path.join(output_dir, 's3_crecimiento_curvatura.png')
    plt.savefig(filename, dpi=150)
    print(f"✅ Guardada: {filename}")
    plt.close()


def grafica_s3_analisis():
    """
    Gráfica genérica para análisis de crecimiento/decrecimiento (ejercicio de interpretación)
    """
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Función ejemplo con varios extremos
    x = np.linspace(0, 10, 400)
    f = 0.05*(x-1)*(x-4)*(x-7) + 8
    
    ax.plot(x, f, 'b-', linewidth=3)
    
    # Marcar visualmente algunas zonas sin dar valores explícitos
    ax.axhline(0, color='k', linewidth=0.5)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('f(x)', fontsize=12)
    ax.set_title('Función para análisis gráfico', fontsize=13, fontweight='bold')
    ax.grid(True, alpha=0.4)
    
    plt.tight_layout()
    filename = os.path.join(output_dir, 's3_grafica_analisis.png')
    plt.savefig(filename, dpi=150)
    print(f"✅ Guardada: {filename}")
    plt.close()


# ============================================================================
# SCRIPT PRINCIPAL
# ============================================================================

if __name__ == '__main__':
    print("\n" + "="*60)
    print("  GENERADOR DE GRÁFICAS - DERIVADAS (MACS I)")
    print("  IES de Teis - Vigo")
    print("="*60 + "\n")
    
    print("🎨 Generando gráficas para Sesión 1...")
    grafica_s1_tvm_tvi()
    grafica_s1_peinador()
    
    print("\n🎨 Generando gráficas para Sesión 3...")
    grafica_s3_crecimiento_curvatura()
    grafica_s3_analisis()
    
    print("\n" + "="*60)
    print(f"✨ PROCESO COMPLETADO")
    print(f"📂 Todas las gráficas guardadas en: {output_dir}/")
    print("="*60 + "\n")
    
    print("💡 Nota: Las sesiones 2 y 4 no requieren gráficas adicionales")
    print("   específicas generadas por código. Las referencias a")
    print("   gráficas en esas sesiones son ilustrativas o conceptuales.")
