from time import time

class MaxPath:
	def __init__(self, pyramid):
		self.pyramid = pyramid
		self.maxPathFound = []
		for i in range(len(pyramid)):
			self.maxPathFound.append([-1 for x in range(i+1)])

	def findMaxPath(self, i, j):
		if not self.maxPathFound[i][j] == -1:
			return self.maxPathFound[i][j]

		if i == len(self.pyramid) - 1:
			self.maxPathFound[i][j] = self.pyramid[i][j]
		else:
			self.maxPathFound[i][j] = self.pyramid[i][j] + max(self.findMaxPath(i+1, j), self.findMaxPath(i+1, j+1))

		return self.maxPathFound[i][j]

if __name__ == '__main__':
	
	'''
	Trivial Case

	pyramid = [[3],
[7, 4],
[2, 4, 6],
[8, 5, 9, 3]]
	print pyramid
	'''

	'''
	Problem 18
	pyramid = [[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 04, 82, 47, 65],
[19, 01, 23, 75, 03, 34],
[88, 02, 77, 73, 07, 63, 67],
[99, 65, 04, 28, 06, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 04, 23]]
	'''

	'''
	Problem 67 
	'''
	pyramid = []
	count = 0
	with open("triangle.txt", "rb") as f:
		for i in f.readlines():
			pyramid.append([])
			for value in i.strip().split(" "):
				pyramid[count].append(int(value))
			count += 1

	mp = MaxPath(pyramid)
	start = time()
	print mp.findMaxPath(0,0)
	finish = time()
	print "Solved in ", finish - start, "s"