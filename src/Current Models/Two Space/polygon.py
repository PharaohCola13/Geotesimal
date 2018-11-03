import matplotlib.pyplot as plt
from matplotlib import *
from numpy import *
from matplotlib.animation import *


name = "Polygons"
def shape(fig, edge_c, edge_w, grid, sides, figcolor):
	
	def r_(u):
		r = 1/(cos((m/n) *arcsin(sin((n/o)*u+p))))
		return r

	n = sides
	m = 2
	o = 2
	p = 0.79


	u = linspace(0,2 * pi, sides+1)

	r = r_(u)

	ax = plt.subplot(111, projection='polar')
	ax.patch.set_facecolor(figcolor)
	ax.xaxis.set_tick_params(color="white", labelcolor="white")
	ax.yaxis.set_tick_params(color="white", labelcolor="white")

	plt.axis(grid)


	delt = plt.plot(u, r, color=edge_c, linewidth=edge_w)
