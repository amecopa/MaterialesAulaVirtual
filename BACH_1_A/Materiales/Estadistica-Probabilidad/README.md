# Estadística y Probabilidad - 1º Bachillerato MACS

## 📁 Estructura de Materiales - Bloque I: Estadística Bidimensional

### Sesiones Disponibles (1-8)

| Sesión | Tema | Archivo HTML | Datos Necesarios | Gráficos |
|--------|------|--------------|------------------|----------|
| **S1** | Variables Bidimensionales | `S1_Variables_Bidimensionales.html` | `temperatura_turistas_cies.csv` | ✅ 3 gráficos SVG |
| **S2** | Distribuciones Marginales y Condicionadas | `S2_Distribuciones_Marginales.html` | `salario_educacion.csv` | ✅ 4 gráficos SVG |
| **S3** | Covarianza y Dependencia | `S3_Covarianza_Dependencia.html` | `precio_pescado_puerto_vigo.csv` | ⏳ Pendiente |
| **S4** | Correlación de Pearson | `S4_Correlacion_Pearson.html` | Datos inline | ⏳ Pendiente |
| **S5** | Regresión Lineal | `S5_Regresion_Lineal.html` | `precio_viviendas_vigo.csv` | ⏳ Pendiente |
| **S6** | Coeficiente de Determinación | `S6_Coeficiente_Determinacion.html` | `barcos_capturas_vigo.csv` | ⏳ Pendiente |
| **S7** | Regresión Cuadrática | `S7_Regresion_Cuadratica.html` | `pasajeros_puerto_vigo.csv` | ⏳ Pendiente |
| **S8** | Correlación vs Causalidad | `S8_Correlacion_Causalidad.html` | Casos de estudio | ⏳ Pendiente |

### 📊 Datasets Disponibles

Todos los archivos CSV están en la carpeta `datos/`:

```
datos/
├── temperatura_turistas_cies.csv        (12 meses - Temperatura vs Turistas)
├── salario_educacion.csv                 (18 trabajadores - Salario vs Nivel educativo)
├── precio_pescado_puerto_vigo.csv        (8 semanas - Precio vs Volumen capturas)
├── precio_viviendas_vigo.csv             (8 barrios - Distancia vs Precio/m²)
├── barcos_capturas_vigo.csv              (12 meses - Barcos activos vs Toneladas)
└── pasajeros_puerto_vigo.csv             (24 meses - Datos cíclicos pasajeros)
```

### 🎨 Gráficos Generados

Todos los gráficos SVG se generan en `graficos/` ejecutando los scripts Python:

```bash
# Generar todos los gráficos de una vez
python3 generar_graficos_s1.py
python3 generar_graficos_s2.py
python3 generar_graficos_s3.py
# ... (continuar con s4-s8)
```

**Gráficos disponibles:**
- `s1_temperatura_turistas_cies.svg`
- `s1_tipos_correlacion.svg`
- `s1_horas_estudio_notas.svg`
- `s2_marginal_vs_condicionada.svg`
- `s2_medias_condicionadas_salario.svg`
- `s2_tabla_contingencia_edad_vivienda.svg`
- `s2_distribuciones_condicionadas_apiladas.svg`

### 🚀 Cómo Usar los Materiales

#### Opción 1: Abrir directamente en navegador
```bash
open S1_Variables_Bidimensionales.html
# O arrastra el archivo al navegador
```

#### Opción 2: Usar Live Server en VS Code
1. Instalar extensión "Live Server"
2. Clic derecho en el archivo HTML > "Open with Live Server"
3. Se abre automáticamente en `http://localhost:5500`

#### Opción 3: Servir vía Python
```bash
# Desde la carpeta Estadistica-Probabilidad
python3 -m http.server 8000
# Abrir http://localhost:8000 en el navegador
```

### 📋 Características de Cada Sesión HTML

✅ **Estructura completa** según la planificación:
- Objetivos de la sesión
- Contenidos teóricos con MathJax
- Bloque 1: Refuerzo (ejercicios de repaso)
- Bloque 2: Consolidación (ejercicios guiados)
- Bloque 3: Afianzamiento (práctica autónoma)
- Bloque 4: Ampliación (extensiones y debate)

✅ **Soluciones desplegables** con `<details>`:
- Todos los ejercicios tienen solución
- Desarrollo paso a paso con justificación matemática
- Cálculos intermedios detallados

✅ **Diseño responsive** con CSS moderno:
- Bloques coloreados por tipo (Refuerzo: amarillo, Consolidación: azul, etc.)
- Tipografía: Georgia serif para legibilidad
- Máximo 860px de ancho para lectura óptima
- Compatible con móviles y tablets

✅ **Datos contextualizados a Vigo**:
- Islas Cíes, Puerto de Vigo, Vitrasa
- Precios de vivienda por barrios
- Datos del sector pesquero

### 🔧 Requisitos Técnicos

**Para visualizar HTML:**
- Navegador moderno (Chrome, Firefox, Safari, Edge)
- Conexión a internet (carga MathJax desde CDN)

**Para ejecutar scripts Python:**
```bash
# Instalar dependencias (si hace falta)
pip3 install matplotlib numpy

# Ejecutar scripts
python3 generar_graficos_s1.py
```

### 📚 Próximos Bloques

Este README cubre el **Bloque I: Estadística Bidimensional (Sesiones 1-8)**.

Próximamente:
- **Bloque II:** Probabilidad (Sesiones 9-14)
- **Bloque III:** Inferencia Estadística (Sesiones 15-18)

### 📞 Soporte

Para dudas sobre los materiales:
- Consultar con el profesor en clase
- Revisar la planificación didáctica en `../../Planificaciones/`
- Comprobar errores en el navegador (F12 > Consola)

---

**Generado:** 19 de abril de 2026  
**Nivel:** 1º Bachillerato MACS  
**Bloque:** Estadística y Probabilidad  
**IES Teis - Vigo**
