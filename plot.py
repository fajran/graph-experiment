
import Image
import ImageDraw

class Plot:

	def __init__(self, output, w, h):
		
		self.w = w
		self.h = h
		self.output = output

		self.im = Image.new('RGB', (w,h))
		self.draw = ImageDraw.Draw(self.im)
		self.draw.rectangle([(0,0),(w,h)], fill='#FFFFFF')

	def draw_edge(self, p1, p2):
		
		self.draw.line([p1, p2], fill='#0000FF', width=5)

	def draw_node(self, pos):
		x = pos[0]
		y = pos[1]

		w = 20
		h = 20

		x1 = x-w/2
		y1 = y-h/2
		x2 = x1 + w
		y2 = y1 + h

		self.draw.ellipse([(x1,y1),(x2,y2)], fill='#FF0000')
	
	def save(self):
		self.im.save(self.output, 'PNG')

class PlotGraph:
	def __init__(self, graph, output, w, h):
		self.output = output
		self.graph = graph
		self.w = w
		self.h = h
		self.plotter = Plot(output, w, h)

	def plot(self):
		for edge in self.graph.edges:
			self.draw_edge(edge)
	
		for node in self.graph.nodes:
			self.draw_node(node)

		self.plotter.save()

	def draw_node(self, node):
		pos = (int(node.loc[0]), int(node.loc[1]))
		self.plotter.draw_node(pos)

	def draw_edge(self, edge):

		x1 = int(edge.nodes[0].loc[0])
		y1 = int(edge.nodes[0].loc[1])
		x2 = int(edge.nodes[1].loc[0])
		y2 = int(edge.nodes[1].loc[1])

		self.plotter.draw_edge((x1,y1),(x2,y2))

		


