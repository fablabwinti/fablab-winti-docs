#!/usr/bin/env python

from __future__ import division
import sys
import random

# a simple disjoint set union data structure
class Equivalence():
	def __init__(self, count):
		self._reps = range(count)
	
	def _representative(self, i):
		if self._reps[i] == i: return i
		else:
			r = self._representative(self._reps[i])
			self._reps[i] = r
			return r
	
	def setequal(self, i, j):
		self._reps[self._representative(i)] = self._representative(j)
	
	def isequal(self, i, j):
		return self._representative(i) == self._representative(j)
	
	def equivalenceclass(self, i):
		r = self._representative(i)
		return [i for i in range(len(self._reps)) if self._representative(i) == r]
	
	def equivalenceclasses(self):
		return [self.equivalenceclass(i) for i in range(len(self._reps)) if self._representative(i) == i]

width = 32
height = 44

edges = []

# diagonal edges
diagedges = []
for y in range(height-1):
	for x in range(width-1):
		# '/' diagonal with 3/4 probability
		if random.getrandbits(2) == 0:
			edges.append((x+y*width, (x+1)+(y+1)*width))
		else:
			e = ((x+1)+y*width, x+(y+1)*width)
			edges.append(e)
			diagedges.append(e)

# multiply the '/' diagonal edges so that they are more likely to be chosen in the end
edges += 3*diagedges

# horizontal edges
for y in range(height):
	for x in range(width-1):
		edges.append((x+y*width, (x+1)+y*width))

# vertical edges
for y in range(height-1):
	for x in range(width):
		edges.append((x+y*width, x+(y+1)*width))

# decimate nodes
with open('dither32x44.raw', 'rb') as f:
	dither = f.read()
for i, d in enumerate(dither):
	if d != '\0':
		edges = [e for e in edges if e[0] != i and e[1] != i]

# mazeify
eq = Equivalence(width*height)
random.shuffle(edges)
mazeedges = []
for e in edges:
	if not eq.isequal(e[0], e[1]):
		eq.setequal(e[0], e[1])
		mazeedges.append(e)

# output
sys.stdout.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
sys.stdout.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="%.3fmm" height="%.3fmm" viewBox="0 0 %d %d">\n' % (154.0*(width-1)/(height-1), 154.0, width-1, height-1))
sys.stdout.write('<path style="fill: none; stroke: #F4F4F4; stroke-width: 0.3536; stroke-linecap: round; stroke-linejoin: round;" d="')
for e in mazeedges:
	sys.stdout.write('M %d,%d L %d,%d ' % (e[0] % width, e[0] // width, e[1] % width, e[1] // width))
sys.stdout.write('"/>\n</svg>\n')
