"""
A script to generate an animated gif of the Julia set.

The code for the JULIA SET 2 is taken from the Matlplotlib documentation 
website: https://matplotlib.org/matplotblog/posts/animated-fractals/?ssp=1&darkschemeovr=1&setlang=de-DE&safesearch=moderate

author: Fabrizio Musacchio (fabriziomusacchio.com)
date: Aug 2, 2021
"""
# %% IMPORTS
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# %% JULIA SET 1:
def julia_set(c, width, height, x_min, x_max, y_min, y_max, max_iter):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    img = np.zeros_like(Z, dtype=int)

    for i in range(max_iter):
        mask = np.abs(Z) < 4
        Z[mask] = Z[mask] ** 2 + c
        img += mask

    return img

# set up the figure and subplots:
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# common parameters:
width, height = 400, 400
x_min, x_max = -2.0, 2.0
y_min, y_max = -2.0, 2.0
c_values = np.linspace(-0.8, 0.8, 100)  # different values of the parameter 'c'
max_iter = 100

# plot 1 - full Julia set:
img1 = ax1.imshow(julia_set(c_values[0], width, height, x_min, x_max, y_min, y_max, max_iter),
                  cmap='RdPu', extent=(x_min, x_max, y_min, y_max), origin='lower')
ax1.set_title('Julia Set (Full)')
ax1.set_xlabel('Re(c)')
ax1.set_ylabel('Im(c)')

# plot 2 - zoomed-in Julia set:
zoom_factor = 0.5
zoom_x_min = x_max - (x_max - x_min) * zoom_factor
zoom_x_max = x_max
zoom_y_min = y_max - (y_max - y_min) * zoom_factor
zoom_y_max = y_max
img2 = ax2.imshow(julia_set(c_values[0], width, height, zoom_x_min, zoom_x_max, zoom_y_min, zoom_y_max, max_iter),
                  cmap='RdPu', extent=(zoom_x_min, zoom_x_max, zoom_y_min, zoom_y_max), origin='lower')
ax2.set_title('Julia Set (Zoomed)')
ax2.set_xlabel('Re(c)')
ax2.set_ylabel('Im(c)')

# update function:
def update(frame):
    # update plot 1 - full Julia set:
    img1.set_array(julia_set(c_values[frame], width, height, x_min, x_max, y_min, y_max, max_iter))
    ax1.set_title(f"c = {c_values[frame]:.2f}")

    # update plot 2 - zoomed-in Julia set:
    img2.set_array(julia_set(c_values[frame], width, height, zoom_x_min, zoom_x_max, zoom_y_min, zoom_y_max, max_iter))
    ax2.set_title(f"c = {c_values[frame]:.2f}")

# create and save the animation:
anim = FuncAnimation(fig, update, frames=len(c_values), interval=100)
anim.save('julia_set_animation.gif', writer='pillow', dpi=120)
plt.show()
# %% JULIA SET 2:
# define parameters:
x_start, y_start = -2, -2  # an interesting region starts here
width, height = 4, 4  # for 4 units up and right
density_per_unit = 200  # how many pixles per unit

# real and imaginary axis:
re = np.linspace(x_start, x_start + width, width * density_per_unit )
im = np.linspace(y_start, y_start + height, height * density_per_unit)

threshold = 20  # max allowed iterations
frames = 100  # number of frames in the animation

# we represent c as c = r*cos(a) + i*r*sin(a) = r*e^{i*a}:
r = 0.7885
a = np.linspace(0, 2*np.pi, frames)

fig = plt.figure(figsize=(10, 10))  # instantiate a figure to draw
ax = plt.axes()  # create an axes object

def julia_quadratic(zx, zy, cx, cy, threshold):
    """Calculates whether the number z[0] = zx + i*zy with a constant c = x + i*y
    belongs to the Julia set. In order to belong, the sequence 
    z[i + 1] = z[i]**2 + c, must not diverge after 'threshold' number of steps.
    The sequence diverges if the absolute value of z[i+1] is greater than 4.
    
    :param float zx: the x component of z[0]
    :param float zy: the y component of z[0]
    :param float cx: the x component of the constant c
    :param float cy: the y component of the constant c
    :param int threshold: the number of iterations to considered it converged
    """
    # initial conditions
    z = complex(zx, zy)
    c = complex(cx, cy)
    
    for i in range(threshold):
        z = z**2 + c
        if abs(z) > 4.:  # it diverged
            return i
        
    return threshold - 1  # it didn't diverge

def animate(i):
    ax.clear()  # clear axes object
    ax.set_xticks([], [])  # clear x-axis ticks
    ax.set_yticks([], [])  # clear y-axis ticks
    
    X = np.empty((len(re), len(im)))  # the initial array-like image
    cx, cy = r * np.cos(a[i]), r * np.sin(a[i])  # the initial c number
    
    # iterations for the given threshold
    for i in range(len(re)):
        for j in range(len(im)):
            X[i, j] = julia_quadratic(re[i], im[j], cx, cy, threshold)
    
    img = ax.imshow(X.T, interpolation="bicubic", cmap='magma')
    plt.tight_layout()
    return [img]

anim = animation.FuncAnimation(fig, animate, frames=frames, interval=50, blit=True)
anim.save('julia_set_animation_2.gif', writer='imagemagick')