import numpy as np
import matplotlib.pyplot as plt

#Condiciones
theta = 75
yo = 10
xo = 2
vo = 300
g = 10 

conv_grad = np.pi / 180
theta_rad = theta * conv_grad

vox = vo * np.cos(theta_rad)
voy = vo * np.sin(theta_rad)

def grafica(x,y,xo,yo):
    plt.figure(figsize=(6,4))
    plt.plot(x,y,lw=0.7, color="black")
    plt.scatter([xo],[yo],color="black")
    plt.xlabel('Distancia (m)', fontdict={"family" : "serif"}, fontsize=10)    
    plt.ylabel('Altura (m)', fontdict={"family" : "serif"}, fontsize=10)
    plt.title("Trayectoria del Proyectil", font="serif", fontsize=12)
    plt.grid(True)
    plt.show()

# Código para el Tiro Parabólico
if 0 < theta < 90:
    # 1. Tiempos (Usando la resolvente cuadrática para admitir cualquier altura inicial 'yo')
    # 0.5*g*t^2 - voy*t - yo = 0
    t_vuelo = (voy + np.sqrt(voy**2 + 2 * g * yo)) / g
    t_ascenso = voy / g
    
    # 2. Arrays de simulación para la gráfica
    t = np.linspace(0, t_vuelo, 100)
    
    # 3. Ecuaciones de posición (Vectores x e y para el plot)
    x = xo + vox * t
    y = yo + voy * t - 0.5 * g * t**2
    
    # 4. Datos máximos
    ymax = yo + (voy**2) / (2 * g)
    xmax = xo + vox * t_vuelo
    
    # 5. Velocidad y ángulo de impacto final
    vfx = vox # La velocidad en X es constante
    vfy = voy - g * t_vuelo # La velocidad en Y al momento de chocar
    vf = np.sqrt(vfx**2 + vfy**2)
    # Calculamos el ángulo con el que choca contra el suelo (en grados)
    angulo_impacto = np.degrees(np.arctan(abs(vfy) / vfx))
    
    # 6. Llamada a la función gráfica (¡Funcionará perfecto porque x e y son arrays de numpy!)
    grafica(x, y, xo, yo)
    
    # 7. Impresión de resultados en consola
    print("\n--- RESULTADOS DEL TIRO PARABÓLICO ---")
    print(f"Condiciones iniciales: {vo} m/s a {theta}° desde {yo} m de altura.")
    print(f"Tiempo de vuelo total: {t_vuelo:.2f} s")
    print(f"Tiempo en alcanzar la altura máxima: {t_ascenso:.2f} s")
    print(f"Altura máxima (Ymax): {ymax:.2f} m")
    print(f"Alcance horizontal máximo (Xmax): {xmax:.2f} m")
    print(f"Velocidad de impacto: {vf:.2f} m/s")
    print(f"Ángulo de impacto contra el suelo: {angulo_impacto:.2f}°\n")
else:
    print("Por favor, ingresa un ángulo entre 0 y 90 grados.")


 
