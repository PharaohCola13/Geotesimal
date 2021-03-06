# A Octohedron, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *

name = "Octahedron"

def shape(fig, alpha, color, edge_c, edge_w, grid, figcolor, rotation, rotmagt, rotmagp, save):
	plt.clf()
# Points on the object
	points = array([
				   [1, 0, 0],
				   [0, 1, 0],
				   [0, 0, 1],
				   [-1, 0, 0],
				   [0, -1, 0],
				   [0, 0, -1]
				   ])

# Scaling Matricies
# 100%
	P = [
		[1, 0, 0],
	    [0, 1, 0],
	    [0, 0, 1]
		]

	Z = zeros((6,3))


	for i in range(6):
		Z[i,:] = dot(points[i,:],P)

# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor(figcolor) # Figure background turns black
	
# Axis Properties
	plt.axis(grid) # Turns off the axis grid
	plt.axis('equal')

# Axis Limits
	ax.set_xlim(-1, 1)
	ax.set_ylim(-1, 1)
	ax.set_zlim(-1, 1)

# The edges of the object
	verts = [
			[Z[0], Z[1], Z[3], Z[4], Z[0]],
			[Z[0], Z[2], Z[1]], 
			[Z[1], Z[2], Z[3]],
			[Z[3], Z[2], Z[4]],
			[Z[4], Z[2], Z[0]],
			[Z[0], Z[5], Z[1]], 
			[Z[1], Z[5], Z[3]],
			[Z[3], Z[5], Z[4]],
			[Z[4], Z[5], Z[0]]	
			]

# Surface plot
	octa = Poly3DCollection(verts)

	octa.set_edgecolor(edge_c)
	octa.set_linewidth(edge_w)
	octa.set_alpha(alpha)
	octa.set_facecolor(color)

	octahedron = ax.add_collection3d(octa)


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
