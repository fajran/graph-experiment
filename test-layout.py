#!/usr/bin/env python

from graph import Graph
from layout.FruchtermanReingold import FruchtermanReingoldFDL

import sys

if len(sys.argv) < 2:
	print "Usage: %s <edges.txt> [w] [h]" % sys.argv[0]
	sys.exit(1)

w = 400
h = 400

try:
	w = int(sys.argv[2])
except:
	pass

try:
	h = int(sys.argv[3])
except:
	pass

graph = Graph()

nodes = {}

f = open(sys.argv[1])
for line in f:
	p = line.strip().split(" ")

	n1 = nodes.get(p[0], None)
	if not n1:
		n1 = graph.add_node(p[0])
		nodes[p[0]] = n1

	n2 = nodes.get(p[1], None)
	if not n2:
		n2 = graph.add_node(p[1])
		nodes[p[1]] = n2

	graph.add_edge(n1, n2)

layout = FruchtermanReingoldFDL(graph, w, h)
layout.layout()

for node in graph.nodes:
	print node.val, node.loc[0], node.loc[1]

