# A Boy's Surface, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from fractions import Fraction

name = "Boy's Surface"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi, figcolor, rotation, rotmagt, rotmagp, save):
	plt.clf()
# Definition of x
	def x_(u, v):
		x = (cos(u) * (Fraction(1,3) * sqrt(2) * cos(u) * cos(2 * v) + Fraction(2,3) * sin(u) * cos(v))) / (1 - sqrt(2) * sin(u) * cos(u) * sin(3 * v))
		return x

# Definition of y
	def y_(u, v):
		y = (cos(u) * (Fraction(1,3) * sqrt(2) * cos(u) * sin(2 * v) - Fraction(2,3) * sin(u) * sin(v))) / (1 - sqrt(2) * sin(u) * cos(u) * sin(3 * v))
		return y


# Definition of z
	def z_(u, v):
		z = cos(u)**2 / (1 - sqrt(2) * sin(u) * cos(u) * sin(3 * v)) - 1
		return z

# Value of the angles
	u = linspace(0, multi_pi * pi, sides + 1)
	v = linspace(0, multi_pi * pi, edges)

	u, v = meshgrid(u, v)

# Symbolic representation
	x = x_(u, v)
	y = y_(u, v)
	z = z_(u, v)

# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor(figcolor)  # Figure background turns black

# Axis Properties
	plt.axis(grid)  # Turns off the axis grid
	plt.axis('equal')

# Axis Limits
	ax.set_xlim(-1, 1)
	ax.set_ylim(-1, 1)
	ax.set_zlim(-1, 1)

# Surface Plot
	boys_surf = ax.plot_surface(x, y, z)

	boys_surf.set_alpha(alpha)  # Transparency of figure
	boys_surf.set_edgecolor(edge_c)  # Edge color of the lines on the figure
	boys_surf.set_linewidth(edge_w)  # Line width of the edges
	boys_surf.set_facecolor(color)  # General color of the figure

	def rot_on():
		def animate(i):
			ax.view_init(azim=rotmagt * i, elev=rotmagp * i)

		if save == "MP4":
			# Animate
			ani = FuncAnimation(fig, animate, frames=500,
								interval=100, save_count=50)  # frames=100)#, repeat=True)

			Writer = writers['ffmpeg']
			writer = Writer(fps=30, bitrate=1800)
			ani.save('{}.mp4'.format(name), writer=writer)
		else:
			#save = None
			# Animate
			ani = FuncAnimation(fig, animate,
								interval=1, save_count=50)  # frames=100)#, repeat=True)
			pass


		plt.ion()
		plt.show()
		time.sleep(0)
		plt.close()

	if rotation == "On":
		rot_on()
	elif rotation == "Off":
		pass