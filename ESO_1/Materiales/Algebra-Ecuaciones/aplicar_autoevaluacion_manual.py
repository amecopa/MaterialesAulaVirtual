#!/usr/bin/env python3
"""
Script manual para S3, S6, S7 con escapes correctos
"""

import os

def procesar_s3():
    archivo = 'S3_monomios.html'
    
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Reemplazar autoevaluación antigua
    autoevaluacion_vieja = """      <div class="panel panel-checkpoint">
        <h3>Autoevaluación</h3>
        <p>Responde honestamente:</p>
        <ol>
          <li>¿Puedo identificar el coeficiente y la parte literal de un monomio? ___</li>
          <li>¿Sé cuándo dos monomios son semejantes? ___</li>
          <li>¿Puedo sumar \\( 5x + 3x \\) sin dudar? ___</li>
          <li>¿Entiendo por qué \\( 2x + 3y \\) no se puede simplificar? ___</li>
        </ol>
      </div>"""
    
    autoevaluacion_nueva = """      <div class="panel panel-checkpoint">
        <h3>Autoevaluación Interactiva</h3>
        <p style="margin-bottom: calc(var(--spacing-unit) * 6);">Responde honestamente (esto es solo para ti, no se guarda ningún dato):</p>
        
        <form id="autoevaluacion-form" style="margin-bottom: calc(var(--spacing-unit) * 4);">
          <div class="pregunta-autoevaluacion">
            <p class="pregunta-texto"><strong>1.</strong> ¿Identificas correctamente el coeficiente y la parte literal de un monomio?</p>
            <div class="opciones-radio">
              <label class="radio-label">
                <input type="radio" name="q1" value="si" required>
                <span>✓ Sí</span>
              </label>
              <label class="radio-label">
                <input type="radio" name="q1" value="no">
                <span>✗ No</span>
              </label>
              <label class="radio-label">
                <input type="radio" name="q1" value="duda">
                <span>? Tengo dudas</span>
              </label>
            </div>
          </div>

          <div class="pregunta-autoevaluacion">
            <p class="pregunta-texto"><strong>2.</strong> ¿Sabes cuándo dos monomios son semejantes?</p>
            <div class="opciones-radio">
              <label class="radio-label">
                <input type="radio" name="q2" value="si" required>
                <span>✓ Sí</span>
              </label>
              <label class="radio-label">
                <input type="radio" name="q2" value="no">
                <span>✗ No</span>
              </label>
              <label class="radio-label">
                <input type="radio" name="q2" value="duda">
                <span>? Tengo dudas</span>
              </label>
            </div>
          </div>

          <div class="pregunta-autoevaluacion">
            <p class="pregunta-texto"><strong>3.</strong> ¿Puedes sumar y restar monomios semejantes?</p>
            <div class="opciones-radio">
              <label class="radio-label">
                <input type="radio" name="q3" value="si" required>
                <span>✓ Sí</span>
              </label>
              <label class="radio-label">
                <input type="radio" name="q3" value="no">
                <span>✗ No</span>
              </label>
              <label class="radio-label">
                <input type="radio" name="q3" value="duda">
                <span>? Tengo dudas</span>
              </label>
            </div>
          </div>

          <div class="pregunta-autoevaluacion">
            <p class="pregunta-texto"><strong>4.</strong> ¿Multiplicas correctamente monomios?</p>
            <div class="opciones-radio">
              <label class="radio-label">
                <input type="radio" name="q4" value="si" required>
                <span>✓ Sí</span>
              </label>
              <label class="radio-label">
                <input type="radio" name="q4" value="no">
                <span>✗ No</span>
              </label>
              <label class="radio-label">
                <input type="radio" name="q4" value="duda">
                <span>? Tengo dudas</span>
              </label>
            </div>
          </div>

          <button type="submit" class="btn-autoevaluacion">📊 Ver mi resultado</button>
        </form>

        <div id="feedback-autoevaluacion" style="display: none;"></div>
      </div>"""
    
    if autoevaluacion_vieja in contenido:
        contenido = contenido.replace(autoevaluacion_vieja, autoevaluacion_nueva)
        print("✓ Reemplazo de autoevaluación en S3 completado")
    else:
        print("✗ No se encontró la sección de autoevaluación en S3")
        return False
    
    # Añadir JavaScript antes de cierre de script
    js_code = """
    // Autoevaluación Interactiva - S3 Monomios
    const feedbackData = {
      q1: {
        si: { correcto: true, mensaje: "¡Perfecto! En \\\\(5x^2\\\\), el coeficiente es 5 y la parte literal es \\\\(x^2\\\\)." },
        no: { correcto: false, mensaje: "El coeficiente es el número, la parte literal son las letras con sus exponentes. Revisa sección 01." },
        duda: { correcto: false, mensaje: "Ejemplo: en \\\\(-3xy^2\\\\), coeficiente = -3, parte lateral = \\\\(xy^2\\\\). Practica en sección 03." }
      },
      q2: {
        si: { correcto: true, mensaje: "¡Excelente! Son semejantes si tienen la misma parte literal (mismas letras con mismos exponentes)." },
        no: { correcto: false, mensaje: "Monomios semejantes = misma parte literal. \\\\(3x^2\\\\) y \\\\(5x^2\\\\) SÍ. \\\\(3x^2\\\\) y \\\\(3x\\\\) NO. Revisa sección 02." },
        duda: { correcto: false, mensaje: "¿Son semejantes \\\\(2xy\\\\) y \\\\(5xy\\\\)? SÍ (misma parte literal). ¿Y \\\\(2xy\\\\) y \\\\(2x^2\\\\)? NO." }
      },
      q3: {
        si: { correcto: true, mensaje: "¡Muy bien! Sumas/restas los coeficientes y mantienes la parte literal: \\\\(3x + 5x = 8x\\\\)." },
        no: { correcto: false, mensaje: "Solo se pueden sumar/restar monomios semejantes. Suma coeficientes. Revisa sección 05." },
        duda: { correcto: false, mensaje: "Ejemplo: \\\\(7x^2 - 3x^2 = 4x^2\\\\) (restas 7-3=4). La parte literal no cambia." }
      },
      q4: {
        si: { correcto: true, mensaje: "¡Genial! Multiplicas coeficientes y sumas exponentes: \\\\(2x \\\\cdot 3x^2 = 6x^3\\\\)." },
        no: { correcto: false, mensaje: "Multiplica coeficientes, suma exponentes de la misma letra. Revisa sección 06." },
        duda: { correcto: false, mensaje: "Ejemplo: \\\\(4x \\\\cdot 2x = (4 \\\\cdot 2)(x \\\\cdot x) = 8x^2\\\\). Coeficientes: 4×2=8, exponentes: 1+1=2." }
      }
    };

    const autoevalForm = document.getElementById('autoevaluacion-form');
    if (autoevalForm) {
      autoevalForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const respuestas = {
          q1: document.querySelector('input[name="q1"]:checked')?.value,
          q2: document.querySelector('input[name="q2"]:checked')?.value,
          q3: document.querySelector('input[name="q3"]:checked')?.value,
          q4: document.querySelector('input[name="q4"]:checked')?.value
        };

        if (!respuestas.q1 || !respuestas.q2 || !respuestas.q3 || !respuestas.q4) {
          alert('⚠️ Por favor, responde todas las preguntas antes de enviar.');
          return;
        }

        let correctas = 0;
        let mensajes = [];
        
        for (let pregunta in respuestas) {
          const respuesta = respuestas[pregunta];
          const feedback = feedbackData[pregunta][respuesta];
          
          if (feedback.correcto) {
            correctas++;
          }
          mensajes.push(`<li><strong>Pregunta ${pregunta.slice(1)}:</strong> ${feedback.mensaje}</li>`);
        }

        const feedbackDiv = document.getElementById('feedback-autoevaluacion');
        let claseEstilo, titulo, emoji, mensaje;

        if (correctas === 4) {
          claseEstilo = 'feedback-excelente';
          titulo = '🎉 ¡EXCELENTE TRABAJO!';
          emoji = '⭐⭐⭐⭐';
          mensaje = '<p class="feedback-mensaje">¡Felicidades! Has comprendido todos los conceptos clave de esta sesión. Estás listo para avanzar al siguiente tema.</p>';
        } else if (correctas >= 2) {
          claseEstilo = 'feedback-bien';
          titulo = '👍 ¡BUEN TRABAJO!';
          emoji = '⭐⭐⭐';
          mensaje = '<p class="feedback-mensaje">Vas por buen camino. Hay algunas áreas que necesitan refuerzo. Revisa las secciones indicadas abajo y vuelve a intentarlo.</p>';
        } else {
          claseEstilo = 'feedback-mejorar';
          titulo = '💪 ¡SIGUE INTENTÁNDOLO!';
          emoji = '⭐⭐';
          mensaje = '<p class="feedback-mensaje">No te desanimes. El álgebra requiere práctica. Lee de nuevo el material, especialmente las secciones indicadas, y vuelve a hacer la autoevaluación.</p>';
        }

        feedbackDiv.className = claseEstilo;
        feedbackDiv.innerHTML = `
          <div class="feedback-titulo">${titulo}</div>
          <div class="feedback-puntuacion">${emoji}</div>
          <div style="text-align: center; font-size: 1.3rem; font-weight: 700; margin-bottom: calc(var(--spacing-unit) * 4);">
            ${correctas} de 4 respuestas positivas
          </div>
          ${mensaje}
          <div class="feedback-consejo">
            <strong>📋 Detalles de tu autoevaluación:</strong>
            <ul style="margin-top: calc(var(--spacing-unit) * 3);">
              ${mensajes.join('')}
            </ul>
          </div>
          ${correctas < 4 ? `
            <div class="feedback-consejo" style="margin-top: calc(var(--spacing-unit) * 4); border-left-color: #3b82f6;">
              <strong>💡 Consejo:</strong>
              <p style="margin-top: calc(var(--spacing-unit) * 2);">
                Revisa las secciones indicadas arriba. No hay prisa: el aprendizaje toma tiempo. 
                Cuando te sientas preparado, vuelve a hacer esta autoevaluación.
              </p>
            </div>
          ` : ''}}
        `;
        
        feedbackDiv.style.display = 'block';
        
        if (typeof Math Jax !== 'undefined') {
          MathJax.typesetPromise([feedbackDiv]).catch((err) => console.log('MathJax error:', err));
        }

        feedbackDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      });
    }"""
    
    # Buscar donde insertar JS (antes de cierre de script)
    if '  </script>' in contenido:
        contenido = contenido.replace('  </script>', js_code + '\n  </script>')
        print("✓ JavaScript añadido a S3")
    else:
        print("✗ No se encontró el cierre de script en S3")
        return False
    
    with open(archivo, 'w', encoding='utf-8') as f:
        f.write(contenido)
    
    return True


# Ejecutar
if __name__ == '__main__':
    print("Procesando S3_monomios.html...")
    if procesar_s3():
        print("✅ S3 procesado exitosamente")
    else:
        print("❌ Error procesando S3")
