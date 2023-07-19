"""
A script to generate an animated gif of the Lotos flower.

author: Fabrizio Musacchio (fabriziomusacchio.com)
date: Jul 19, 2023
"""
# %% IMPORTS
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
# %% LOTOS FLOWER (STATIC)
def flower(num_petals):
    theta = np.linspace(0, 2.*np.pi, 1000)
    r = np.sin(num_petals * theta)
    return r * np.cos(theta), r * np.sin(theta)

x, y = flower(8)  # 8 petals
plt.figure(figsize=[8,8])
plt.plot(x, y, c='deeppink')
# remove the axis:
ax = plt.gca()
ax.set_axis_off()
plt.tight_layout()
plt.savefig('images/lotos_flower.png', dpi=300)
plt.show()
# %% LOTOS FLOWER WITH ANIMATION
fig, ax = plt.subplots(figsize=(8, 8))

x, y = [], []
line, = plt.plot([], [], c='deeppink')

def init():
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_axis_off()
    return line,

def flower(t):
    theta = np.linspace(0, 2.*np.pi, 1000)
    r = np.sin(8 * theta * t)
    return r * np.cos(theta), r * np.sin(theta)

def update(frame):
    x, y = flower(frame/100)
    line.set_data(x, y)
    return line,

ani = FuncAnimation(fig, update, frames=range(101), init_func=init, blit=True)
ani.save('images/lotos_flower.gif', writer='imagemagick')
plt.close(fig)
# %% LOTOS FLOWER WITH ANIMATION AND DESCRIPTION
fig, ax = plt.subplots(figsize=(8, 8))
x, y = [], []
line, = plt.plot([], [], c='deeppink')
text = plt.text(-0.99, 0.99, '', fontsize=12, color='slategrey')
plt.xlabel('X')
plt.ylabel('Y')

def init():
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_axis_off()
    return line, text

def flower(t):
    theta = np.linspace(0, 2.*np.pi, 1000)
    r = np.sin(8 * theta * t)
    return r * np.cos(theta), r * np.sin(theta)

def update(frame):
    x, y = flower(frame/100)
    line.set_data(x, y)
    # The theta value is changing continuously from 0 to 2π
    text.set_text(f'theta = 0 to 2π\nr = sin(8*theta*{frame/100})\nx = r*cos(theta)\ny = r*sin(theta)')
    return line, text

ani = FuncAnimation(fig, update, frames=range(101), init_func=init, blit=True)

ani.save('images/lotos_flower_2.gif', writer='imagemagick')
plt.close(fig)

""" x_tmp, y_tmp = flower(20/100)
plt.plot(x_tmp, y_tmp)
plt.show() """

# %% END