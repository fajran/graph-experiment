
import random
import math

class FruchtermanReingoldFDL:

	def __init__(self, graph, w, h):

		self.w = w
		self.h = h
		self.graph = graph
		self.max_iteration = 700
		self.EPSILON = 0.000001

		self.threshold = 0.000001

		# Force constant
		self.k = 0.75 * math.sqrt((w*h)/len(graph.nodes))

		# Initial position
		cx = w / 2.0
		cy = h / 2.0

		alpha = 0.1
		scaleW = alpha * w / 2.0
		scaleH = alpha * h / 2.0

		for node in graph.nodes:
			node.loc[0] = cx + random.uniform(0,1) * scaleW
			node.loc[1] = cy + random.uniform(0,1) * scaleH

	def layout(self):
		self.temp = self.w / 10.0

		for i in range(0, self.max_iteration):
			self.step(i)

			if self.temp < self.threshold:
				break

	def step(self, iteration):
		
		for node in self.graph.nodes:
			self.calc_repulsion(node)

		for edge in self.graph.edges:
			self.calc_attraction(edge)

		for node in self.graph.nodes:
			self.calc_position(node)

		self.cool(iteration)

		#print "iteration=%d, temperature=%f" % (iteration, self.temp)

	def calc_repulsion(self, node):

		node.disp[0] = 0.0
		node.disp[1] = 0.0
		
		for node2 in self.graph.nodes:
			
			xdelta = node.loc[0] - node2.loc[0]
			ydelta = node.loc[1] - node2.loc[1]

			length = max(self.EPSILON, math.sqrt(xdelta * xdelta + ydelta * ydelta))

			force = self.k * self.k / length

			node.disp[0] += xdelta / length * force
			node.disp[1] += ydelta / length * force

	def calc_attraction(self, edge):
		
		n1 = edge.nodes[0]
		n2 = edge.nodes[1]

		xdelta = n1.loc[0] - n2.loc[0]
		ydelta = n1.loc[1] - n2.loc[1]

		length = max(self.EPSILON, math.sqrt(xdelta * xdelta + ydelta * ydelta))

		force = length * length / self.k

		xdisp = xdelta / length * force
		ydisp = ydelta / length * force

		n1.disp[0] -= xdisp
		n1.disp[1] -= ydisp

		n2.disp[0] += xdisp
		n2.disp[1] += ydisp

	def calc_position(self, node):
		
		length = max(self.EPSILON, math.sqrt(node.disp[0] * node.disp[0] + node.disp[1] * node.disp[1]))

		xdisp = node.disp[0] / length * min(length, self.temp)
		ydisp = node.disp[1] / length * min(length, self.temp)

		node.loc[0] += xdisp
		node.loc[1] += ydisp

		# Check border
		border = self.w / 50.0

		x = node.loc[0]
		if x < border:
			x = border + random.uniform(0,1) * border * 2.0
		elif x > self.w - border:
			x = self.w - border - random.uniform(0,1) * border * 2.0

		y = node.loc[1]
		if y < border:
			y = border + random.uniform(0,1) * border * 2.0
		elif y > self.h - border:
			y = self.h - border - random.uniform(0,1) * border * 2.0

		node.loc[0] = x
		node.loc[1] = y

	def cool(self, iteration):
		self.temp *= (1.0 - float(iteration) / self.max_iteration)

