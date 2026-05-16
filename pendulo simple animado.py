import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Definimos las constantes del problema
m = 1
k = 1
b = 0.2

# Función posición del pendulo
t = np.linspace(0, 40, 500)
w_a = np.sqrt(k/m - (b/2*m)**2)
x = np.exp(-b/4*m *t) * np.cos(w_a * t)

# Grafico
fig, axis = plt.subplots(1, 2, figsize=(10,4)) # figura con 2 filas y una columna

animated_masa, = axis[0].plot([], [], "o", markersize=15, color="indigo") # importante la coma!!!!!
animated_resorte, = axis[0].plot([], [], color="black")

axis[0].set_xlim([-2, 2])
axis[0].set_ylim([-2, 2])
axis[0].grid()

animated_posición, = axis[1].plot([], [], color="green") # la coma!!!!!

axis[1].set_xlim([min(t), max(t)])
axis[1].set_ylim([-2, 2])
axis[1].grid()

# Función update que produce la animación
def update(frame):
    animated_masa.set_data([x[frame]], [0])
    animated_resorte.set_data([-2, x[frame]], [0, 0])

    animated_posición.set_data(t[:frame], x[:frame])

    return animated_masa, animated_resorte, animated_posición


animation = FuncAnimation(fig, update,interval=25)
plt.show()