import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Configuración general
plt.style.use('seaborn-v0_8-whitegrid')
output_folder = "" # Dejar vacío si es la misma carpeta

def guardar_plot(nombre):
    plt.tight_layout()
    plt.savefig(f"{output_folder}{nombre}.png", dpi=100)
    plt.close()
    print(f"Generado: {nombre}.png")

# --- SESIÓN 1: Rampa de Botadura (Astilleros) ---
def plot_sesion1():
    fig, ax = plt.subplots(figsize=(8, 4))
    
    # Triángulo (Rampa)
    x = [0, 10, 10, 0]
    y = [0, 0, 3, 0] # Pendiente suave
    
    ax.add_patch(patches.Polygon(xy=list(zip(x, y)), closed=True, color='#FF5733', alpha=0.3))
    ax.plot(x, y, color='black', linewidth=2)
    
    # Etiquetas
    ax.text(5, -0.5, 'Cateto Adyacente (Distancia horizontal)', ha='center')
    ax.text(10.2, 1.5, 'Cateto\nOpuesto\n(Altura)', va='center')
    ax.text(5, 1.8, 'Hipotenusa (Rampa del buque)', rotation=16, ha='center', color='darkred')
    
    # Ángulo
    arc = patches.Arc((0, 0), 3, 3, theta1=0, theta2=16.7, color='blue', linewidth=2)
    ax.add_patch(arc)
    ax.text(2, 0.3, r'$\alpha$', fontsize=14, color='blue')
    
    ax.set_title("Modelización: Rampa de Astillero en Barreras")
    ax.set_aspect('equal')
    ax.axis('off')
    guardar_plot("sesion1_rampa")

# --- SESIÓN 2: Cercha Nave Industrial ---
def plot_sesion2():
    fig, ax = plt.subplots(figsize=(6, 4))
    # Triángulo isósceles (Estructura techo)
    x = [0, 5, 10]
    y = [0, 3, 0]
    ax.plot(x + [0], y + [0], 'k-', linewidth=2)
    ax.plot([5, 5], [0, 3], 'r--', label='Altura (h)') # Altura
    
    # Ángulos notables
    ax.text(1, 0.2, r'$30^\circ$', fontsize=12)
    ax.text(9, 0.2, r'$30^\circ$', fontsize=12)
    
    ax.set_title("Estructura Metálica: Nave en Balaídos")
    ax.axis('off')
    guardar_plot("sesion2_cercha")

# --- SESIÓN 3: Radar Marítimo (Cíes) ---
def plot_sesion3():
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'projection': 'polar'})
    
    # Puntos cardinales
    ax.set_xticklabels(['E', 'NE', 'N', 'NO', 'O', 'SO (Cíes)', 'S', 'SE'])
    
    # Barco en 3er Cuadrante (aprox 225 grados)
    theta = np.deg2rad(225)
    r = 0.8
    ax.plot(theta, r, 'ro', markersize=10, label='Barco')
    ax.annotate("Barco detectado\n(-x, -y)", xy=(theta, r), xytext=(theta, r+0.2), ha='center')
    
    # Relleno del cuadrante
    theta_range = np.linspace(np.pi, 1.5*np.pi, 100)
    ax.fill_between(theta_range, 0, 1, color='blue', alpha=0.1)
    
    ax.set_title("Radar de Navegación: Cuadrante III")
    guardar_plot("sesion3_radar")

# --- SESIÓN 4: Luces de Navidad (Simetría) ---
def plot_sesion4():
    fig, ax = plt.subplots(figsize=(6, 6))
    theta = np.linspace(0, 2*np.pi, 100)
    ax.plot(np.cos(theta), np.sin(theta), 'k--', alpha=0.5) # C. Goniométrica
    
    # Ángulos simétricos (ej: 45, 135, 225, 315)
    angulos = [45, 135, 225, 315]
    colors = ['red', 'green', 'blue', 'orange']
    
    for ang, col in zip(angulos, colors):
        rad = np.deg2rad(ang)
        ax.plot([0, np.cos(rad)], [0, np.sin(rad)], color=col, marker='o')
        ax.text(np.cos(rad)*1.2, np.sin(rad)*1.2, f"{ang}°", color=col, ha='center')

    ax.set_title("Diseño de Simetrías: Luces de Navidad")
    ax.set_aspect('equal')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(False)
    guardar_plot("sesion4_luces")

# --- SESIÓN 5: Doble Observación (Rande) ---
def plot_sesion5():
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # Puntos
    torre_x, torre_y = 10, 8
    obs1_x, obs2_x = 0, 4
    
    # Dibujo
    ax.plot([torre_x, torre_x], [0, torre_y], 'k-', linewidth=3, label="Pilar Puente") # Torre
    ax.plot([0, 12], [0, 0], 'k-') # Suelo
    
    # Visuales
    ax.plot([obs1_x, torre_x], [0, torre_y], 'b--')
    ax.plot([obs2_x, torre_x], [0, torre_y], 'g--')
    
    # Ángulos
    ax.text(1, 0.5, r'$\alpha_1$', color='blue', fontsize=12)
    ax.text(4.5, 0.5, r'$\alpha_2$', color='green', fontsize=12)
    
    ax.annotate("", xy=(obs1_x, -0.5), xytext=(obs2_x, -0.5), arrowprops=dict(arrowstyle='<->'))
    ax.text(2, -1, "Distancia conocida (d)", ha='center')
    
    ax.set_title("Doble Observación: Pilar Puente de Rande")
    ax.axis('off')
    guardar_plot("sesion5_rande")

# --- SESIÓN 6: Rescate Pesca 1 ---
def plot_sesion6():
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Escenario
    ax.plot([0, 0], [0, 10], 'k-', linewidth=3) # Acantilado vertical
    ax.plot([0, 15], [0, 0], 'b-', linewidth=2) # Mar horizontal
    
    # Coordenadas
    heli_x, heli_y = 0, 10
    batea_x, batea_y = 12, 0
    
    # Dibujos elementos
    ax.plot(heli_x, heli_y, 'ko', markersize=15, label="Pesca 1 (Heli)")
    # CORRECCIÓN AQUÍ: cambiado 'Ns' por 's' (square) y color 'brown'
    ax.plot(batea_x, batea_y, marker='s', color='brown', markersize=12, label="Batea")
    
    # Cable
    ax.plot([heli_x, batea_x], [heli_y, batea_y], 'r--', label="Cable")
    
    # Línea horizontal visual desde el helicóptero (para el ángulo de depresión)
    ax.plot([0, 12], [10, 10], 'k:', alpha=0.6) 
    
    # Cálculo del ángulo para el arco
    # El cable baja de (0,10) a (12,0). Dy=-10, Dx=12. 
    angle_rad = np.arctan2(-10, 12) # Ángulo negativo
    angle_deg = np.degrees(angle_rad) # Aprox -39.8 grados
    
    # Arco: dibujamos desde el cable (360 + angle_deg) hasta la horizontal (360)
    # Ejemplo: si el ángulo es -40, dibujamos de 320 a 360.
    arc = patches.Arc((0, 10), 5, 5, theta1=360+angle_deg, theta2=360, color='purple', linewidth=1.5)
    ax.add_patch(arc)
    ax.text(3.5, 9.2, "Ángulo de\ndepresión", fontsize=10, color='purple')

    ax.set_title("Simulación: Rescate Pesca 1")
    ax.legend(loc='upper right')
    ax.axis('equal')
    guardar_plot("sesion6_rescate")

if __name__ == "__main__":
    print("Generando gráficos...")
    plot_sesion1()
    plot_sesion2()
    plot_sesion3()
    plot_sesion4()
    plot_sesion5()
    plot_sesion6()
    print("¡Gráficos generados correctamente!")
