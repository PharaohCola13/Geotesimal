# A Cuboctahedron, brought to you by PharaohCola13

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from matplotlib.text import Annotation
from mpl_toolkits.mplot3d.proj3d import proj_transform

name = "Small Stellated Dodecahedron"

def shape(fig, alpha, color, edge_c, edge_w, grid, figcolor, rotation, rotmagt, rotmagp, save):
	plt.clf()

	points = array([[0, 	0.5, -((sqrt(5) - 1)/4)],
					[0, 	0.5, ((sqrt(5) - 1)/4)],
					[0, 	-0.5, -((sqrt(5) - 1)/4)],
					[0, 	-0.5, ((sqrt(5) - 1)/4)],
					[0.5, 	-((sqrt(5) - 1)/4), 0],
					[-0.5, 	-((sqrt(5) - 1)/4), 0],
					[0.5, 	((sqrt(5) - 1)/4), 0],
					[-0.5, 	((sqrt(5) - 1)/4), 0],
					[-((sqrt(5) - 1)/4),0, 0.5],
					[-((sqrt(5) - 1)/4),0, -0.5],
					[((sqrt(5) - 1)/4),0, 0.5],
					[((sqrt(5) - 1)/4),0, -0.5],
])

	# Scaling Matricies
	P = [[1, 0, 0],
		 [0, 1, 0],
		 [0, 0, 1]]

	Z = zeros((12, 3))

	for i in range(12):
		Z[i, :] = dot(points[i, :], P)

	# Figure Properties
	ax = p3.Axes3D(fig)
	ax.set_facecolor(figcolor)

	plt.axis(grid)

	ax.set_xlim(-1, 1)
	ax.set_ylim(-1, 1)
	ax.set_zlim(-1, 1)

	verts = [	[Z[0], Z[2],  Z[7],  Z[11], Z[5]],
				   	[Z[0], Z[5],  Z[1],  Z[9],  Z[8]],
					[Z[0], Z[8],  Z[6],  Z[7],  Z[10]],
					[Z[1], Z[3],  Z[6],  Z[8],  Z[4]],
					[Z[1], Z[4],  Z[0],  Z[10], Z[11]],
					[Z[1], Z[11], Z[7],  Z[6],  Z[9]],
					[Z[2], Z[0],  Z[4],  Z[9],  Z[6]],
					[Z[2], Z[6],  Z[3],  Z[11], Z[10]],
					[Z[2], Z[10], Z[5],  Z[4],  Z[8]],
					[Z[3], Z[1],  Z[5],  Z[10], Z[7]],
					[Z[3], Z[7],  Z[2],  Z[8],  Z[9]],
					[Z[3], Z[9],  Z[4],  Z[5],  Z[11]]
				]
	
	ssdod = Poly3DCollection(verts)

	ssdod.set_edgecolor(edge_c)
	ssdod.set_linewidth(edge_w)
	ssdod.set_alpha(alpha)
	ssdod.set_facecolor(color)

	# Plot Surfaces
	ax.add_collection3d(ssdod)

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
