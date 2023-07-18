"""
A script to generate an animated gif of the Weierstrass function.

author: Fabrizio Musacchio (fabriziomusacchio.com)
date: Aug 2, 2021
"""
# %% IMPORTS
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from mpl_toolkits.mplot3d import Axes3D
# %% WEIERSTRASS FUNCTION 1D
# setting the ranges for calculation: 
b_start = -3
b_stop = 3
steps = 1000

# b for x axis. Here you can change start and stop points:
b = np.arange(b_start, b_stop, ((b_stop-b_start)/steps))

# defining the weierstrass function:
def weierstrass(x, Nvar, b):
    ws = np.zeros(steps)
    for n in range(0, Nvar):
        ws = ws + np.cos(b**n*np.pi*x)/2**n
    return ws

# plot/animate:
fig, ax = plt.subplots()
ax.set_xlim(b_start, b_stop)
line, = ax.plot(b, weierstrass(b, 500, 0.1))
ax.annotate(f'b = {0.1:.2f}', (0.05, 0.95), xycoords='axes fraction')

def update(b):
    line.set_ydata(weierstrass(b, 500, b))
    ax.texts[0].set_text(f'b = {b:.2f}')
    return line,

ani = FuncAnimation(fig, update, frames=np.linspace(0.1, 4, 100), interval=50)
writer = PillowWriter(fps=15)
ani.save('images/weierstrass_function.gif', writer=writer)
plt.show()
# %% WEIERSTRASS FUNCTION 2D (STATIC)
# setting the ranges for calculation:
b_start = -2
b_stop = 2
steps = 1000

# set b for x axis. Here you can change start and stop points:
x = np.linspace(b_start, b_stop, steps)
X, Y = np.meshgrid(x, x)

# defining the weierstrass function:
def weierstrass(x, y, Nvar):
    Z = np.zeros((steps, steps))
    for n in range(0, Nvar):
        Z += (0.5**n) * np.sin((7**n) * (np.pi * x)) * np.sin((7**n) * (np.pi * y))
    return Z

Z = weierstrass(X, Y, 20)

# plot:
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
plt.tight_layout()
plt.savefig('images/weierstrass_fractal.png', dpi=300)
plt.show()
# %% WEIERSTRASS FUNCTION 2D (ANIMATED)
# setting the ranges for calculation:
b_start = -2
b_stop = 2
steps = 1000

# set b for x axis. Here you can change start and stop points:
x = np.linspace(b_start, b_stop, steps)
X, Y = np.meshgrid(x, x)

# defining the weierstrass function:
def weierstrass(x, y, Nvar, b):
    Z = np.zeros((steps, steps))
    for n in range(0, Nvar):
        Z += (0.5**n) * np.sin((b**n) * (np.pi * x)) * np.sin((b**n) * (np.pi * y))
    return Z

# plot/animate:
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
ax.set_zlim(-1, 1)
surf = ax.plot_surface(X, Y, weierstrass(X, Y, 10, 1))
text = ax.text2D(0.05, 0.95, f"b = {1}", transform=ax.transAxes)

def update(b):
    ax.clear()
    ax.set_zlim(-1, 1)
    surf = ax.plot_surface(X, Y, weierstrass(X, Y, 10, b), cmap='viridis')
    text = ax.text2D(0.05, 0.95, f"b = {b:.2f}", transform=ax.transAxes)
    plt.tight_layout()
    return surf,

ani = FuncAnimation(fig, update, frames=np.linspace(1, 20, 200), interval=100)
writer = PillowWriter(fps=10)
ani.save('images/weierstrass_fractal.gif', writer=writer)
plt.show()