# Materiales Didácticos: Derivadas

## Matemáticas Aplicadas a las Ciencias Sociales I - 1º Bachillerato

**IES de Teis - Vigo**  
**Curso académico 2024-2025**

---

## 📂 Estructura de la Unidad

Esta carpeta contiene los materiales didácticos completos para la unidad de **Derivadas**, diseñada según el currículo LOMLOE de Galicia para MACS I.

```
Derivadas/
├── S1_tasa_variacion.html              # Sesión 1: TVM e Instantánea
├── S2_reglas_derivacion.html           # Sesión 2: Reglas de derivación
├── S3_crecimiento_curvatura.html       # Sesión 3: Análisis de funciones
├── S4_optimizacion.html                # Sesión 4: Problemas de optimización
├── generar_graficos.py                 # Script para generar visualizaciones
├── imgs/                               # Gráficas generadas
│   ├── s1_tvm_tvi.png
│   ├── s1_peinador.png
│   ├── s3_crecimiento_curvatura.png
│   └── s3_grafica_analisis.png
└── README.md                           # Este archivo
```

---

## 📖 Descripción de las Sesiones

### Sesión 1: El ritmo del cambio en la Ría
**Objetivo:** Comprender la Tasa de Variación Media (TVM) e Instantánea (TVI) a través de situaciones reales del entorno de Vigo.

**Contenidos:**
- Repaso de pendiente de una recta
- Tasa de Variación Media (TVM)
- Tasa de Variación Instantánea (TVI) y concepto de derivada
- Aplicaciones: exportaciones del Puerto de Vigo, precio del gasoil, aeropuerto de Peinador

**Duración:** 50 min (15' refuerzo + 15' consolidación + 20' ampliación)

---

### Sesión 2: La regla del juego (Reglas de Derivación)
**Objetivo:** Dominar la mecánica de derivación de funciones elementales y compuestas mediante reglas algebraicas.

**Contenidos:**
- Reglas básicas: constante, potencia, exponencial, logaritmo
- Regla de la suma, producto, cociente y cadena
- Aplicaciones a costes, beneficios, interés compuesto y consumo eléctrico

**Duración:** 40 min (10' refuerzo + 15' consolidación + 15' ampliación)

---

### Sesión 3: El pico de la campaña (Crecimiento y Curvatura)
**Objetivo:** Utilizar la primera y segunda derivada para describir el comportamiento completo de una función.

**Contenidos:**
- Primera derivada: crecimiento, decrecimiento y puntos críticos
- Clasificación de extremos: máximos y mínimos
- Segunda derivada: concavidad, convexidad y puntos de inflexión
- Aplicaciones: ocupación hotelera, demanda de pescado, productividad en astilleros

**Duración:** 40 min (10' refuerzo + 15' consolidación + 15' ampliación)

---

### Sesión 4: Optimización en la industria de Vigo
**Objetivo:** Resolver problemas de optimización contextualizados en el entorno socioeconómico de Vigo.

**Contenidos:**
- Metodología de resolución de problemas de optimización
- Problemas geométricos: área y perímetro con restricciones
- Problemas económicos: maximización de beneficios y minimización de costes
- Aplicaciones: embalaje de exportación, rutas de transporte, precio óptimo de entradas

**Duración:** 40 min (10' refuerzo + 15' consolidación + 15' ampliación)

---

## 🎯 Criterios de Evaluación

- **CE 1.3:** Resolución de problemas en situaciones diversas estableciendo conexiones con el mundo real
- **CE 1.4:** Empleo de estrategias y herramientas digitales en problemas de ciencias sociales

---

## 🛠️ Tecnologías Utilizadas

### HTML + MathJax
- Los archivos HTML son **autocontenidos** (se pueden abrir directamente en cualquier navegador)
- Fórmulas matemáticas renderizadas con **MathJax 3** (CDN)
- Diseño responsive y accesible
- Soluciones desplegables con `<details>` para facilitar la autoevaluación

### Python + Matplotlib
- Visualizaciones generadas con matplotlib y numpy
- Script ejecutable: `python3 generar_graficos.py`
- Gráficas en alta resolución (150 dpi) formato PNG

---

## 📊 Gráficas Incluidas

| Archivo | Descripción |
|---------|-------------|
| `s1_tvm_tvi.png` | Comparación visual entre TVM (recta secante) y TVI (recta tangente) |
| `s1_peinador.png` | Evolución simulada de pasajeros en el aeropuerto de Peinador |
| `s3_crecimiento_curvatura.png` | Análisis completo de crecimiento y curvatura con puntos críticos |
| `s3_grafica_analisis.png` | Función genérica para ejercicios de interpretación gráfica |

---

## 📝 Características de los Ejercicios

Cada sesión incluye:
- **Ejercicios de Refuerzo:** Consolidación de saberes previos y conceptos básicos
- **Ejercicios de Consolidación:** Aplicación directa de los contenidos de la sesión
- **Ejercicios de Ampliación:** Problemas de mayor complejidad o síntesis
- **Trabajo Activo:** Actividades contextualizadas para trabajo individual o en grupo
- **Ejercicios para Casa:** Práctica adicional con soluciones incluidas

**Total:** Más de 50 ejercicios resueltos paso a paso.

---

## 🌍 Contextualización

Todos los problemas están contextualizados en el entorno socioeconómico de **Vigo y su área metropolitana**:
- Puerto de Vigo (exportaciones, flota pesquera)
- Aeropuerto de Peinador
- Stellantis (industria automoción)
- Parque de Castrelos
- Industria conservera y textil
- Luces de Navidad de Vigo

---

## 🚀 Cómo Utilizar estos Materiales

### Para el alumnado:
1. Abre los archivos HTML directamente en tu navegador (Chrome, Firefox, Edge, Safari)
2. Lee la teoría con atención
3. Intenta resolver los ejercicios antes de desplegar las soluciones
4. Consulta las gráficas para visualizar los conceptos

### Para el profesorado:
1. Los HTML se pueden **proyectar directamente** en el aula
2. Se pueden **publicar en Moodle, Google Classroom o similar**
3. El código Python permite **regenerar o personalizar** las gráficas
4. Los archivos HTML se pueden **imprimir** manteniendo el formato

### Publicación web:
- Compatible con **GitHub Pages**
- Compatible con **VS Code Live Server**
- Sin dependencias externas (excepto MathJax CDN)

---

## 📦 Regenerar las Gráficas

Si deseas modificar o regenerar las gráficas:

```bash
# Asegúrate de tener Python 3 y las dependencias instaladas
pip install matplotlib numpy

# Ejecuta el script
python3 generar_graficos.py
```

Las gráficas se guardarán automáticamente en la carpeta `imgs/`.

---

## 📚 Saberes Básicos del Currículo

Esta unidad desarrolla los siguientes saberes básicos del bloque **D. Sentido del Análisis**:

- **D.3.** Tasa de variación media e instantánea
- **D.4.** Derivada de una función en un punto. Aplicación al estudio de fenómenos económicos y sociales
- **D.5.** Función derivada. Reglas de derivación de las operaciones elementales con funciones
- **D.6.** Aplicaciones del estudio de la derivada al estudio de funciones y a la resolución de problemas de optimización

---

## 📄 Licencia y Atribución

**Autor:** IES de Teis - Departamento de Matemáticas  
**Curso:** 2024-2025  
**Nivel:** 1º Bachillerato - Matemáticas Aplicadas a las Ciencias Sociales I

Estos materiales están diseñados con fines educativos. Se permite su uso, modificación y distribución para actividades docentes sin ánimo de lucro.

---

## ✉️ Contacto y Mejoras

Si encuentras errores o tienes sugerencias para mejorar estos materiales, por favor contacta con el Departamento de Matemáticas del IES de Teis.

---

**Última actualización:** 10 de abril de 2026
