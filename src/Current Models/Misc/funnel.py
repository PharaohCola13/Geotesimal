# A Funnel, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Funnel"

def shape(fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi, radiusm, height, figcolor, rotation, rotmagt, rotmagp, save):
	plt.clf()
    # Definition of x
	def x_(u, v):
		x = u * cos(v)
		return x

	# Definition of y
	def y_(u, v):
		y = u * sin(v)
		return y


	# Definition of z
	def z_(u, v):
		z = h * log1p(u)
		return z

	# Determines the total height of the funnel
	h = height

	# Defines the radius of the hole
	r = radiusm

	# Value of the angles
	s = sides
	u = linspace(r, pi, s + 1)
	v = linspace(0, 2 * pi, edges)

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
	ax.set_xlim(-r - h , r + h)
	ax.set_ylim(-r - h, r + h)
	ax.set_zlim(0, 2 * h)

	# Surface Plot
	funnel = ax.plot_surface(x, y, z)

	funnel.set_alpha(alpha)  # Transparency of figure
	funnel.set_edgecolor(edge_c)  # Edge color of the lines on the figure
	funnel.set_linewidth(edge_w)  # Line width of the edges
	funnel.set_facecolor(color)  # General color of the figure


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
