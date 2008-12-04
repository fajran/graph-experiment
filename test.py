#!/usr/bin/env python

from graph import Graph, Node, Edge
from layout.FruchtermanReingold import FruchtermanReingoldFDL
from plot import PlotGraph

w = 300
h = 300

g = Graph()
n1 = g.add_node(1)
n2 = g.add_node(2)
n3 = g.add_node(3)
g.add_edge(n1, n2)
g.add_edge(n2, n3)

layout = FruchtermanReingoldFDL(g, w, h)
layout.layout()

p = PlotGraph(g, '/tmp/graph.png', w, h)
p.plot()

