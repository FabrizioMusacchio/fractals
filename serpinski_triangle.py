"""
A script to generate an animated gif of the Sierpinski triangle.

author: Fabrizio Musacchio (fabriziomusacchio.com)
date: Aug 2, 2021
"""
# %% IMPORTS
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# %% SIERPINSKI TRIANGLE
def sierpinski_triangle(ax, p1, p2, p3, depth=0):
    if depth == 0:
        ax.fill([p1[0], p2[0], p3[0]], [p1[1], p2[1], p3[1]], 'k')
    else:
        p12 = (p1 + p2) / 2
        p23 = (p2 + p3) / 2
        p31 = (p3 + p1) / 2
        
        sierpinski_triangle(ax, p1, p12, p31, depth - 1)
        sierpinski_triangle(ax, p12, p2, p23, depth - 1)
        sierpinski_triangle(ax, p31, p23, p3, depth - 1)

def update(frame):
    ax.clear()
    ax.set_aspect('equal')
    ax.axis('off')
    
    depth = frame + 1
    sierpinski_triangle(ax, p1, p2, p3, depth)
    
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(-0.1, 1.1)
    plt.tight_layout()

# initialize the plot:
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axis('off')

# define the vertices of the initial triangle:
p1 = np.array([0, 0])
p2 = np.array([0.5, np.sqrt(3) / 2])
p3 = np.array([1, 0])

# set the number of animation frames (depth levels):
num_frames = 11

# create and save the animation:
anim = FuncAnimation(fig, update, frames=num_frames, interval=500)
anim.save('sierpinski_triangle_animation.gif', writer='imagemagick')
plt.show()
# %% END