#!/usr/bin/env python3
"""
Script manual para S6 y S7 con escapes correctos
"""

import os

def procesar_s6():
    archivo = 'S6_ecuaciones_multiplicacion.html'
    
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Reemplazar autoevaluación antigua
    autoevaluacion_vieja = """      <div class="panel panel-checkpoint">
        <h3>Autoevaluación</h3>
        <ol>
          <li>¿Entiendes el concepto principal de esta sesión? ___</li>
          <li>¿Puedes resolver ejercicios básicos sin ayuda? ___</li>
          <li>¿Sabes aplicar esto a problemas reales? ___</li>
          <li>¿Qué parte te resultó más difícil? ___</li>
        </ol>
      </div>"""
    
    autoevaluacion_nueva = """      <div class="panel panel-checkpoint">
        <h3>Autoevaluación Interactiva</h3>
        <p style="margin-bottom: calc(var(--spacing-unit) * 6);">Responde honestamente (esto es solo para ti, no se guarda ningún dato):</p>
        
        <form id="autoevaluacion-form" style="margin-bottom: calc(var(--spacing-unit) * 4);">
          <div class="pregunta-autoevaluacion">
            <p class="pregunta-texto"><strong>1.</strong> ¿Multiplicas correctamente ambos lados de una ecuación?</p>
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
            <p class="pregunta-texto"><strong>2.</strong> ¿Divides correctamente para despejar la incógnita?</p>
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
            <p class="pregunta-texto"><strong>3.</strong> ¿Simplif icas fracciones antes de operar?</p>
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
            <p class="pregunta-texto"><strong>4.</strong> ¿Tienes cuidado con las divisiones por cero?</p>
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
        print("✓ Reemplazo de autoevaluación en S6 completado")
    else:
        print("✗ No se encontró la sección de autoevaluación en S6")
        return False
    
    # Añadir JavaScript antes de cierre de script
    js_code = """
    // Autoevaluación Interactiva - S6 Ecuaciones con Multiplicación/División
    const feedbackData = {
      q1: {
        si: { correcto: true, mensaje: "¡Perfecto! Si multiplicas un lado por 3, debes multiplicar el otro también. La balanza se mantiene equilibrada." },
        no: { correcto: false, mensaje: "Recuerda: lo que haces a un lado, debes hacerlo al otro. Si \\\\(x \\\\div 2 = 5\\\\), multiplica ambos por 2. Revisa sección 02." },
        duda: { correcto: false, mensaje: "Ejemplo: \\\\(\\\\frac{x}{3} = 4\\\\) → multiplica ambos por 3 → \\\\(x = 12\\\\). Practica en sección 03." }
      },
      q2: {
        si: { correcto: true, mensaje: "¡Excelente! Para despejar \\\\(x\\\\) en \\\\(5x = 20\\\\), divides ambos lados entre 5." },
        no: { correcto: false, mensaje: "Si \\\\(3x = 12\\\\), divide ambos lados entre 3: \\\\(x = 4\\\\). Revisa sección 04." },
        duda: { correcto: false, mensaje: "La división es la operación inversa de la multiplicación. Si \\\\(7x = 21\\\\), entonces \\\\(x = 21 \\\\div 7 = 3\\\\)." }
      },
      q3: {
        si: { correcto: true, mensaje: "¡Muy bien! Simplificar facilita los cálculos: \\\\(\\\\frac{6x}{2} = \\\\frac{12}{2}\\\\) → \\\\(3x = 6\\\\) → \\\\(x = 2\\\\)." },
        no: { correcto: false, mensaje: "Simplificar antes de operar reduce errores. \\\\(\\\\frac{4x}{2} = \\\\frac{8}{2}\\\\) se simplifica a \\\\(2x = 4\\\\). Revisa sección 05." },
        duda: { correcto: false, mensaje: "Si tienes \\\\(\\\\frac{10x}{5} = \\\\frac{20}{5}\\\\), simplifica cada lado: \\\\(2x = 4\\\\), luego \\\\(x = 2\\\\)." }
      },
      q4: {
        si: { correcto: true, mensaje: "¡Genial! NUNCA puedes dividir entre cero. Es una operación matemática imposible." },
        no: { correcto: false, mensaje: "¡IMPORTANTE! No puedes dividir entre 0. Si el denominador es 0, la ecuación no tiene solución. Revisa sección 06." },
        duda: { correcto: false, mensaje: "Regla fundamental: la división entre cero NO EXISTE. Si \\\\(\\\\frac{x}{0} = 5\\\\) ⇒ NO HAY SOLUCIÓN." }
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
          ` : ''}
        `;
        
        feedbackDiv.style.display = 'block';
        
        if (typeof MathJax !== 'undefined') {
          MathJax.typesetPromise([feedbackDiv]).catch((err) => console.log('MathJax error:', err));
        }

        feedbackDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      });
    }"""
    
    # Buscar donde insertar JS (antes de cierre de script)
    if '  </script>' in contenido:
        contenido = contenido.replace('  </script>', js_code + '\n  </script>')
        print("✓ JavaScript añadido a S6")
    else:
        print("✗ No se encontró el cierre de script en S6")
        return False
    
    with open(archivo, 'w', encoding='utf-8') as f:
        f.write(contenido)
    
    return True


def procesar_s7():
    archivo = 'S7_ecuaciones_parentesis.html'
    
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Reemplazar autoevaluación antigua
    autoevaluacion_vieja = """      <div class="panel panel-checkpoint">
        <h3>Autoevaluación</h3>
        <ol>
          <li>¿Entiendes el concepto principal de esta sesión? ___</li>
          <li>¿Puedes resolver ejercicios básicos sin ayuda? ___</li>
          <li>¿Sabes aplicar esto a problemas reales? ___</li>
          <li>¿Qué parte te resultó más difícil? ___</li>
        </ol>
      </div>"""
    
    autoevaluacion_nueva = """      <div class="panel panel-checkpoint">
        <h3>Autoevaluación Interactiva</h3>
        <p style="margin-bottom: calc(var(--spacing-unit) * 6);">Responde honestamente (esto es solo para ti, no se guarda ningún dato):</p>
        
        <form id="autoevaluacion-form" style="margin-bottom: calc(var(--spacing-unit) * 4);">
          <div class="pregunta-autoevaluacion">
            <p class="pregunta-texto"><strong>1.</strong> ¿Aplicas correctamente la propiedad distributiva?</p>
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
            <p class="pregunta-texto"><strong>2.</strong> ¿Eliminas paréntesis sin errores de signos?</p>
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
            <p class="pregunta-texto"><strong>3.</strong> ¿Reduces términos semejantes tras quitar paréntesis?</p>
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
            <p class="pregunta-texto"><strong>4.</strong> ¿Resuelves ecuaciones con paréntesis anidados?</p>
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
        print("✓ Reemplazo de autoevaluación en S7 completado")
    else:
        print("✗ No se encontró la sección de autoevaluación en S7")
        return False
    
    # Añadir JavaScript antes de cierre de script
    js_code = """
    // Autoevaluación Interactiva - S7 Ecuaciones con Paréntesis
    const feedbackData = {
      q1: {
        si: { correcto: true, mensaje: "¡Perfecto! \\\\(3(x + 2) = 3 \\\\cdot x + 3 \\\\cdot 2 = 3x + 6\\\\). Multiplicas el número por cada término." },
        no: { correcto: false, mensaje: "Propiedad distributiva: \\\\(a(b + c) = ab + ac\\\\). Multiplica el factor por todos los términos dentro del paréntesis. Revisa sección 02." },
        duda: { correcto: false, mensaje: "Ejemplo: \\\\(5(x - 1) = 5 \\\\cdot x + 5 \\\\cdot (-1) = 5x - 5\\\\). El signo menos se mantiene. Practica en sección 03." }
      },
      q2: {
        si: { correcto: true, mensaje: "¡Excelente! Signo menos delante del paréntesis cambia todos los signos: \\\\(-(x - 3) = -x + 3\\\\)." },
        no: { correcto: false, mensaje: "¡CUIDADO con los signos! \\\\(-(2x - 5)\\\\) se convierte en \\\\(-2x + 5\\\\) (ambos cambian). Revisa sección 04." },
        duda: { correcto: false, mensaje: "Regla: signo '-' delante cambia TODO. \\\\(-(3x + 4) = -3x - 4\\\\), \\\\(-(3x - 4) = -3x + 4\\\\). Memorízalo." }
      },
      q3: {
        si: { correcto: true, mensaje: "¡Muy bien! Tras quitar paréntesis siempre buscas términos con la misma letra: \\\\(3x + 2x = 5x\\\\)." },
        no: { correcto: false, mensaje: "Después de eliminar paréntesis, agrupa términos semejantes. \\\\(2x + 3 + 4x - 1 = 6x + 2\\\\). Revisa sección 05." },
        duda: { correcto: false, mensaje: "Ejemplo completo: \\\\(2(x + 1) + 3x = 2x + 2 + 3x = 5x + 2\\\\). Practica más en sección 06." }
      },
      q4: {
        si: { correcto: true, mensaje: "¡Genial! Paréntesis de dentro hacia fuera. \\\\(2(3(x + 1) - 2)\\\\): primero \\\\(3(x+1)=3x+3\\\\), luego \\\\(2(3x+3-2)=2(3x+1)=6x+2\\\\)." },
        no: { correcto: false, mensaje: "Con paréntesis anidados, trabaja de dentro hacia fuera. Revisa sección 07 con calma." },
        duda: { correcto: false, mensaje: "Estrategia paso a paso: 1) Elimina paréntesis internos, 2) Reduce, 3) Elimina externos. Repasa ejemplos de sección 07." }
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
          ` : ''}
        `;
        
        feedbackDiv.style.display = 'block';
        
        if (typeof MathJax !== 'undefined') {
          MathJax.typesetPromise([feedbackDiv]).catch((err) => console.log('MathJax error:', err));
        }

        feedbackDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      });
    }"""
    
    # Buscar donde insertar JS (antes de cierre de script)
    if '  </script>' in contenido:
        contenido = contenido.replace('  </script>', js_code + '\n  </script>')
        print("✓ JavaScript añadido a S7")
    else:
        print("✗ No se encontró el cierre de script en S7")
        return False
    
    with open(archivo, 'w', encoding='utf-8') as f:
        f.write(contenido)
    
    return True


# Ejecutar
if __name__ == '__main__':
    print("\n=== Procesando S6 y S7 ===\n")
    
    print("📝 Procesando S6_ecuaciones_multiplicacion.html...")
    if procesar_s6():
        print("✅ S6 procesado exitosamente\n")
    else:
        print("❌ Error procesando S6\n")
    
    print("📝 Procesando S7_ecuaciones_parentesis.html...")
    if procesar_s7():
        print("✅ S7 procesado exitosamente\n")
    else:
        print("❌ Error procesando S7\n")
    
    print("=== FIN ===")
