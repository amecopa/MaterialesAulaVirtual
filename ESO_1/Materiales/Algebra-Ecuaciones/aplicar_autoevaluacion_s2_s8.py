#!/usr/bin/env python3
"""
Script para aplicar autoevaluación interactiva a sesiones S2-S8
Adapta las preguntas al contenido específico de cada sesión
"""

import re
import os

# Configuración de preguntas por sesión
PREGUNTAS_POR_SESION = {
    'S2_valor_numerico.html': {
        'titulo': 'Valor Numérico',
        'preguntas': [
            {
                'texto': '¿Sabes calcular el valor numérico de \\( 2x + 3 \\) cuando \\( x = 5 \\)?',
                'feedback': {
                    'si': {
                        'correcto': True,
                        'mensaje': '¡Perfecto! Sustituyes x=5: \\(2(5) + 3 = 10 + 3 = 13\\).'
                    },
                    'no': {
                        'correcto': False,
                        'mensaje': 'Sustituye la variable por el número y calcula: \\(2(5) + 3 = 13\\). Revisa la sección 03.'
                    },
                    'duda': {
                        'correcto': False,
                        'mensaje': 'Recuerda: sustituir significa "cambiar x por el número". Practica en la sección 05.'
                    }
                }
            },
            {
                'texto': '¿Distingues entre \\( x^2 \\) cuando x=3 (que es 9) y \\( 2x \\) cuando x=3 (que es 6)?',
                'feedback': {
                    'si': {
                        'correcto': True,
                        'mensaje': '¡Excelente! \\(x^2 = 3^2 = 9\\) (elevar al cuadrado) vs \\(2x = 2(3) = 6\\) (multiplicar por 2).'
                    },
                    'no': {
                        'correcto': False,
                        'mensaje': '\\(x^2\\) es "x al cuadrado", \\(2x\\) es "dos veces x". Son operaciones diferentes. Revisa sección 02.'
                    },
                    'duda': {
                        'correcto': False,
                        'mensaje': 'Prueba con ejemplos: si x=4, entonces \\(x^2 = 16\\) pero \\(2x = 8\\).'
                    }
                }
            },
            {
                'texto': '¿Puedes verificar si un valor es solución de una expresión?',
                'feedback': {
                    'si': {
                        'correcto': True,
                        'mensaje': '¡Muy bien! Sustituyes el valor y compruebas si se cumple la igualdad.'
                    },
                    'no': {
                        'correcto': False,
                        'mensaje': 'Para verificar, sustituye el valor en la expresión y comprueba el resultado. Practica en sección 06.'
                    },
                    'duda': {
                        'correcto': False,
                        'mensaje': 'Ejemplo: ¿Es x=2 solución de \\(3x = 6\\)? Sustituye: \\(3(2) = 6\\) ✓ Sí lo es.'
                    }
                }
            },
            {
                'texto': '¿Respetas el orden de operaciones (paréntesis, potencias, productos, sumas)?',
                'feedback': {
                    'si': {
                        'correcto': True,
                        'mensaje': '¡Genial! El orden correcto es clave para obtener resultados correctos.'
                    },
                    'no': {
                        'correcto': False,
                        'mensaje': 'Recuerda: 1º paréntesis, 2º potencias, 3º × y ÷, 4º + y −. Revisa sección 04.'
                    },
                    'duda': {
                        'correcto': False,
                        'mensaje': 'Ejemplo: \\(2 + 3 \\times 4 = 2 + 12 = 14\\) (no es 20). Multiplica primero.'
                    }
                }
            }
        ]
    },
    'S3_monomios.html': {
        'titulo': 'Monomios',
        'preguntas': [
            {
                'texto': '¿Identificas correctamente el coeficiente y la parte literal de un monomio?',
                'feedback': {
                    'si': {
                        'correcto': True,
                        'mensaje': '¡Perfecto! En \\(5x^2\\), el coeficiente es 5 y la parte literal es \\(x^2\\).'
                    },
                    'no': {
                        'correcto': False,
                        'mensaje': 'El coeficiente es el número, la parte literal son las letras con sus exponentes. Revisa sección 01.'
                    },
                    'duda': {
                        'correcto': False,
                        'mensaje': 'Ejemplo: en \\(-3xy^2\\), coeficiente = -3, parte literal = \\(xy^2\\). Practica en sección 03.'
                    }
                }
            },
            {
                'texto': '¿Sabes cuándo dos monomios son semejantes?',
                'feedback': {
                    'si': {
                        'correcto': True,
                        'mensaje': '¡Excelente! Son semejantes si tienen la misma parte literal (mismas letras con mismos exponentes).'
                    },
                    'no': {
                        'correcto': False,
                        'mensaje': 'Monomios semejantes = misma parte literal. \\(3x^2\\) y \\(5x^2\\) SÍ. \\(3x^2\\) y \\(3x\\) NO. Revisa sección 02.'
                    },
                    'duda': {
                        'correcto': False,
                        'mensaje': '¿Son semejantes \\(2xy\\) y \\(5xy\\)? SÍ (misma parte literal). ¿Y \\(2xy\\) y \\(2x^2\\)? NO.'
                    }
                }
            },
            {
                'texto': '¿Puedes sumar y restar monomios semejantes?',
                'feedback': {
                    'si': {
                        'correcto': True,
                        'mensaje': '¡Muy bien! Sumas/restas los coeficientes y mantienes la parte literal: \\(3x + 5x = 8x\\).'
                    },
                    'no': {
                        'correcto': False,
                        'mensaje': 'Solo se pueden sumar/restar monomios semejantes. Suma coeficientes. Revisa sección 05.'
                    },
                    'duda': {
                        'correcto': False,
                        'mensaje': 'Ejemplo: \\(7x^2 - 3x^2 = 4x^2\\) (restas 7-3=4). La parte literal no cambia.'
                    }
                }
            },
            {
                'texto': '¿Multiplicas correctamente monomios?',
                'feedback': {
                    'si': {
                        'correcto': True,
                        'mensaje': '¡Genial! Multiplicas coeficientes y sumas exponentes: \\(2x \\cdot 3x^2 = 6x^3\\).'
                    },
                    'no': {
                        'correcto': False,
                        'mensaje': 'Multiplica coeficientes, suma exponentes de la misma letra. Revisa sección 06.'
                    },
                    'duda': {
                        'correcto': False,
                        'mensaje': 'Ejemplo: \\(4x \\cdot 2x = (4 \\cdot 2)(x \\cdot x) = 8x^2\\). Coeficientes: 4×2=8, exponentes: 1+1=2.'
                    }
                }
            }
        ]
    },
    'S4_concepto_ecuacion.html': {
        'titulo': 'Concepto de Ecuación',
        'preguntas': [
            {
                'texto': '¿Diferencias entre una expresión algebraica y una ecuación?',
                'feedback': {
                    'si': {
                        'correcto': True,
                        'mensaje': '¡Perfecto! Una ecuación tiene un signo = (igualdad), una expresión algebraica no.'
                    },
                    'no': {
                        'correcto': False,
                        'mensaje': 'Expresión: \\(2x + 3\\). Ecuación: \\(2x + 3 = 7\\) (tiene =). Revisa sección 01.'
                    },
                    'duda': {
                        'correcto': False,
                        'mensaje': 'La ecuación afirma que dos expresiones son iguales. El = es la clave.'
                    }
                }
            },
            {
                'texto': '¿Entiendes qué es la solución de una ecuación?',
                'feedback': {
                    'si': {
                        'correcto': True,
                        'mensaje': '¡Excelente! Es el valor que hace verdadera la igualdad. En \\(x + 2 = 5\\), x=3 es solución.'
                    },
                    'no': {
                        'correcto': False,
                        'mensaje': 'La solución es el número que sustituido en x hace que ambos lados sean iguales. Revisa sección 02.'
                    },
                    'duda': {
                        'correcto': False,
                        'mensaje': 'Prueba: si \\(x + 4 = 10\\), sustituye x=6: \\(6 + 4 = 10\\) ✓ Entonces x=6 es solución.'
                    }
                }
            },
            {
                'texto': '¿Verificas si un valor dado es solución de una ecuación?',
                'feedback': {
                    'si': {
                        'correcto': True,
                        'mensaje': '¡Muy bien! Sustituyes el valor en la ecuación y compruebas si se cumple la igualdad.'
                    },
                    'no': {
                        'correcto': False,
                        'mensaje': 'Para verificar, sustituye el valor en ambos lados y comprueba si son iguales. Practica en sección 05.'
                    },
                    'duda': {
                        'correcto': False,
                        'mensaje': '¿Es x=4 solución de \\(2x = 8\\)? Sustituye: \\(2(4) = 8\\) → \\(8 = 8\\) ✓ Sí.'
                    }
                }
            },
            {
                'texto': '¿Identificas los miembros, términos e incógnita de una ecuación?',
                'feedback': {
                    'si': {
                        'correcto': True,
                        'mensaje': '¡Genial! En \\(3x + 2 = 8\\): 1er miembro (\\(3x + 2\\)), 2º miembro (8), incógnita (x).'
                    },
                    'no': {
                        'correcto': False,
                        'mensaje': 'Miembros: lo que hay a cada lado del =. Incógnita: la letra (x). Revisa sección 03.'
                    },
                    'duda': {
                        'correcto': False,
                        'mensaje': 'En \\(5 + x = 12\\): miembro izquierdo = \\(5 + x\\), derecho = 12, incógnita = x.'
                    }
                }
            }
        ]
    },
    'S5_ecuaciones_suma_resta.html': {
        'titulo': 'Ecuaciones con Sumas y Restas',
        'preguntas': [
            {
                'texto': '¿Aplicas correctamente la transposición de términos?',
                'feedback': {
                    'si': {
                        'correcto': True,
                        'mensaje': '¡Perfecto! Si pasas un término al otro lado, cambia su signo: +3 pasa como -3.'
                    },
                    'no': {
                        'correcto': False,
                        'mensaje': 'Al cambiar de miembro, cambia el signo: + se vuelve −, − se vuelve +. Revisa sección 03.'
                    },
                    'duda': {
                        'correcto': False,
                        'mensaje': 'Ejemplo: \\(x + 5 = 12\\) → \\(x = 12 - 5\\) (el +5 pasa como -5).'
                    }
                }
            },
            {
                'texto': '¿Aíslas correctamente la incógnita en ecuaciones simples?',
                'feedback': {
                    'si': {
                        'correcto': True,
                        'mensaje': '¡Excelente! Pasas todos los números a un lado y dejas la x sola al otro lado.'
                    },
                    'no': {
                        'correcto': False,
                        'mensaje': 'Pasa todos los términos con x a un lado, los números al otro. Revisa sección 04.'
                    },
                    'duda': {
                        'correcto': False,
                        'mensaje': '\\(x + 3 = 10\\) → pasa el +3: \\(x = 10 - 3\\) → \\(x = 7\\). Practica en sección 05.'
                    }
                }
            },
            {
                'texto': '¿Reduces correctamente términos semejantes antes de resolver?',
                'feedback': {
                    'si': {
                        'correcto': True,
                        'mensaje': '¡Muy bien! Simplificas \\(2x + 3x = 5x\\) antes de continuar resolviendo.'
                    },
                    'no': {
                        'correcto': False,
                        'mensaje': 'Agrupa términos con x y números por separado antes de transponer. Revisa sección 02.'
                    },
                    'duda': {
                        'correcto': False,
                        'mensaje': 'En \\(2x + 3 + x = 10\\), primero simplifica: \\(3x + 3 = 10\\), luego resuelve.'
                    }
                }
            },
            {
                'texto': '¿Compruebas la solución sustituyendo en la ecuación original?',
                'feedback': {
                    'si': {
                        'correcto': True,
                        'mensaje': '¡Genial! Siempre es buena práctica verificar que tu solución sea correcta.'
                    },
                    'no': {
                        'correcto': False,
                        'mensaje': 'Comprueba siempre: sustituye el valor de x y verifica que se cumple la igualdad. Sección 06.'
                    },
                    'duda': {
                        'correcto': False,
                        'mensaje': 'Si obtienes x=5, sustituye en la ecuación original y comprueba que ambos lados dan lo mismo.'
                    }
                }
            }
        ]
    },
    'S6_ecuaciones_multiplicacion.html': {
        'titulo': 'Ecuaciones con Multiplicación',
        'preguntas': [
            {
                'texto': '¿Despejas la x cuando está multiplicando (como en \\(3x = 12\\))?',
                'feedback': {
                    'si': {
                        'correcto': True,
                        'mensaje': '¡Perfecto! Divides ambos lados: \\(3x = 12\\) → \\(x = 12 \\div 3 = 4\\).'
                    },
                    'no': {
                        'correcto': False,
                        'mensaje': 'Si x está multiplicando, divide ambos lados por ese número. Revisa sección 03.'
                    },
                    'duda': {
                        'correcto': False,
                        'mensaje': 'Ejemplo: \\(5x = 20\\) → divide por 5 → \\(x = 20 \\div 5 = 4\\). Practica en sección 05.'
                    }
                }
            },
            {
                'texto': '¿Despejas la x cuando está dividiendo (como en \\(\\frac{x}{4} = 3\\))?',
                'feedback': {
                    'si': {
                        'correcto': True,
                        'mensaje': '¡Excelente! Multiplicas ambos lados: \\(\\frac{x}{4} = 3\\) → \\(x = 3 \\times 4 = 12\\).'
                    },
                    'no': {
                        'correcto': False,
                        'mensaje': 'Si x está dividiendo, multiplica ambos lados por ese número. Revisa sección 04.'
                    },
                    'duda': {
                        'correcto': False,
                        'mensaje': 'Ejemplo: \\(\\frac{x}{2} = 7\\) → multiplica por 2 → \\(x = 7 \\times 2 = 14\\).'
                    }
                }
            },
            {
                'texto': '¿Combinas sumas/restas con productos en ecuaciones?',
                'feedback': {
                    'si': {
                        'correcto': True,
                        'mensaje': '¡Muy bien! Primero transpones términos, luego despejas el coeficiente de x.'
                    },
                    'no': {
                        'correcto': False,
                        'mensaje': 'Paso 1: transponer términos. Paso 2: dividir para despejar x. Revisa sección 05.'
                    },
                    'duda': {
                        'correcto': False,
                        'mensaje': '\\(2x + 3 = 11\\) → \\(2x = 11 - 3\\) → \\(2x = 8\\) → \\(x = 4\\). Dos pasos.'
                    }
                }
            },
            {
                'texto': '¿Evitas dividir por cero y reconoces cuándo una ecuación no tiene solución?',
                'feedback': {
                    'si': {
                        'correcto': True,
                        'mensaje': '¡Genial! Nunca se puede dividir por cero. Algunas ecuaciones no tienen solución.'
                    },
                    'no': {
                        'correcto': False,
                        'mensaje': 'Dividir por 0 es imposible. Si llegas a \\(0x = 5\\), no hay solución. Revisa sección 06.'
                    },
                    'duda': {
                        'correcto': False,
                        'mensaje': 'Si al resolver llegas a algo como \\(0 = 3\\), la ecuación no tiene solución.'
                    }
                }
            }
        ]
    },
    'S7_ecuaciones_parentesis.html': {
        'titulo': 'Ecuaciones con Paréntesis',
        'preguntas': [
            {
                'texto': '¿Aplicas correctamente la propiedad distributiva?',
                'feedback': {
                    'si': {
                        'correcto': True,
                        'mensaje': '¡Perfecto! \\(3(x + 2) = 3x + 6\\). Multiplicas el de fuera por cada término del paréntesis.'
                    },
                    'no': {
                        'correcto': False,
                        'mensaje': 'Multiplica lo de fuera por cada término dentro: \\(a(b + c) = ab + ac\\). Revisa sección 03.'
                    },
                    'duda': {
                        'correcto': False,
                        'mensaje': 'Ejemplo: \\(2(x + 5) = 2 \\cdot x + 2 \\cdot 5 = 2x + 10\\). Practica en sección 05.'
                    }
                }
            },
            {
                'texto': '¿Eliminas paréntesis con signo negativo delante?',
                'feedback': {
                    'si': {
                        'correcto': True,
                        'mensaje': '¡Excelente! \\(-(x - 3) = -x + 3\\). Cambias el signo de cada término dentro.'
                    },
                    'no': {
                        'correcto': False,
                        'mensaje': 'El signo − delante cambia todos los signos: \\(-(a + b) = -a - b\\). Revisa sección 04.'
                    },
                    'duda': {
                        'correcto': False,
                        'mensaje': '\\(-(2x - 5)\\) se convierte en \\(-2x + 5\\) (ambos signos cambian).'
                    }
                }
            },
            {
                'texto': '¿Resuelves ecuaciones con paréntesis anidados?',
                'feedback': {
                    'si': {
                        'correcto': True,
                        'mensaje': '¡Muy bien! Eliminas paréntesis de dentro hacia fuera, paso a paso.'
                    },
                    'no': {
                        'correcto': False,
                        'mensaje': 'Trabaja de dentro hacia fuera. Elimina primero los paréntesis interiores. Revisa sección 06.'
                    },
                    'duda': {
                        'correcto': False,
                        'mensaje': 'En \\(2(3(x + 1))\\), primero \\(3(x + 1) = 3x + 3\\), luego \\(2(3x + 3) = 6x + 6\\).'
                    }
                }
            },
            {
                'texto': '¿Compruebas tu solución final sustituyendo en la ecuación original (con paréntesis)?',
                'feedback': {
                    'si': {
                        'correcto': True,
                        'mensaje': '¡Genial! Es importante verificar con la ecuación original, no con la simplificada.'
                    },
                    'no': {
                        'correcto': False,
                        'mensaje': 'Sustituye tu solución en la ecuación original (con paréntesis) para comprobar. Sección 07.'
                    },
                    'duda': {
                        'correcto': False,
                        'mensaje': 'Usa la ecuación ORIGINAL (antes de quitar paréntesis) para verificar tu respuesta.'
                    }
                }
            }
        ]
    },
    'S8_problemas_reales.html': {
        'titulo': 'Problemas Reales',
        'preguntas': [
            {
                'texto': '¿Traduces correctamente un problema verbal a una ecuación?',
                'feedback': {
                    'si': {
                        'correcto': True,
                        'mensaje': '¡Perfecto! Identificas la incógnita (x) y las relaciones matemáticas del problema.'
                    },
                    'no': {
                        'correcto': False,
                        'mensaje': 'Lee bien, identifica qué es x y cómo se relaciona con los datos. Revisa sección 03.'
                    },
                    'duda': {
                        'correcto': False,
                        'mensaje': '"El doble de un número más 5 es 17" → \\(2x + 5 = 17\\). Practica en sección 05.'
                    }
                }
            },
            {
                'texto': '¿Identificas correctamente qué representa la incógnita x?',
                'feedback': {
                    'si': {
                        'correcto': True,
                        'mensaje': '¡Excelente! Defines claramente qué representa x antes de plantear la ecuación.'
                    },
                    'no': {
                        'correcto': False,
                        'mensaje': 'Define primero: "x = edad de María" o "x = número de cromos". Revisa sección 02.'
                    },
                    'duda': {
                        'correcto': False,
                        'mensaje': 'Siempre empieza escribiendo: "Sea x = ..." (lo que buscas). Eso te ayuda a plantear.'
                    }
                }
            },
            {
                'texto': '¿Compruebas que tu solución tiene sentido en el contexto del problema?',
                'feedback': {
                    'si': {
                        'correcto': True,
                        'mensaje': '¡Muy bien! Si el problema habla de edades, x=-5 no tiene sentido. Siempre valida.'
                    },
                    'no': {
                        'correcto': False,
                        'mensaje': 'La solución debe tener sentido: edades positivas, cantidades enteras si es necesario, etc. Sección 06.'
                    },
                    'duda': {
                        'correcto': False,
                        'mensaje': 'Si x=número de personas, no puede ser 3.7 (debe ser entero). Revisa tu solución.'
                    }
                }
            },
            {
                'texto': '¿Escribes una respuesta completa con unidades y contexto?',
                'feedback': {
                    'si': {
                        'correcto': True,
                        'mensaje': '¡Genial! No solo "x=12", sino "María tiene 12 años" o "Hay 12 cromos".'
                    },
                    'no': {
                        'correcto': False,
                        'mensaje': 'Escribe la respuesta en el contexto del problema con sus unidades. Revisa sección 07.'
                    },
                    'duda': {
                        'correcto': False,
                        'mensaje': 'Si te preguntan la edad y obtienes x=15, responde: "María tiene 15 años".'
                    }
                }
            }
        ]
    }
}

# Estilos CSS a añadir
CSS_AUTOEVALUACION = """
    /* Autoevaluación Interactiva */
    .pregunta-autoevaluacion {
      margin-bottom: calc(var(--spacing-unit) * 6);
      padding: calc(var(--spacing-unit) * 4);
      background: rgba(255, 255, 255, 0.5);
      border-radius: var(--radius-sm);
      border-left: 3px solid var(--color-accent);
    }

    .pregunta-texto {
      font-weight: 600;
      color: var(--color-text);
      margin-bottom: calc(var(--spacing-unit) * 3);
    }

    .opciones-radio {
      display: flex;
      gap: calc(var(--spacing-unit) * 4);
      flex-wrap: wrap;
    }

    .radio-label {
      display: flex;
      align-items: center;
      gap: calc(var(--spacing-unit) * 2);
      cursor: pointer;
      padding: calc(var(--spacing-unit) * 2) calc(var(--spacing-unit) * 4);
      border-radius: var(--radius-sm);
      background: white;
      border: 2px solid #e5e7eb;
      transition: all 0.2s;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      font-size: 0.95rem;
    }

    .radio-label:hover {
      background: var(--color-bg-alt);
      border-color: var(--color-accent);
      transform: translateY(-2px);
    }

    .radio-label input[type="radio"] {
      width: 18px;
      height: 18px;
      cursor: pointer;
    }

    .radio-label input[type="radio"]:checked {
      accent-color: var(--color-accent);
    }

    .btn-autoevaluacion {
      background: linear-gradient(135deg, var(--color-accent) 0%, #ea580c 100%);
      color: white;
      border: none;
      padding: calc(var(--spacing-unit) * 3) calc(var(--spacing-unit) * 8);
      border-radius: var(--radius-sm);
      font-weight: 700;
      font-size: 1rem;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      cursor: pointer;
      transition: all 0.3s;
      box-shadow: var(--shadow-md);
      display: block;
      margin: calc(var(--spacing-unit) * 6) auto 0;
    }

    .btn-autoevaluacion:hover {
      transform: translateY(-3px);
      box-shadow: var(--shadow-lg);
    }

    .btn-autoevaluacion:active {
      transform: translateY(-1px);
    }

    #feedback-autoevaluacion {
      margin-top: calc(var(--spacing-unit) * 6);
      padding: calc(var(--spacing-unit) * 6);
      border-radius: var(--radius-md);
      animation: slideIn 0.5s ease;
    }

    @keyframes slideIn {
      from {
        opacity: 0;
        transform: translateY(-20px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    .feedback-excelente {
      background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
      border: 3px solid #10b981;
    }

    .feedback-bien {
      background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
      border: 3px solid #3b82f6;
    }

    .feedback-mejorar {
      background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
      border: 3px solid #f59e0b;
    }

    .feedback-titulo {
      font-size: 1.5rem;
      font-weight: 700;
      margin-bottom: calc(var(--spacing-unit) * 4);
      text-align: center;
    }

    .feedback-puntuacion {
      font-size: 3rem;
      font-weight: 900;
      text-align: center;
      margin: calc(var(--spacing-unit) * 4) 0;
    }

    .feedback-mensaje {
      font-size: 1.1rem;
      line-height: 1.6;
      margin-bottom: calc(var(--spacing-unit) * 4);
    }

    .feedback-consejo {
      background: rgba(255, 255, 255, 0.7);
      padding: calc(var(--spacing-unit) * 4);
      border-radius: var(--radius-sm);
      border-left: 4px solid currentColor;
      margin-top: calc(var(--spacing-unit) * 4);
    }

    .feedback-consejo strong {
      display: block;
      margin-bottom: calc(var(--spacing-unit) * 2);
      font-size: 1.05rem;
    }

    body.high-contrast .radio-label {
      background: #000;
      border-color: #ffff00;
      color: #ffff00;
    }

    body.high-contrast .btn-autoevaluacion {
      background: #ffff00;
      color: #000;
    }

    body.high-contrast #feedback-autoevaluacion {
      background: #1a1a1a !important;
      border-color: #ffff00 !important;
      color: #ffff00;
    }
"""


def generar_html_formulario(preguntas):
    """Genera el HTML del formulario de autoevaluación"""
    html_preguntas = []
    
    for i, pregunta in enumerate(preguntas, 1):
        html_preguntas.append(f"""
          <div class="pregunta-autoevaluacion">
            <p class="pregunta-texto"><strong>{i}.</strong> {pregunta['texto']}</p>
            <div class="opciones-radio">
              <label class="radio-label">
                <input type="radio" name="q{i}" value="si" required>
                <span>✓ Sí</span>
              </label>
              <label class="radio-label">
                <input type="radio" name="q{i}" value="no">
                <span>✗ No</span>
              </label>
              <label class="radio-label">
                <input type="radio" name="q{i}" value="duda">
                <span>? Tengo dudas</span>
              </label>
            </div>
          </div>""")
    
    return f"""      <div class="panel panel-checkpoint">
        <h3>Autoevaluación Interactiva</h3>
        <p style="margin-bottom: calc(var(--spacing-unit) * 6);">Responde honestamente (esto es solo para ti, no se guarda ningún dato):</p>
        
        <form id="autoevaluacion-form" style="margin-bottom: calc(var(--spacing-unit) * 4);">
{''.join(html_preguntas)}

          <button type="submit" class="btn-autoevaluacion">📊 Ver mi resultado</button>
        </form>

        <div id="feedback-autoevaluacion" style="display: none;"></div>
      </div>"""


def generar_javascript(preguntas):
    """Genera el código JavaScript para la autoevaluación"""
    
    # Construir objeto feedbackData
    feedback_js = "    const feedbackData = {\n"
    
    for i, pregunta in enumerate(preguntas, 1):
        feedback_js += f"      q{i}: {{\n"
        for respuesta_tipo in ['si', 'no', 'duda']:
            feedback = pregunta['feedback'][respuesta_tipo]
            correcto_str = 'true' if feedback['correcto'] else 'false'
            feedback_js += f"        {respuesta_tipo}: {{ correcto: {correcto_str}, mensaje: \"{feedback['mensaje']}\" }},\n"
        feedback_js += "      },\n"
    
    feedback_js += "    };\n"
    
    # Resto del JavaScript
    js_code = f"""
    // Autoevaluación Interactiva
{feedback_js}
    const autoevalForm = document.getElementById('autoevaluacion-form');
    if (autoevalForm) {{
      autoevalForm.addEventListener('submit', function(e) {{
        e.preventDefault();
        
        // Obtener respuestas
        const respuestas = {{
          q1: document.querySelector('input[name="q1"]:checked')?.value,
          q2: document.querySelector('input[name="q2"]:checked')?.value,
          q3: document.querySelector('input[name="q3"]:checked')?.value,
          q4: document.querySelector('input[name="q4"]:checked')?.value
        }};

        // Validar que todas estén respondidas
        if (!respuestas.q1 || !respuestas.q2 || !respuestas.q3 || !respuestas.q4) {{
          alert('⚠️ Por favor, responde todas las preguntas antes de enviar.');
          return;
        }}

        // Calcular puntuación
        let correctas = 0;
        let mensajes = [];
        
        for (let pregunta in respuestas) {{
          const respuesta = respuestas[pregunta];
          const feedback = feedbackData[pregunta][respuesta];
          
          if (feedback.correcto) {{
            correctas++;
          }}
          mensajes.push(`<li><strong>Pregunta ${{pregunta.slice(1)}}:</strong> ${{feedback.mensaje}}</li>`);
        }}

        // Generar feedback visual
        const feedbackDiv = document.getElementById('feedback-autoevaluacion');
        let claseEstilo, titulo, emoji, mensaje;

        if (correctas === 4) {{
          claseEstilo = 'feedback-excelente';
          titulo = '🎉 ¡EXCELENTE TRABAJO!';
          emoji = '⭐⭐⭐⭐';
          mensaje = '<p class="feedback-mensaje">¡Felicidades! Has comprendido todos los conceptos clave de esta sesión. Estás listo para avanzar al siguiente tema.</p>';
        }} else if (correctas >= 2) {{
          claseEstilo = 'feedback-bien';
          titulo = '👍 ¡BUEN TRABAJO!';
          emoji = '⭐⭐⭐';
          mensaje = '<p class="feedback-mensaje">Vas por buen camino. Hay algunas áreas que necesitan refuerzo. Revisa las secciones indicadas abajo y vuelve a intentarlo.</p>';
        }} else {{
          claseEstilo = 'feedback-mejorar';
          titulo = '💪 ¡SIGUE INTENTÁNDOLO!';
          emoji = '⭐⭐';
          mensaje = '<p class="feedback-mensaje">No te desanimes. El álgebra requiere práctica. Lee de nuevo el material, especialmente las secciones indicadas, y vuelve a hacer la autoevaluación.</p>';
        }}

        feedbackDiv.className = claseEstilo;
        feedbackDiv.innerHTML = `
          <div class="feedback-titulo">${{titulo}}</div>
          <div class="feedback-puntuacion">${{emoji}}</div>
          <div style="text-align: center; font-size: 1.3rem; font-weight: 700; margin-bottom: calc(var(--spacing-unit) * 4);">
            ${{correctas}} de 4 respuestas positivas
          </div>
          ${{mensaje}}
          <div class="feedback-consejo">
            <strong>📋 Detalles de tu autoevaluación:</strong>
            <ul style="margin-top: calc(var(--spacing-unit) * 3);">
              ${{mensajes.join('')}}
            </ul>
          </div>
          ${{correctas < 4 ? `
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
        
        // Renderizar fórmulas matemáticas con MathJax
        if (typeof MathJax !== 'undefined') {{
          MathJax.typesetPromise([feedbackDiv]).catch((err) => console.log('MathJax error:', err));
        }}

        // Scroll suave al feedback
        feedbackDiv.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
      }});
    }}"""
    
    return js_code


def procesar_sesion(archivo, config):
    """Procesa una sesión para agregar autoevaluación interactiva"""
    
    ruta_archivo = archivo
    
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # 1. Añadir CSS (después de los estilos de respuesta)
    if 'body.high-contrast details.respuesta summary {' in contenido:
        punto_insercion = contenido.find('body.high-contrast details.respuesta summary {')
        siguiente_cierre = contenido.find('}', punto_insercion)
        siguiente_cierre = contenido.find('\n', siguiente_cierre)
        
        contenido = contenido[:siguiente_cierre + 1] + CSS_AUTOEVALUACION + '\n' + contenido[siguiente_cierre + 1:]
    
    # 2. Reemplazar sección de autoevaluación
    patron_autoevaluacion = r'<div class="panel panel-checkpoint">\s*<h3>Autoevaluación</h3>.*?</div>'
    
    nuevo_html = generar_html_formulario(config['preguntas'])
    contenido = re.sub(patron_autoevaluacion, nuevo_html, contenido, flags=re.DOTALL)
    
    # 3. Añadir JavaScript (antes del cierre de </script>)
    patron_script_cierre = r'(\s*// Update progress bar on load.*?}\);)\s*</script>'
    
    nuevo_js = generar_javascript(config['preguntas'])
    contenido = re.sub(
        patron_script_cierre,
        r'\1' + nuevo_js + '\n  </script>',
        contenido,
        flags=re.DOTALL
    )
    
    # Guardar
    with open(ruta_archivo, 'w', encoding='utf-8') as f:
        f.write(contenido)
    
    return True


def main():
    """Función principal"""
    print("=" * 70)
    print("   APLICANDO AUTOEVALUACIÓN INTERACTIVA A S2-S8")
    print("=" * 70)
    print()
    
    archivos_procesados = []
    archivos_error = []
    
    for archivo, config in PREGUNTAS_POR_SESION.items():
        print(f"Procesando {archivo} ({config['titulo']})...")
        
        try:
            if procesar_sesion(archivo, config):
                archivos_procesados.append(archivo)
                print(f"  ✓ Completado")
            else:
                archivos_error.append(archivo)
                print(f"  ✗ Error al procesar")
        except Exception as e:
            archivos_error.append(archivo)
            print(f"  ✗ Error: {e}")
        
        print()
    
    # Resumen
    print("=" * 70)
    print("   RESUMEN")
    print("=" * 70)
    print(f"\n✅ Archivos procesados correctamente: {len(archivos_procesados)}/7")
    
    for archivo in archivos_procesados:
        print(f"  ✓ {archivo}")
    
    if archivos_error:
        print(f"\n❌ Archivos con errores: {len(archivos_error)}")
        for archivo in archivos_error:
            print(f"  ✗ {archivo}")
    
    print("\n" + "=" * 70)
    print()


if __name__ == '__main__':
    main()
