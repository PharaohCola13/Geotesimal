# A Family of Pyramids, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

def shape(fig, alpha, color, edge_c, edge_w, rot_elev, rot_azim, grid, sides):
# Definition of x
	def x_(u,v):
	    x = ((h - u) / h) * r * cos(v)
	    return x

# Definition of y
	def y_(u,v):
	    y = ((h - u)/h) * r * sin(v)
	    return y

# Definition of z
	def z_(u,v):
	    z = u
	    return z

# Height
	h = 1

# Radius
	r = 1

# Number of edges on the base
	s = sides

# Value of the angles
	u = linspace(0, h, 100)
	v = linspace(0, 2 * pi, s + 1)

	u, v = meshgrid(u, v)

# Symbolic representation
	x = x_(u,v)
	y = y_(u,v)
	z = z_(u,v)

# Figure Properties

	ax = p3.Axes3D(fig)
	ax.set_facecolor('black') # Figure background turns black

# Axis Properties
	plt.axis(grid) # Turns off the axis grid
	plt.axis('equal')

# Axis Limits
	ax.set_xlim(-1 * r,r)
	ax.set_ylim(-1 * r,r)
	ax.set_zlim(0,h)

# Surface Plot
	pyramid = ax.plot_surface(x,y,z)

	pyramid.set_alpha(alpha) # Transparency of figure
	pyramid.set_edgecolor(edge_c) # Edge color of the lines on the figure
	pyramid.set_linewidth(edge_w) # Line width of the edges
	pyramid.set_facecolor(color) # General color of the figure

# Definitions for animation
	def init():
	    return pyramid,

	def animate(i):
# azimuth angle : 0 deg to 360 deg
# elev = i * n --> rotates object about the xy-plane with a magnitude of n
# azim = i * n --> rotates object around the z axis with a magnitude of n
# For top view elev = 90
# For side view elev = 0

	    ax.view_init(elev=i, azim=i*4)
	    return pyramid,

# Animate
	ani = FuncAnimation(fig, animate, init_func=init,
	                    frames=100, interval=20, blit=False, repeat=True)
# Saving to s-Pyramid.mp4

	# Writer = writers['ffmpeg']
	# writer = Writer(fps=15, bitrate=1800)

	# name = '%s-Pyramid' % int(s)
	# ani.save('%s.mp4' % name, writer=writer)
