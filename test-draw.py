#!/usr/bin/env python

from plot import Plot
import sys

if len(sys.argv) < 5:
	print "Usage: %s <edges.txt> <node-pos.txt> <w> <h>" % sys.argv[0]
	sys.exit(1)

w = int(sys.argv[3])
h = int(sys.argv[4])

plot = Plot("/tmp/graph.png", w, h)

pos = {}
f = open(sys.argv[2])
for line in f:
	(n, x, y) = line.strip().split(" ")
	x = int(float(x))
	y = int(float(y))

	pos[n] = (x,y)

f = open(sys.argv[1])
for line in f:
	(n1, n2) = line.strip().split(" ")
	plot.draw_edge(pos[n1], pos[n2])

for n in pos:
	plot.draw_node(pos[n])

plot.save()



