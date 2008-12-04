
class Graph:

	def __init__(self):
		self.nodes = []
		self.edges = []

	def add_node(self, val):
		node = Node(val)
		self.nodes.append(node)

		return node

	def add_edge(self, n1, n2):
		edge = Edge(n1, n2)
		self.edges.append(edge)

		return edge

class Node:
	
	def __init__(self, val):
		self.val = val
		self.neighbor = []
		self.degree = 0

		self.loc = [0.0, 0.0]
		self.disp = [0.0, 0.0]

	def add_neighbor(self, node):
		self.neighbor.append(node)
		self.degree += 1
	
class Edge:
	
	def __init__(self, n1, n2):
		self.nodes = [n1, n2]

		n1.add_neighbor(n2)
		n2.add_neighbor(n1)

