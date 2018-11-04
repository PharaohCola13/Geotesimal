# A Shell, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Shell"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides, edges, figcolor, rotation, rotmagt, rotmagp):
	plt.clf()
# Definition of x
	def x_(u,v):
		x = power(1.2, v) * (sin(u)**2 * sin(v))
		return x

# Definition of y
	def y_(u,v):
		y = power(1.2, v) * (sin(u)**2 * cos(v))
		return y

# Definition of z
	def z_(u,v):
		z = power(1.2, v) * (sin(u) * cos(u))
		return z

#Value of the angles
	s = sides
	u = linspace(0, pi, s + 1)
	v = linspace(-pi/4, 5 * pi/2, edges)

	u, v = meshgrid(u, v)

# Symbolic representation
	x = x_(u,v)
	y = y_(u,v)
	z = z_(u,v)

# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor(figcolor) # Figure background turns black

# Axis Properties
	plt.axis(grid) # Turns off the axis grid
	plt.axis('equal')

# Axis Limits
	#ax.set_xlim(-1,1)
	#ax.set_ylim(-1,1)
	#ax.set_zlim(-1,1)

# Surface Plot
	shell = ax.plot_surface(x, y, z)

	shell.set_alpha(alpha) # Transparency of figure
	shell.set_edgecolor(edge_c) # Edge color of the lines on the figure
	shell.set_linewidth(edge_w) # Line width of the edges
	shell.set_facecolor(color) # General color of the figure


	def rot_on():
		def animate(i):
			ax.view_init(azim=rotmagt * i, elev=rotmagp * i)

		# Animate
		ani = FuncAnimation(fig, animate,
							interval=1, save_count=50)  # frames=100)#, repeat=True)

		plt.ion()
		plt.show()
		time.sleep(0)
		plt.close()


	if rotation == "On":
		rot_on()
	elif rotation == "Off":
		pass

