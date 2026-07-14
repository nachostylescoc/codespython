import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parámetros físicos
g = 9.81      # aceleración de gravedad (m/s^2)
L = 1.0       # longitud del péndulo (m)
b = 0.3       # coeficiente de amortiguación (viscoso, por unidad de masa)

# Condiciones iniciales
theta0 = 0.1
theta_dot0 = 0.0

# Sistema con término de amortiguación -b*theta_dot
def pendulo_amortiguado(t, y):
    theta, theta_dot = y
    dtheta_dt = theta_dot
    dtheta_dot_dt = -(g / L) * theta - b * theta_dot
    return [dtheta_dt, dtheta_dot_dt]

t_span = (0, 20)
t_eval = np.linspace(*t_span, 4000)
sol = solve_ivp(pendulo_amortiguado, t_span, [theta0, theta_dot0], t_eval=t_eval)

theta = sol.y[0]
theta_dot = sol.y[1]

plt.plot(theta, theta_dot)
plt.xlabel(r'$\theta$ (rad)')
plt.ylabel(r'$\dot{\theta}$ (rad/s)')
plt.title('Espacio de fase del péndulo')
plt.legend()
plt.grid(alpha=0.3)
#plt.show()

# Animación

from matplotlib.animation import FuncAnimation
 
# Para que la animación no tenga miles de cuadros, se sub-muestrea
paso = 5
theta_anim = theta[::paso]
theta_dot_anim = theta_dot[::paso]
n_frames = len(theta_anim)
 
fig, ax = plt.subplots()
ax.plot(theta, theta_dot, color='lightgray', lw=1)  # trayectoria completa de fondo
linea_estela, = ax.plot([], [], color='tab:blue', lw=2)   # estela ya recorrida
punto, = ax.plot([], [], 'o', color='tab:red', markersize=8)  # posición actual
 
ax.set_xlabel(r'$\theta$ (rad)')
ax.set_ylabel(r'$\dot{\theta}$ (rad/s)')
ax.set_title('Espacio de fase del péndulo')
ax.grid(alpha=0.3)
 
def init():
    linea_estela.set_data([], [])
    punto.set_data([], [])
    return linea_estela, punto
 
def update(frame):
    linea_estela.set_data(theta_anim[:frame+1], theta_dot_anim[:frame+1])
    punto.set_data([theta_anim[frame]], [theta_dot_anim[frame]])
    return linea_estela, punto
 
anim = FuncAnimation(fig, update, frames=n_frames, init_func=init,
                      interval=20, blit=True)
plt.show()
 