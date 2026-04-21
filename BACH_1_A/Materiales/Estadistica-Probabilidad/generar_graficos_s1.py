"""
Generador de gráficos para Sesión 1: Variables Bidimensionales
Genera diagramas de dispersión para los ejercicios
"""

import matplotlib.pyplot as plt
import numpy as np
import csv

# Configuración general
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (8, 6)

# Crear directorio de salida si no existe
import os
os.makedirs('graficos', exist_ok=True)

# ============================================================================
# GRÁFICO 1: Temperatura y Turistas en Cíes
# ============================================================================
# Leer datos del CSV
meses = []
temperaturas = []
turistas = []

with open('datos/temperatura_turistas_cies.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        meses.append(row['Mes'])
        temperaturas.append(float(row['Temperatura_Media_°C']))
        turistas.append(float(row['Turistas_Miles']))

fig, ax = plt.subplots(figsize=(10, 7))
ax.scatter(temperaturas, turistas, 
           s=100, alpha=0.7, color='#2a5298', edgecolors='black', linewidth=1.5)

# Añadir etiquetas de mes
for i, mes in enumerate(meses):
    ax.annotate(mes[:3], 
                (temperaturas[i], turistas[i]),
                xytext=(5, 5), textcoords='offset points', fontsize=8, alpha=0.7)

ax.set_xlabel('Temperatura Media (°C)', fontsize=12, fontweight='bold')
ax.set_ylabel('Turistas en Islas Cíes (miles)', fontsize=12, fontweight='bold')
ax.set_title('Relación entre Temperatura y Afluencia Turística\nIslas Cíes - Vigo', 
             fontsize=14, fontweight='bold', pad=15)
ax.grid(True, alpha=0.3, linestyle='--')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('graficos/s1_temperatura_turistas_cies.svg', format='svg', dpi=150)
print("✓ Gráfico 1 generado: s1_temperatura_turistas_cies.svg")

# ============================================================================
# GRÁFICO 2: Ejemplo de diferentes tipos de relación
# ============================================================================
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Relación lineal positiva fuerte
x1 = np.linspace(0, 10, 15)
y1 = 2*x1 + 3 + np.random.normal(0, 1, 15)
axes[0, 0].scatter(x1, y1, s=80, alpha=0.7, color='#2a5298', edgecolors='black', linewidth=1)
axes[0, 0].set_title('Correlación Positiva Fuerte', fontweight='bold')
axes[0, 0].grid(True, alpha=0.3)
axes[0, 0].set_xlabel('Variable X')
axes[0, 0].set_ylabel('Variable Y')

# Relación lineal negativa fuerte
x2 = np.linspace(0, 10, 15)
y2 = -1.5*x2 + 20 + np.random.normal(0, 1, 15)
axes[0, 1].scatter(x2, y2, s=80, alpha=0.7, color='#c2185b', edgecolors='black', linewidth=1)
axes[0, 1].set_title('Correlación Negativa Fuerte', fontweight='bold')
axes[0, 1].grid(True, alpha=0.3)
axes[0, 1].set_xlabel('Variable X')
axes[0, 1].set_ylabel('Variable Y')

# Sin correlación
x3 = np.random.rand(15) * 10
y3 = np.random.rand(15) * 10
axes[1, 0].scatter(x3, y3, s=80, alpha=0.7, color='#388e3c', edgecolors='black', linewidth=1)
axes[1, 0].set_title('Sin Correlación', fontweight='bold')
axes[1, 0].grid(True, alpha=0.3)
axes[1, 0].set_xlabel('Variable X')
axes[1, 0].set_ylabel('Variable Y')

# Relación no lineal (cuadrática)
x4 = np.linspace(-3, 3, 15)
y4 = x4**2 + np.random.normal(0, 0.5, 15)
axes[1, 1].scatter(x4, y4, s=80, alpha=0.7, color='#f9a825', edgecolors='black', linewidth=1)
axes[1, 1].set_title('Relación No Lineal (Cuadrática)', fontweight='bold')
axes[1, 1].grid(True, alpha=0.3)
axes[1, 1].set_xlabel('Variable X')
axes[1, 1].set_ylabel('Variable Y')

for ax in axes.flat:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('graficos/s1_tipos_correlacion.svg', format='svg', dpi=150)
print("✓ Gráfico 2 generado: s1_tipos_correlacion.svg")

# ============================================================================
# GRÁFICO 3: Ejemplo de tabla de doble entrada (visual)
# ============================================================================
fig, ax = plt.subplots(figsize=(8, 5))
ax.axis('tight')
ax.axis('off')

# Datos de ejemplo para la tabla
horas = [2, 3, 5, 4, 6, 7, 8, 5, 6, 7, 9, 8, 10, 9, 11]
notas = [4.5, 5.0, 6.5, 5.5, 7.0, 7.5, 8.0, 6.0, 7.0, 7.5, 8.5, 8.0, 9.0, 8.5, 9.5]

# Crear diagrama de dispersión
fig2, ax2 = plt.subplots(figsize=(9, 6))
ax2.scatter(horas, notas, s=100, alpha=0.7, color='#2a5298', edgecolors='black', linewidth=1.5)

ax2.set_xlabel('Horas de Estudio Semanal', fontsize=12, fontweight='bold')
ax2.set_ylabel('Calificación en Matemáticas', fontsize=12, fontweight='bold')
ax2.set_title('Relación entre Horas de Estudio y Calificaciones\n(Muestra de 15 alumnos)', 
              fontsize=13, fontweight='bold', pad=15)
ax2.grid(True, alpha=0.3, linestyle='--')
ax2.set_xlim(0, 12)
ax2.set_ylim(3, 10)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('graficos/s1_horas_estudio_notas.svg', format='svg', dpi=150)
print("✓ Gráfico 3 generado: s1_horas_estudio_notas.svg")

plt.close('all')
print("\n✅ Todos los gráficos de la Sesión 1 generados exitosamente")
