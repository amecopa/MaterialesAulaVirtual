"""
Generador de gráficos para Sesión 2: Distribuciones Marginales y Condicionadas
Genera gráficos para ilustrar conceptos de distribuciones condicionadas
"""

import matplotlib.pyplot as plt
import numpy as np

# Configuración general
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10

# Crear directorio si no existe
import os
os.makedirs('graficos', exist_ok=True)

# ============================================================================
# GRÁFICO 1: Ejemplo visual de distribución marginal vs condicionada
# ============================================================================

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Datos de ejemplo: Salario vs Nivel Educativo
niveles = ['Básico', 'Medio', 'Superior']
salarios_basico = [18.5, 22.3, 19.8, 21.2, 20.1]
salarios_medio = [24.5, 28.3, 26.7, 27.9, 25.4, 29.1]
salarios_superior = [32.5, 38.9, 35.2, 41.3, 36.8, 39.5, 34.1]

todos_salarios = salarios_basico + salarios_medio + salarios_superior

# Gráfico 1: Distribución marginal de salarios (todos juntos)
axes[0].hist(todos_salarios, bins=8, color='#2a5298', alpha=0.7, edgecolor='black', linewidth=1.2)
axes[0].axvline(np.mean(todos_salarios), color='red', linestyle='--', linewidth=2, label=f'Media: {np.mean(todos_salarios):.1f} mil€')
axes[0].set_xlabel('Salario Anual (miles €)', fontsize=11, fontweight='bold')
axes[0].set_ylabel('Frecuencia', fontsize=11, fontweight='bold')
axes[0].set_title('Distribución Marginal de Salarios\n(Todos los niveles educativos)', fontsize=12, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3, axis='y')
axes[0].spines['top'].set_visible(False)
axes[0].spines['right'].set_visible(False)

# Gráfico 2: Distribuciones 'marginales' separadas por nivel
bp = axes[1].boxplot([salarios_basico, salarios_medio, salarios_superior],
                      labels=niveles,
                      patch_artist=True,
                      notch=True,
                      medianprops=dict(color='red', linewidth=2))

colores = ['#f9a825', '#2a5298', '#388e3c']
for patch, color in zip(bp['boxes'], colores):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

axes[1].set_ylabel('Salario Anual (miles €)', fontsize=11, fontweight='bold')
axes[1].set_xlabel('Nivel Educativo', fontsize=11, fontweight='bold')
axes[1].set_title('Distribuciones Condicionadas de Salario\n(por Nivel Educativo)', fontsize=12, fontweight='bold')
axes[1].grid(True, alpha=0.3, axis='y')
axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('graficos/s2_marginal_vs_condicionada.svg', format='svg', dpi=150)
print("✓ Gráfico 1 generado: s2_marginal_vs_condicionada.svg")

# ============================================================================
# GRÁFICO 2: Comparación de medias condicionadas (barras)
# ============================================================================

fig, ax = plt.subplots(figsize=(10, 7))

niveles_ed = ['Básico', 'Medio', 'Superior']
medias_condicionadas = [
    np.mean(salarios_basico),
    np.mean(salarios_medio),
    np.mean(salarios_superior)
]
std_condicionadas = [
    np.std(salarios_basico, ddof=1),
    np.std(salarios_medio, ddof=1),
    np.std(salarios_superior, ddof=1)
]

bars = ax.bar(niveles_ed, medias_condicionadas, 
               color=['#f9a825', '#2a5298', '#388e3c'],
               alpha=0.7, edgecolor='black', linewidth=1.5)

# Añadir barras de error (desviación típica)
ax.errorbar(niveles_ed, medias_condicionadas, yerr=std_condicionadas,
            fmt='none', ecolor='darkred', capsize=8, capthick=2, linewidth=2)

# Añadir valores sobre las barras
for i, (nivel, media) in enumerate(zip(niveles_ed, medias_condicionadas)):
    ax.text(i, media + 1, f'{media:.1f} mil€', 
            ha='center', va='bottom', fontsize=11, fontweight='bold')

ax.set_ylabel('Salario Medio Anual (miles €)', fontsize=12, fontweight='bold')
ax.set_xlabel('Nivel Educativo', fontsize=12, fontweight='bold')
ax.set_title('Comparación de Salarios Medios Condicionados al Nivel Educativo\n(con desviación típica)', 
             fontsize=13, fontweight='bold', pad=15)
ax.set_ylim(0, max(medias_condicionadas) + 8)
ax.grid(True, alpha=0.3, axis='y', linestyle='--')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('graficos/s2_medias_condicionadas_salario.svg', format='svg', dpi=150)
print("✓ Gráfico 2 generado: s2_medias_condicionadas_salario.svg")

# ============================================================================
# GRÁFICO 3: Tabla de contingencia visual (ejemplo edad-vivienda)
# ============================================================================

fig, ax = plt.subplots(figsize=(10, 6))

# Datos de la tabla de contingencia
categorias_edad = ['<25', '25-40', '40-60', '>60']
categorias_vivienda = ['Propiedad', 'Alquiler', 'Otros']

# Frecuencias absolutas (inventadas para el ejemplo)
datos = np.array([
    [15, 45, 10],   # <25
    [35, 50, 15],   # 25-40
    [55, 20, 10],   # 40-60
    [40, 5, 5]      # >60
])

# Crear heatmap
im = ax.imshow(datos, cmap='YlOrBr', aspect='auto', alpha=0.8)

# Configurar ejes
ax.set_xticks(np.arange(len(categorias_vivienda)))
ax.set_yticks(np.arange(len(categorias_edad)))
ax.set_xticklabels(categorias_vivienda, fontsize=11, fontweight='bold')
ax.set_yticklabels(categorias_edad, fontsize=11, fontweight='bold')

# Añadir valores en las celdas
for i in range(len(categorias_edad)):
    for j in range(len(categorias_vivienda)):
        text = ax.text(j, i, datos[i, j],
                      ha="center", va="center", color="black", fontsize=13, fontweight='bold')

# Añadir totales marginales
totales_fila = datos.sum(axis=1)
totales_columna = datos.sum(axis=0)

# Títulos y etiquetas
ax.set_xlabel('Tipo de Vivienda', fontsize=12, fontweight='bold', labelpad=10)
ax.set_ylabel('Grupo de Edad', fontsize=12, fontweight='bold', labelpad=10)
ax.set_title('Tabla de Contingencia: Edad vs Tipo de Vivienda\n(Frecuencias absolutas - 200 personas)', 
             fontsize=13, fontweight='bold', pad=15)

# Añadir colorbar
cbar = plt.colorbar(im, ax=ax)
cbar.set_label('Frecuencia', rotation=270, labelpad=20, fontsize=11, fontweight='bold')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.tight_layout()
plt.savefig('graficos/s2_tabla_contingencia_edad_vivienda.svg', format='svg', dpi=150)
print("✓ Gráfico 3 generado: s2_tabla_contingencia_edad_vivienda.svg")

# ============================================================================
# GRÁFICO 4: Distribuciones condicionadas apiladas
# ============================================================================

fig, ax = plt.subplots(figsize=(11, 7))

# Porcentajes de tipo de vivienda por grupo de edad
propiedad_pct = [15/70*100, 35/100*100, 55/85*100, 40/50*100]
alquiler_pct = [45/70*100, 50/100*100, 20/85*100, 5/50*100]
otros_pct = [10/70*100, 15/100*100, 10/85*100, 5/50*100]

x = np.arange(len(categorias_edad))
width = 0.6

p1 = ax.bar(x, propiedad_pct, width, label='Propiedad', color='#2a5298', alpha=0.8, edgecolor='black')
p2 = ax.bar(x, alquiler_pct, width, bottom=propiedad_pct, label='Alquiler', color='#f9a825', alpha=0.8, edgecolor='black')
p3 = ax.bar(x, otros_pct, width, bottom=np.array(propiedad_pct)+np.array(alquiler_pct), 
           label='Otros', color='#388e3c', alpha=0.8, edgecolor='black')

ax.set_ylabel('Porcentaje (%)', fontsize=12, fontweight='bold')
ax.set_xlabel('Grupo de Edad', fontsize=12, fontweight='bold')
ax.set_title('Distribución Condicionada del Tipo de Vivienda por Grupo de Edad\n(Porcentajes)', 
            fontsize=13, fontweight='bold', pad=15)
ax.set_xticks(x)
ax.set_xticklabels(categorias_edad, fontsize=11)
ax.legend(loc='upper right', fontsize=11)
ax.set_ylim(0, 105)
ax.grid(True, alpha=0.3, axis='y', linestyle='--')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Línea de referencia al 100%
ax.axhline(100, color='red', linestyle='--', linewidth=1, alpha=0.5)

plt.tight_layout()
plt.savefig('graficos/s2_distribuciones_condicionadas_apiladas.svg', format='svg', dpi=150)
print("✓ Gráfico 4 generado: s2_distribuciones_condicionadas_apiladas.svg")

plt.close('all')
print("\n✅ Todos los gráficos de la Sesión 2 generados exitosamente")
