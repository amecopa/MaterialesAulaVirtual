#!/usr/bin/env python3
"""
Añadir CSS de autoevaluación a S3, S6, S7
"""

CSS_AUTOEVALUACION = """
    /* === ESTILOS AUTOEVALUACIÓN INTERACTIVA === */
    .pregunta-autoevaluacion {
      margin-bottom: calc(var(--spacing-unit) * 8);
      padding: calc(var(--spacing-unit) * 5);
      background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
      border-radius: calc(var(--spacing-unit) * 2);
      border-left: 4px solid var(--color-primary);
      animation: slideIn 0.3s ease-out;
    }

    .pregunta-texto {
      font-size: 1.1rem;
      font-weight: 600;
      color: var(--color-text);
      margin-bottom: calc(var(--spacing-unit) * 4);
      line-height: 1.6;
    }

    .opciones-radio {
      display: flex;
      flex-direction: column;
      gap: calc(var(--spacing-unit) * 3);
    }

    .radio-label {
      display: flex;
      align-items: center;
      padding: calc(var(--spacing-unit) * 3) calc(var(--spacing-unit) * 4);
      background: white;
      border: 2px solid #dee2e6;
      border-radius: calc(var(--spacing-unit) * 2);
      cursor: pointer;
      transition: all 0.2s ease;
      font-size: 1rem;
      font-weight: 500;
    }

    .radio-label:hover {
      background: #f1f3f5;
      border-color: var(--color-primary);
      transform: translateX(4px);
    }

    .radio-label input[type="radio"] {
      margin-right: calc(var(--spacing-unit) * 3);
      width: 20px;
      height: 20px;
      cursor: pointer;
    }

    .radio-label input[type="radio"]:checked + span {
      color: var(--color-primary);
      font-weight: 700;
    }

    .btn-autoevaluacion {
      display: block;
      width: 100%;
      max-width: 400px;
      margin: calc(var(--spacing-unit) * 6) auto 0;
      padding: calc(var(--spacing-unit) * 4) calc(var(--spacing-unit) * 8);
      font-size: 1.2rem;
      font-weight: 700;
      color: white;
      background: linear-gradient(135deg, var(--color-primary) 0%, #0056b3 100%);
      border: none;
      border-radius: calc(var(--spacing-unit) * 2);
      cursor: pointer;
      transition: all 0.3s ease;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .btn-autoevaluacion:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
      background: linear-gradient(135deg, #0056b3 0%, var(--color-primary) 100%);
    }

    .btn-autoevaluacion:active {
      transform: translateY(0);
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    /* Feedback Styles */
    #feedback-autoevaluacion {
      margin-top: calc(var(--spacing-unit) * 6);
      padding: calc(var(--spacing-unit) * 6);
      border-radius: calc(var(--spacing-unit) * 3);
      animation: slideIn 0.4s ease-out;
    }

    .feedback-excelente {
      background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
      border: 3px solid #28a745;
    }

    .feedback-bien {
      background: linear-gradient(135deg, #d1ecf1 0%, #bee5eb 100%);
      border: 3px solid #17a2b8;
    }

    .feedback-mejorar {
      background: linear-gradient(135deg, #fff3cd 0%, #ffeeba 100%);
      border: 3px solid #ffc107;
    }

    .feedback-titulo {
      font-size: 1.8rem;
      font-weight: 900;
      text-align: center;
      margin-bottom: calc(var(--spacing-unit) * 3);
      color: var(--color-text);
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    .feedback-puntuacion {
      font-size: 2.5rem;
      text-align: center;
      margin-bottom: calc(var(--spacing-unit) * 4);
    }

    .feedback-mensaje {
      font-size: 1.1rem;
      line-height: 1.7;
      color: var(--color-text);
      text-align: center;
      margin-bottom: calc(var(--spacing-unit) * 5);
      font-weight: 500;
    }

    .feedback-consejo {
      background: rgba(255, 255, 255, 0.7);
      padding: calc(var(--spacing-unit) * 4);
      border-radius: calc(var(--spacing-unit) * 2);
      border-left: 4px solid #28a745;
      margin-top: calc(var(--spacing-unit) * 4);
    }

    .feedback-consejo strong {
      display: block;
      font-size: 1.2rem;
      margin-bottom: calc(var(--spacing-unit) * 2);
      color: var(--color-primary);
    }

    .feedback-consejo ul {
      list-style: none;
      padding-left: 0;
    }

    .feedback-consejo li {
      padding: calc(var(--spacing-unit) * 2) 0;
      border-bottom: 1px solid rgba(0, 0, 0, 0.1);
    }

    .feedback-consejo li:last-child {
      border-bottom: none;
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

    @media (prefers-contrast: high) {
      .radio-label {
        border-width: 3px;
      }
      
      .btn-autoevaluacion {
        border: 3px solid white;
      }
    }

    @media (max-width: 900px) {
      .pregunta-autoevaluacion {
        padding: calc(var(--spacing-unit) * 4);
      }
      
      .pregunta-texto {
        font-size: 1rem;
      }
      
      .radio-label {
        padding: calc(var(--spacing-unit) * 2.5) calc(var(--spacing-unit) * 3);
        font-size: 0.95rem;
      }
      
      .btn-autoevaluacion {
        font-size: 1.1rem;
        padding: calc(var(--spacing-unit) * 3.5) calc(var(--spacing-unit) * 6);
      }
      
      .feedback-titulo {
        font-size: 1.5rem;
      }
      
      .feedback-puntuacion {
        font-size: 2rem;
      }
    }
"""

def añadir_css(archivo):
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Buscar el cierre de </style>
    if '  </style>' in contenido:
        # Añadir CSS justo antes del cierre
        contenido = contenido.replace('  </style>', CSS_AUTOEVALUACION + '\n  </style>')
        print(f"✓ CSS añadido a {archivo}")
        
        with open(archivo, 'w', encoding='utf-8') as f:
            f.write(contenido)
        return True
    else:
        print(f"✗ No se encontró cierre de style en {archivo}")
        return False

if __name__ == '__main__':
    print("\n=== Añadiendo CSS de autoevaluación ===\n")
    
    archivos = [
        'S3_monomios.html',
        'S6_ecuaciones_multiplicacion.html',
        'S7_ecuaciones_parentesis.html'
    ]
    
    for archivo in archivos:
        print(f"📝 Procesando {archivo}...")
        if añadir_css(archivo):
            print(f"✅ {archivo} completado\n")
        else:
            print(f"❌ Error en {archivo}\n")
    
    print("=== FIN ===")
