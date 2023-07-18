"""
A script to generate an animated gif of the Takagi function (Blancmange curve).
author: Fabrizio Musacchio (fabriziomusacchio.com)
date: Aug 2, 2021
"""
# %% IMPORTS
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# %% TAKAGI FUNCTION (BLANCMANGE CURVE) 1D
def phi(x):
    return np.abs(x - np.floor(x + 0.5)).astype(float)

def takagi(x, n):
    result = np.zeros_like(x, dtype=float)
    for i in range(n + 1):
        result = np.add(result, phi(2**i * x) / 2**i, out=result, casting="unsafe")
    return result

fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
line, = ax.plot([], [], lw=0.5)
ax.annotate(f'n = {0.0:.2f}', (0.05, 0.95), xycoords='axes fraction')

def init():
    line.set_data([], [])
    return line,

def update(frame):
    x = np.linspace(0, 1, 1000)
    y = takagi(x, frame + 1)
    line.set_data(x, y)
    # Annotate current n:
    ax.texts[0].set_text(f'n = {frame:.2f}')
    ax.set_title(f'Takagi function (Blancmange curve) with n = {frame:.2f}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
        
    return line

# Set up the animation and save as GIF:
anim = FuncAnimation(fig, update, frames=15, init_func=init, blit=True)
anim.save('images/takagi_animation.gif', writer='pillow', dpi=300)
plt.show()