import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_triangle(ax, base, height, title, label_base, label_height, label_hyp):
    # Puntos del triángulo
    pts = [[0, 0], [base, 0], [base, height]]
    
    # Dibujar polígono (triángulo)
    triangle = patches.Polygon(pts, closed=True, fill=True, color='lightblue', alpha=0.5, edgecolor='blue', linewidth=2)
    ax.add_patch(triangle)
    
    # Dibujar símbolo de ángulo recto
    rect_size = min(base, height) * 0.1
    rect_angle = patches.Rectangle((base - rect_size, 0), rect_size, rect_size, fill=False, edgecolor='black')
    ax.add_patch(rect_angle)
    
    # Dibujar arco del ángulo alfa
    arc_rad = min(base, height) * 0.2
    arc = patches.Arc((0, 0), arc_rad*2, arc_rad*2, angle=0, theta1=0, theta2=plt.np.degrees(plt.np.arctan(height/base)), color='red', linewidth=2)
    ax.add_patch(arc)
    ax.text(arc_rad*1.2, arc_rad*0.4, r'$\alpha$', color='red', fontsize=12)
    
    # Etiquetas de los lados
    ax.text(base/2, -height*0.1, label_base, ha='center', fontsize=10)
    ax.text(base + base*0.05, height/2, label_height, va='center', fontsize=10)
    ax.text(base/2 - base*0.05, height/2 + height*0.05, label_hyp, ha='center', fontsize=10, rotation=plt.np.degrees(plt.np.arctan(height/base)))
    
    # Configuración de los ejes
    ax.set_xlim(-base*0.2, base*1.2)
    ax.set_ylim(-height*0.2, height*1.2)
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')
    ax.set_title(title, fontsize=14, fontweight='bold')

# Configuración de la figura general
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Ejercicio 1: Escalera
draw_triangle(axs[0, 0], base=3, height=4, title='Ejercicio 1: Escalera', 
              label_base='3 m (Cateto Contiguo)', label_height='4 m (Opuesto)', label_hyp='5 m (Hipotenusa)')

# Ejercicio 2: Rampa (La escala visual está un poco exagerada para que se vea claro el ángulo)
draw_triangle(axs[0, 1], base=14.95, height=3, title='Ejercicio 2: Rampa (Altura exagerada)', 
              label_base='14.95 m (Contiguo)', label_height='1.2 m (Opuesto)', label_hyp='15 m (Hipotenusa)')

# Ejercicio 3: Obelisco
draw_triangle(axs[1, 0], base=20, height=21, title='Ejercicio 3: Obelisco', 
              label_base='20 m (Sombra/Contiguo)', label_height='21 m (Opuesto)', label_hyp='29 m (Distancia/Hipotenusa)')

# Ejercicio 4: Triángulo Genérico
draw_triangle(axs[1, 1], base=8, height=6, title='Ejercicio 4: Práctica Avanzada', 
              label_base='8 cm (Contiguo)', label_height='6 cm (Opuesto)', label_hyp='10 cm (Hipotenusa)')

plt.tight_layout()
plt.savefig('visualizaciones_sesion1.png', dpi=300)
print("Imagen generada con éxito: visualizaciones_sesion1.png")
