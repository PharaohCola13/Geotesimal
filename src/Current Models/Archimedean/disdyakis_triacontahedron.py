# A Disdyakis Triacontahedron, brought to you by PharaohCola13
import matplotlib
from matplotlib import *

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import *
from matplotlib.animation import *
from numpy import *

name = "Disdyakis Triacontahedron"

def shape(fig, alpha, color, edge_c, edge_w, grid, figcolor, rotation, rotmagt, rotmagp, save):
	plt.clf()

# Points on the object
	p = (1 + sqrt(5))/2
	points = array([
					[0,			0,			0],			#0 		

					[0, 		0, 			2*p**2], 	#1
					[p**2, 		0, 			p**3], 		#2
					[p, 		p**2, 		p**3],		#3

					[0, 		p, 			p**3],		#4
					[-p, 		p**2, 		p**3],		#5
					[-p**2, 	0, 			p**3], 		#6

					[-p, 		-p**2, 		p**3],		#7
					[0, 		-p, 		p**3], 		#8
					[p, 		-p**2, 		p**3], 		#9

					[p**3, 		p, 			p**2],		#10
					[p**2, 		p**2, 		p**2], 		#11
					[0, 		p**3, 		p**2],		#12

					[-p**2, 	p**2, 		p**2],		#13
					[-p**3, 	p, 			p**2], 		#14
					[-p**3, 	-p, 		p**2], 		#15

					[-p**2, 	-p**2, 		p**2],		#16
					[0, 		-p**3, 		p**2],		#17
					[p**2, 		-p**2, 		p**2], 		#18

					[p**3, 		-p, 		p**2], 		#19
					[p**3, 		0, 			p],			#20
					[p**2, 		p**3, 		p],			#21

					[-p**2, 	p**3, 		p],			#22
					[-p**3, 	0, 			p],			#23
					[-p**2,		-p**3, 		p],			#24

					[p**2, 		-p**3, 		p],			#25
					[2*p**2, 	0, 			0],			#26					
					[p**3, 		p**2, 		0],			#27

					[p, 		p**3, 		0],			#28
					[0, 		2*p**2, 	0],			#29
					[-p, 		p**3,		0],			#30
				
					[-p**3, 	p**2,		0],			#31
					[-2*p**2, 	0, 			0],			#32
					[-p**3, 	-p**2, 		0],			#33

					[-p, 		-p**3,		0],			#34				
					[0, 		-2*p**2,	0],			#35
					[p, 		-p**3, 		0], 		#36

					[p**3, 		-p**2, 		0],			#37
					[p**3, 		0, 			-p],		#38					
					[p**2, 		p**3, 		-p], 		#39

					[-p**2, 	p**3, 		-p],		#40
					[-p**3, 	0, 			-p],		#41
					[-p**2,		-p**3, 		-p],		#42
 					
					[p**2, 		-p**3, 		-p],		#43
					[p**3, 		p, 			-p**2],		#44
					[p**2, 		p**2, 		-p**2], 	#45

					[0, 		p**3, 		-p**2],		#46
					[-p**2, 	p**2, 		-p**2],		#47
					[-p**3, 	p, 			-p**2],		#48	
				
					[-p**3, 	-p, 		-p**2],		#49					
					[-p**2, 	-p**2, 		-p**2], 	#50					
					[0, 		-p**3, 		-p**2],		#51
					
					[p**2, 		-p**2, 		-p**2], 	#52					
					[p**3, 		-p, 		-p**2],		#53					
					[p**2, 		0, 			-p**3],		#54
					
					[p, 		p**2, 		-p**3],		#55
					[0,			p, 			-p**3],		#56
					[-p, 		p**2, 		-p**3],		#57	
				
					[-p**2,		0, 			-p**3],		#58			
					[-p, 		-p**2, 		-p**3],		#59					
					[0, 		-p, 		-p**3],		#60	
			
					[p,			-p**2, 		-p**3],		#61				
					[0, 		0, 			-2*p**2],	#62					
	])

# Scaling Matricies
# 100%
	P = [
		[1, 0, 0],
		[0, 1, 0],
		[0, 0, 1]
		]

	J = zeros((63,3))

	for i in range(63):
		J[i,:] = dot(points[i,:],P)

	ax = p3.Axes3D(fig)
	ax.set_facecolor(figcolor)

	plt.axis(grid)
	#plt.axis('equal')
	
	ax.set_xlim(-10,10)
	ax.set_ylim(-10,10)
	ax.set_zlim(-10,10)
# Radius
	r = [-1 ,1]

# Definition of x and y
	X, Y = np.meshgrid(r, r)

# The edges of the object
	verts = [
			[J[1],  J[2],  J[4]], 	[J[2],  J[3],  J[4]],	[J[2],  J[20], J[10]], #
			[J[2],  J[10], J[11]],	[J[2],  J[11], J[3]],	[J[3],  J[11], J[12]], #
			[J[3],  J[12], J[4]],	[J[20], J[26], J[27]],	[J[20], J[27], J[10]], #

			[J[10], J[27], J[11]],	[J[11], J[27], J[21]],	[J[11], J[21], J[12]], #
			[J[21], J[27], J[28]],	[J[12], J[21], J[28]],	[J[12], J[28], J[29]], #
			[J[1],  J[4],  J[6]],	[J[4],  J[12], J[5]],	[J[4],  J[5],  J[6]],  #

			[J[5],  J[12], J[13]],	[J[5],  J[13], J[6]],	[J[6],  J[13], J[14]], #
			[J[6],  J[14], J[23]],	[J[12], J[29], J[30]],	[J[12], J[30], J[22]], #
			[J[12], J[22], J[13]],	[J[13], J[22], J[31]],	[J[22], J[30], J[31]], #

			[J[13], J[31], J[14]],	[J[14], J[31], J[23]],	[J[23], J[31], J[32]], #
			[J[1],  J[6],  J[8]],	[J[6],  J[23], J[15]],	[J[6],  J[15], J[16]], #
			[J[6],  J[16], J[7]],	[J[6],  J[7],  J[8]],	[J[8],  J[7],  J[17]], #

			[J[7],  J[16], J[17]],	[J[23], J[32], J[33]],	[J[15], J[23], J[33]], #
			[J[16], J[15], J[33]],	[J[24], J[16], J[33]],	[J[34], J[24], J[33]], #
			[J[17], J[16], J[24]],	[J[17], J[24], J[34]],	[J[17], J[34], J[35]], #

			[J[1],  J[8],  J[2]],	[J[8],  J[17], J[9]],	[J[8],  J[9],  J[2]],  #
			[J[9],  J[17], J[18]],	[J[9],  J[18], J[2]],	[J[2],  J[18], J[19]], #
			[J[2],  J[19], J[20]],	[J[17], J[35], J[36]],	[J[17], J[36], J[25]], #

			[J[17], J[25], J[18]],	[J[18], J[25], J[37]],  [J[25], J[36], J[37]], #
			[J[19], J[18], J[37]],  [J[20], J[19], J[37]],  [J[20], J[37], J[26]], #
			[J[27], J[26], J[38]], 	[J[27], J[38], J[44]],  [J[27], J[44], J[45]], #
			
			[J[27], J[45], J[39]],  [J[27], J[39], J[28]],  [J[28], J[39], J[46]], #
			[J[28], J[46], J[29]],	[J[39], J[45], J[46]],  [J[38], J[54], J[44]], #
			[J[55], J[45], J[54]],  [J[45], J[44], J[54]],  [J[45], J[55], J[46]], #
			
			[J[46], J[55], J[56]],  [J[55], J[54], J[56]],  [J[56], J[54], J[62]], #
			[J[30], J[29], J[46]],  [J[30], J[46], J[40]],  [J[31], J[30], J[40]], #	
			[J[40], J[46], J[47]],  [J[31], J[40], J[47]],  [J[31], J[47], J[48]], #

			[J[31], J[48], J[41]],  [J[31], J[41], J[32]],  [J[46], J[56], J[57]], #
			[J[47], J[46], J[57]],  [J[47], J[57], J[58]],  [J[48], J[47], J[58]], #
			[J[41], J[48], J[58]],	[J[57], J[56], J[58]],  [J[58], J[56], J[62]], #

			[J[33], J[32], J[41]],  [J[33], J[41], J[49]],  [J[33], J[49], J[50]], #
			[J[33], J[50], J[42]],  [J[33], J[42], J[34]],  [J[34], J[42], J[51]], #
			[J[42], J[50], J[51]],  [J[35], J[34], J[51]],  [J[49], J[41], J[58]], #
			
			[J[50], J[49], J[58]],  [J[50], J[58], J[59]],  [J[51], J[50], J[59]], #
			[J[51], J[59], J[60]],  [J[59], J[58], J[60]],  [J[60], J[58], J[62]], #
			[J[36], J[35], J[51]],  [J[36], J[51], J[43]],  [J[37], J[36], J[43]], #
			
			[J[43], J[51], J[52]],  [J[37], J[43], J[52]],  [J[37], J[52], J[53]], #
			[J[37], J[53], J[38]],  [J[37], J[38], J[26]],  [J[51], J[60], J[61]], #
			[J[52], J[51], J[61]],	[J[52], J[61], J[54]],  [J[53], J[52], J[54]], #

			
			[J[38], J[53], J[54]],  [J[54], J[61], J[60]],	[J[54], J[60], J[62]], 		
	]

	hedron = Poly3DCollection(verts)

	hedron.set_edgecolor(edge_c)
	hedron.set_linewidth(edge_w)
	hedron.set_alpha(alpha)
	hedron.set_facecolor(color)

	hedron = ax.add_collection3d(hedron)


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


