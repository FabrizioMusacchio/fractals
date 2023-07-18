"""
A script to generate an animated gif of the Mandelbrot set.

The first code is taken from the Matplotlib documentation website: https://matplotlib.org/matplotblog/posts/animated-fractals/?ssp=1&darkschemeovr=1&setlang=de-DE&safesearch=moderate

author: Fabrizio Musacchio (fabriziomusacchio.com)
date: Aug 2, 2021
"""
# %% IMPORTS
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import imageio
import os
# %% MANDELBROT SET ANIMATION (FROM MATPLOTLIB)
def mandelbrot(x, y, threshold):
    """Calculates whether the number c = x + i*y belongs to the 
    Mandelbrot set. In order to belong, the sequence z[i + 1] = z[i]**2 + c
    must not diverge after 'threshold' number of steps. The sequence diverges
    if the absolute value of z[i+1] is greater than 4.
    
    :param float x: the x component of the initial complex number
    :param float y: the y component of the initial complex number
    :param int threshold: the number of iterations to considered it converged
    """
    # initial conditions:
    c = complex(x, y)
    z = complex(0, 0)
    
    for i in range(threshold):
        z = z**2 + c
        if abs(z) > 4.:  # it diverged
            return i
        
    return threshold - 1  # it didn't diverge

x_start, y_start = -2, -1.5  # an interesting region starts here
width, height = 3, 3  # for 3 units up and right
density_per_unit = 250  # how many pixles per unit

# real and imaginary axis:
re = np.linspace(x_start, x_start + width, width * density_per_unit )
im = np.linspace(y_start, y_start + height, height * density_per_unit)

fig = plt.figure(figsize=(10, 10))  # instantiate a figure to draw
ax = plt.axes()  # create an axes object

def animate(i):
    ax.clear()  # clear axes object
    ax.set_xticks([], [])  # clear x-axis ticks
    ax.set_yticks([], [])  # clear y-axis ticks
    
    X = np.empty((len(re), len(im)))  # re-initialize the array-like image
    threshold = round(1.15**(i + 1))  # calculate the current threshold
    
    # iterations for the current threshold:
    for i in range(len(re)):
        for j in range(len(im)):
            X[i, j] = mandelbrot(re[i], im[j], threshold)
    
    # associate colors to the iterations with an iterpolation:
    img = ax.imshow(X.T, interpolation="bicubic", cmap='magma')
    plt.tight_layout()
    return [img]
 
anim = animation.FuncAnimation(fig, animate, frames=45, interval=120, blit=True)
anim.save('images/mandelbrot.gif',writer='imagemagick')
# %% MANDELBROT SET ANIMATION (FROM SCRATCH)
def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def mandelbrot_set(xmin,xmax,ymin,ymax,width,height,max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1,r2,np.array([[mandelbrot(complex(r, i),max_iter) for r in r1] for i in r2]))

images = []
n_frames = 82

for i in range(n_frames):
    dpi = 120
    img_width = 800
    img_height = 800
    fig = plt.figure(figsize=(img_width/dpi, img_height/dpi), dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1)

    # Adjust the coordinates for zooming effect
    if i < 36:
        xmin = -2.0+0.02*i
        xmax = -1.0+0.02*i
        ymin = -1.5+0.02*i
        ymax = 1.5-0.02*i
    else:
        xmin = (-2.0+0.02*35) + (0.01*(i-35))
        xmax = (-1.0+0.02*35) - (0.01*(i-35))
        ymin = (-1.5+0.02*35) + (0.01*(i-35))
        ymax = (1.5-0.02*35) - (0.01*(i-35))

    pixels = mandelbrot_set(xmin, xmax, ymin, ymax, 800, 800, 256)
    ax.imshow(pixels[2], origin="lower", cmap="jet")
    
    plt.xticks([])
    plt.yticks([])
    plt.tight_layout()

    # Check if the frames directory exists and create it if necessary:
    if not os.path.exists("mandelbrot_frames"):
        os.makedirs("mandelbrot_frames")
    plt.savefig("mandelbrot_frames/frame_{}.png".format(i))
    images.append(imageio.imread("mandelbrot_frames/frame_{}.png".format(i)))

# Ensure you have a directory called 'images/images' or adjust the path as needed
imageio.mimsave('images/mandelbrot_zoom.gif', images[:82])
# %% END