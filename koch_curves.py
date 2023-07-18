"""
A script to generate an animated gif of the Koch snowflake.

author: Fabrizio Musacchio (fabriziomusacchio.com)
date: Aug 2, 2021
"""
# %% IMPORTS
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
# %% KOCH SNOWFLAKE ANIMATION
def koch_snowflake(ax, p1, p2, depth=0):
    if depth == 0:
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color='b')
    else:
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        length = np.sqrt(dx**2 + dy**2)
        unit = length / 3.0
        angle = np.arctan2(dy, dx)

        p1_new = p1
        p2_new = [p1[0] + np.cos(angle) * unit, p1[1] + np.sin(angle) * unit]
        p3_new = [p2_new[0] + np.cos(angle - np.pi / 3) * unit, p2_new[1] + np.sin(angle - np.pi / 3) * unit]
        p4_new = [p1[0] + np.cos(angle) * 2 * unit, p1[1] + np.sin(angle) * 2 * unit]

        koch_snowflake(ax, p1_new, p2_new, depth - 1)
        koch_snowflake(ax, p2_new, p3_new, depth - 1)
        koch_snowflake(ax, p3_new, p4_new, depth - 1)
        koch_snowflake(ax, p4_new, p2, depth - 1)

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axis('off')

# initial points of the Koch snowflake:
p1 = [-0.5, -0.288]
p2 = [0.5, -0.288]
p3 = [0.0, 0.577]

depth = 5  # Set the desired depth of recursion

def update(frame):
    ax.clear()
    ax.set_aspect('equal')
    ax.axis('off')

    # calculate the new points for the current frame:
    new_p1 = p1
    new_p2 = p2
    new_p3 = p3

    # adjust the depth for each frame:
    current_depth = int(depth * (frame + 1) / 100.0)

    # Generate the Koch snowflake
    koch_snowflake(ax, new_p1, new_p2, current_depth)
    koch_snowflake(ax, new_p2, new_p3, current_depth)
    koch_snowflake(ax, new_p3, new_p1, current_depth)

    # set the plot limits:
    ax.set_xlim([-0.7, 0.7])
    ax.set_ylim([-0.7, 0.7])

    # annotate the depth in the plot:
    ax.text(0.02, 0.95, 'Depth: {}'.format(current_depth), transform=ax.transAxes, color='black', fontsize=12)

anim = FuncAnimation(fig, update, frames=120, interval=100)
anim.save('koch_snowflake_animation.gif', writer='pillow', fps=60)
plt.show()
# %% KOCH SNOWFLAKE ANIMATION W/ CHANGING COLORS
def koch_snowflake(ax, p1, p2, depth=0, color='b'):
    if depth == 0:
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=color)
    else:
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        length = np.sqrt(dx**2 + dy**2)
        unit = length / 3.0
        angle = np.arctan2(dy, dx)

        p1_new = p1
        p2_new = [p1[0] + np.cos(angle) * unit, p1[1] + np.sin(angle) * unit]
        p3_new = [p2_new[0] + np.cos(angle - np.pi / 3) * unit, p2_new[1] + np.sin(angle - np.pi / 3) * unit]
        p4_new = [p1[0] + np.cos(angle) * 2 * unit, p1[1] + np.sin(angle) * 2 * unit]

        # generate a random color for each recursion level:
        new_color = '#' + ''.join(random.choices('0123456789ABCDEF', k=6))

        koch_snowflake(ax, p1_new, p2_new, depth - 1, new_color)
        koch_snowflake(ax, p2_new, p3_new, depth - 1, new_color)
        koch_snowflake(ax, p3_new, p4_new, depth - 1, new_color)
        koch_snowflake(ax, p4_new, p2, depth - 1, new_color)

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axis('off')

# initial points of the Koch snowflake:
p1 = [-0.5, -0.288]
p2 = [0.5, -0.288]
p3 = [0.0, 0.577]

depth = 5  # set the desired depth of recursion

def update(frame):
    ax.clear()
    ax.set_aspect('equal')
    ax.axis('off')

    # calculate the new points for the current frame:
    new_p1 = p1
    new_p2 = p2
    new_p3 = p3

    # adjust the depth for each frame:
    current_depth = int(depth * (frame + 1) / 100.0)

    # generate the Koch snowflake:
    koch_snowflake(ax, new_p1, new_p2, current_depth)
    koch_snowflake(ax, new_p2, new_p3, current_depth)
    koch_snowflake(ax, new_p3, new_p1, current_depth)

    # set the plot limits:
    ax.set_xlim([-0.7, 0.7])
    ax.set_ylim([-0.7, 0.7])

    # annotate the depth in the plot:
    ax.text(0.02, 0.95, 'Depth: {}'.format(current_depth), transform=ax.transAxes, color='black', fontsize=12)

anim = FuncAnimation(fig, update, frames=100, interval=100)
anim.save('koch_snowflake_animation_color.gif', writer='pillow', fps=60)
plt.show()
# %% END