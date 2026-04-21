"""
Script para generar las sesiones HTML restantes (S3-S8) del Bloque I
Genera archivos HTML completos con estructura, teoría, ejercicios y soluciones
"""

# Plantilla HTML base
def generar_html_sesion(numero, titulo, objetivos, contenido_teorico, bloques_ejercicios, resumen, proxima_sesion, graficos):
    """
    Genera HTML completo para una sesión
    """
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sesión {numero}: {titulo}</title>
  <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
  <style>
    body {{ font-family: Georgia, serif; max-width: 860px; margin: 2rem auto; padding: 0 1.2rem; line-height: 1.7; color: #222; }}
    h1 {{ color: #1a3a6e; border-bottom: 2px solid #1a3a6e; padding-bottom: .4rem; }}
    h2 {{ color: #2a5298; margin-top: 2rem; }}
    h3 {{ color: #3a6bc4; }}
    .objetivos {{ background: #e8f4f8; border-left: 4px solid #2a5298; padding: 1rem 1.5rem; margin: 1.5rem 0; border-radius: 0 6px 6px 0; }}
    .bloque-refuerzo {{ background: #fff9e6; border-left: 4px solid #f9a825; padding: 1rem 1.5rem; margin: 1.5rem 0; border-radius: 0 6px 6px 0; }}
    .bloque-consolidacion {{ background: #f0f4fc; border-left: 4px solid #2a5298; padding: 1rem 1.5rem; margin: 1.5rem 0; border-radius: 0 6px 6px 0; }}
    .bloque-afianzamiento {{ background: #e8f5e9; border-left: 4px solid #388e3c; padding: 1rem 1.5rem; margin: 1.5rem 0; border-radius: 0 6px 6px 0; }}
    .bloque-ampliacion {{ background: #fce4ec; border-left: 4px solid #c2185b; padding: 1rem 1.5rem; margin: 1.5rem 0; border-radius: 0 6px 6px 0; }}
    .solucion  {{ background: #f4fcf0; border-left: 4px solid #2a8a2a; padding: 1rem 1.5rem; margin: .8rem 0; border-radius: 0 6px 6px 0; }}
    .ejemplo {{ background: #f9f9f9; border: 1px solid #ddd; padding: 1rem; margin: 1rem 0; border-radius: 4px; }}
    .definicion {{ background: #fffbea; border-left: 3px solid #f9a825; padding: 0.8rem 1.2rem; margin: 1rem 0; font-style: italic; }}
    ol li, ul li {{ margin-bottom: .5rem; }}
    img {{ max-width: 100%; display: block; margin: 1rem auto; border: 1px solid #ddd; border-radius: 4px; }}
    table {{ border-collapse: collapse; width: 100%; margin: 1rem 0; }}
    th, td {{ border: 1px solid #333; padding: 0.6rem; text-align: center; }}
    th {{ background-color: #2a5298; color: white; font-weight: bold; }}
    details {{ margin: 1rem 0; }}
    summary {{ cursor: pointer; font-weight: bold; color: #2a5298; padding: 0.5rem; background: #f0f4fc; border-radius: 4px; }}
    summary:hover {{ background: #e0e8f4; }}
    .paso {{ margin: 0.8rem 0; padding-left: 1.5rem; }}
  </style>
</head>
<body>

  <h1>Sesión {numero}: {titulo}</h1>
  
  <div class="objetivos">
    <h3>🎯 Objetivos de la Sesión</h3>
    {objetivos}
  </div>

  <h2>📚 Contenidos Teóricos</h2>
  {contenido_teorico}

  <hr style="margin: 2rem 0;">

  {bloques_ejercicios}

  <hr style="margin: 2rem 0;">

  <h2>📊 Resumen de la Sesión</h2>
  {resumen}

  <h2>📝 Para la Próxima Sesión</h2>
  {proxima_sesion}

  <footer style="margin-top: 3rem; padding-top: 1rem; border-top: 1px solid #ddd; font-size: 0.9rem; color: #666;">
    <p><strong>1º Bachillerato - Matemáticas Aplicadas a las Ciencias Sociales I</strong></p>
    <p>Bloque 4: Sentido Estocástico | Estadística y Probabilidad</p>
    <p>IES Teis - Vigo | Curso 2025-2026</p>
  </footer>

</body>
</html>"""
    return html

# Por falta de espacio, voy a crear las sesiones directamente en archivos individuales
# en lugar de usar este script. Continúo con creación manual optimizada.

print("Script de generación de sesiones preparado")
print("Las sesiones se generarán individualmente para maximizar calidad")
