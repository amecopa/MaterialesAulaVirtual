"""
Generador de gráficos para Sesiones 3-8
Genera todos los gráficos del bloque de Estadística Bidimensional
"""

import matplotlib.pyplot as plt
import numpy as np
import csv

# Configuración general
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10

import os
os.makedirs('graficos', exist_ok=True)

# ============================================================================
# SESIÓN 3: COVARIANZA
# ============================================================================

# Gráfico 1: Ilustración de covarianza positiva/negativa
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Covarianza positiva
x_pos = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y_pos = np.array([2, 3, 4, 5, 6, 7, 8, 9]) + np.random.normal(0, 0.5, 8)
axes[0].scatter(x_pos, y_pos, s=100, alpha=0.7, color='#2a5298', edgecolors='black', linewidth=1.5)
axes[0].axhline(np.mean(y_pos), color='red', linestyle='--', alpha=0.6, label=f'Media Y')
axes[0].axvline(np.mean(x_pos), color='blue', linestyle='--', alpha=0.6, label=f'Media X')
axes[0].set_title('Covarianza Positiva\n(Sxy > 0)', fontweight='bold')
axes[0].set_xlabel('Variable X')
axes[0].set_ylabel('Variable Y')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Covarianza negativa  
x_neg = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y_neg = np.array([9, 8, 7, 6, 5, 4, 3, 2]) + np.random.normal(0, 0.5, 8)
axes[1].scatter(x_neg, y_neg, s=100, alpha=0.7, color='#c2185b', edgecolors='black', linewidth=1.5)
axes[1].axhline(np.mean(y_neg), color='red', linestyle='--', alpha=0.6)
axes[1].axvline(np.mean(x_neg), color='blue', linestyle='--', alpha=0.6)
axes[1].set_title('Covarianza Negativa\n(Sxy < 0)', fontweight='bold')
axes[1].set_xlabel('Variable X')
axes[1].set_ylabel('Variable Y')
axes[1].grid(True, alpha=0.3)

# Covarianza cercana a cero
x_zero = np.random.rand(20) * 10
y_zero = np.random.rand(20) * 10
axes[2].scatter(x_zero, y_zero, s=100, alpha=0.7, color='#388e3c', edgecolors='black', linewidth=1.5)
axes[2].axhline(np.mean(y_zero), color='red', linestyle='--', alpha=0.6)
axes[2].axvline(np.mean(x_zero), color='blue', linestyle='--', alpha=0.6)
axes[2].set_title('Covarianza ≈ 0\n(Sin relación lineal)', fontweight='bold')
axes[2].set_xlabel('Variable X')
axes[2].set_ylabel('Variable Y')
axes[2].grid(True, alpha=0.3)

for ax in axes:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('graficos/s3_tipos_covarianza.svg', format='svg', dpi=150)
print("✓ S3 Gráfico 1: tipos_covarianza.svg")

# Gráfico 2: Datos de precio pescado Vigo
precios = []
volumenes = []
with open('datos/precio_pescado_puerto_vigo.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        precios.append(float(row['Precio_€_kg']))
        volumenes.append(float(row['Volumen_Toneladas']))

fig, ax = plt.subplots(figsize=(10, 7))
ax.scatter(volumenes, precios, s=120, alpha=0.7, color='#2a5298', edgecolors='black', linewidth=1.5)
ax.set_xlabel('Volumen de Capturas (Toneladas)', fontsize=12, fontweight='bold')
ax.set_ylabel('Precio del Pescado (€/kg)', fontsize=12, fontweight='bold')
ax.set_title('Relación entre Volumen de Capturas y Precio\nPuerto de Vigo (8 semanas)', fontsize=13, fontweight='bold')
ax.grid(True, alpha=0.3, linestyle='--')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('graficos/s3_precio_volumen_pescado_vigo.svg', format='svg', dpi=150)
print("✓ S3 Gráfico 2: precio_volumen_pescado_vigo.svg")

# ============================================================================
# SESIÓN 4: CORRELACIÓN DE PEARSON
# ============================================================================

# Gráfico: Diferentes valores de r
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

valores_r = [0.95, 0.70, 0.30, -0.30, -0.70, -0.95]
titulos = ['r = 0.95\n(Muy fuerte positiva)', 'r = 0.70\n(Fuerte positiva)', 'r = 0.30\n(Débil positiva)',
           'r = -0.30\n(Débil negativa)', 'r = -0.70\n(Fuerte negativa)', 'r = -0.95\n(Muy fuerte negativa)']

for i, (r, titulo) in enumerate(zip(valores_r, titulos)):
    n = 50
    x = np.random.randn(n)
    y = r * x + np.sqrt(1 - r**2) * np.random.randn(n)
    
    axes[i].scatter(x, y, s=60, alpha=0.6, color='#2a5298' if r > 0 else '#c2185b', edgecolors='black', linewidth=0.8)
    axes[i].set_title(titulo, fontweight='bold')
    axes[i].grid(True, alpha=0.3)
    axes[i].spines['top'].set_visible(False)
    axes[i].spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('graficos/s4_valores_correlacion.svg', format='svg', dpi=150)
print("✓ S4 Gráfico: valores_correlacion.svg")

# ============================================================================
# SESIÓN 5: REGRESIÓN LINEAL
# ============================================================================

# Leer datos de viviendas Vigo
distancias = []
precios = []
barrios = []
with open('datos/precio_viviendas_vigo.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        barrios.append(row['Barrio'])
        distancias.append(float(row['Distancia_km']))
        precios.append(float(row['Precio_€_m2']))

fig, ax = plt.subplots(figsize=(11, 8))
ax.scatter(distancias, precios, s=150, alpha=0.7, color='#2a5298', edgecolors='black', linewidth=1.5)

# Añadir etiquetas de barrios
for i, barrio in enumerate(barrios):
    ax.annotate(barrio, (distancias[i], precios[i]), xytext=(5, 5), textcoords='offset points', fontsize=9)

# Calcular y graficar recta de regresión
x_arr = np.array(distancias)
y_arr = np.array(precios)
m, b = np.polyfit(x_arr, y_arr, 1)
x_linea = np.linspace(0, max(distancias) + 1, 100)
y_linea = m * x_linea + b

ax.plot(x_linea, y_linea, 'r--', linewidth=2, label=f'y = {m:.2f}x + {b:.2f}')

ax.set_xlabel('Distancia al Centro de Vigo (km)', fontsize=12, fontweight='bold')
ax.set_ylabel('Precio de Vivienda (€/m²)', fontsize=12, fontweight='bold')
ax.set_title('Regresión Lineal: Precio de Vivienda vs Distancia al Centro\nBarrios de Vigo', fontsize=13, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3, linestyle='--')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('graficos/s5_regresion_viviendas_vigo.svg', format='svg', dpi=150)
print("✓ S5 Gráfico: regresion_viviendas_vigo.svg")

# ============================================================================
# SESIÓN 6: COEFICIENTE DE DETERMINACIÓN
# ============================================================================

# Gráfico: Comparación de R² diferentes
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

r2_values = [0.25, 0.65, 0.92]
titulos = ['R² = 0.25\n(Ajuste pobre)', 'R² = 0.65\n(Ajuste moderado)', 'R² = 0.92\n(Ajuste excelente)']

for i, (r2, titulo) in enumerate(zip(r2_values, titulos)):
    n = 40
    x = np.linspace(0, 10, n)
    r = np.sqrt(r2)
    y = 2*x + 5 + np.random.normal(0, 10*(1-r), n)
    
    axes[i].scatter(x, y, s=60, alpha=0.6, color='#2a5298', edgecolors='black', linewidth=0.8)
    m, b = np.polyfit(x, y, 1)
    axes[i].plot(x, m*x + b, 'r--', linewidth=2)
    axes[i].set_title(titulo, fontweight='bold')
    axes[i].set_xlabel('Variable X')
    axes[i].set_ylabel('Variable Y')
    axes[i].grid(True, alpha=0.3)
    axes[i].spines['top'].set_visible(False)
    axes[i].spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('graficos/s6_comparacion_r2.svg', format='svg', dpi=150)
print("✓ S6 Gráfico: comparacion_r2.svg")

# ============================================================================
# SESIÓN 7: REGRESIÓN CUADRÁTICA
# ============================================================================

# Leer datos de pasajeros puerto
meses_num = []
pasajeros = []
with open('datos/pasajeros_puerto_vigo.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        meses_num.append(int(row['Numero_Mes']))
        pasajeros.append(float(row['Pasajeros_Miles']))

fig, ax = plt.subplots(figsize=(12, 7))

# Datos
x_arr = np.array(meses_num)
y_arr = np.array(pasajeros)

# Modelo lineal
m_lin, b_lin = np.polyfit(x_arr, y_arr, 1)
y_lin = m_lin * x_arr + b_lin

# Modelo cuadrático
coef_cuad = np.polyfit(x_arr, y_arr, 2)
y_cuad = np.polyval(coef_cuad, x_arr)

# Graficar
ax.scatter(x_arr, y_arr, s=80, alpha=0.7, color='#2a5298', edgecolors='black', linewidth=1.5, label='Datos reales', zorder=3)
ax.plot(x_arr, y_lin, 'r--', linewidth=2, label='Modelo lineal', alpha=0.7)
ax.plot(x_arr, y_cuad, 'g-', linewidth=2.5, label='Modelo cuadrático', alpha=0.8)

ax.set_xlabel('Mes (ordinal)', fontsize=12, fontweight='bold')
ax.set_ylabel('Pasajeros (miles)', fontsize=12, fontweight='bold')
ax.set_title('Comparación Regresión Lineal vs Cuadrática\nPasajeros Puerto de Vigo (24 meses)', fontsize=13, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3, linestyle='--')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('graficos/s7_lineal_vs_cuadratica.svg', format='svg', dpi=150)
print("✓ S7 Gráfico: lineal_vs_cuadratica.svg")

# ============================================================================
# SESIÓN 8: CORRELACIÓN VS CAUSALIDAD
# ============================================================================

# Gráfico: Ejemplos de correlaciones espurias
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Ejemplo 1: Helados y ahogamientos (variable confusora: temperatura)
meses = np.arange(1, 13)
temperatura = 15 + 7*np.sin((meses - 4) * np.pi / 6)
helados = temperatura * 20 + np.random.normal(0, 10, 12)
ahogados = temperatura * 0.5 + np.random.normal(0, 1, 12)

axes[0, 0].scatter(helados, ahogados, s=100, c=temperatura, cmap='YlOrRd', edgecolors='black', linewidth=1.5)
axes[0, 0].set_xlabel('Venta de Helados', fontsize=11, fontweight='bold')
axes[0, 0].set_ylabel('Nº de Ahogamientos', fontsize=11, fontweight='bold')
axes[0, 0].set_title('Correlación Espuria: Helados vs Ahogamientos\n(Variable confusora: Temperatura)', fontweight='bold')
axes[0, 0].grid(True, alpha=0.3)

# Ejemplo 2: Policía y delitos (causalidad inversa)
delitos = np.array([20, 35, 50, 70, 90, 110, 130])
policia = delitos * 0.8 + np.random.normal(0, 5, 7)

axes[0, 1].scatter(policia, delitos, s=100, alpha=0.7, color='#2a5298', edgecolors='black', linewidth=1.5)
axes[0, 1].set_xlabel('Nº de Policías', fontsize=11, fontweight='bold')
axes[0, 1].set_ylabel('Nº de Delitos', fontsize=11, fontweight='bold')
axes[0, 1].set_title('Causalidad Inversa: Más delitos → Más policía\n(No al revés)', fontweight='bold')
axes[0, 1].grid(True, alpha=0.3)

# Ejemplo 3: Relación genuina (educación-salario)
educacion = np.array([8, 10, 12, 14, 16, 18, 20])
salario = educacion * 2.5 + np.random.normal(0, 2, 7)

axes[1, 0].scatter(educacion, salario, s=100, alpha=0.7, color='#388e3c', edgecolors='black', linewidth=1.5)
axes[1, 0].set_xlabel('Años de Educación', fontsize=11, fontweight='bold')
axes[1, 0].set_ylabel('Salario (miles €)', fontsize=11, fontweight='bold')
axes[1, 0].set_title('Relación Causal Plausible\n(Educación → Salario)', fontweight='bold')
axes[1, 0].grid(True, alpha=0.3)

# Ejemplo 4: No lineal (U invertida)
x_nolineal = np.linspace(0, 10, 30)
y_nolineal = -0.5*(x_nolineal - 5)**2 + 15 + np.random.normal(0, 1, 30)

axes[1, 1].scatter(x_nolineal, y_nolineal, s=100, alpha=0.7, color='#f9a825', edgecolors='black', linewidth=1.5)
axes[1, 1].set_xlabel('Horas de Trabajo Diarias', fontsize=11, fontweight='bold')
axes[1, 1].set_ylabel('Productividad', fontsize=11, fontweight='bold')
axes[1, 1].set_title('Relación No Lineal\n(r ≈ 0 pero hay relación)', fontweight='bold')
axes[1, 1].grid(True, alpha=0.3)

for ax in axes.flat:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('graficos/s8_correlacion_vs_causalidad.svg', format='svg', dpi=150)
print("✓ S8 Gráfico: correlacion_vs_causalidad.svg")

plt.close('all')
print("\n✅ Todos los gráficos de las Sesiones 3-8 generados exitosamente")
