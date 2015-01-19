# Lattice Paths

from time import time

class PathFinder:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.Computed = [[-1 for x in range(width + 1)] for y in range(height + 1)] 

	def numberOfPossiblePaths(self, x, y):

		if not self.Computed[x][y] == -1:
			return self.Computed[x][y]

		if x < self.width and y < self.height:
			self.Computed[x][y] = self.numberOfPossiblePaths(x+1, y) + self.numberOfPossiblePaths(x, y+1)
		elif x < self.width:
			self.Computed[x][y] = self.numberOfPossiblePaths(x+1, y)
		elif y < self.height:
			self.Computed[x][y] = self.numberOfPossiblePaths(x, y+1)
		else:
			self.Computed[x][y] = 1

		return self.Computed[x][y]

if __name__ == '__main__':
	pf = PathFinder(100,100)
	start = time()
	print pf.numberOfPossiblePaths(0,0)
	fin = time()
	print "Took ", fin - start, "Secs"