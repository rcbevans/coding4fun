from math import sqrt, floor

class findDivisors:
	def isPrime(self, num):
		for i in range(2, int(floor(sqrt(num)) + 1)):
			if not num % i:
				return False
		return True

	def numDivisors(self, num):
		factors = {}
		numFactors = 2
		currNum = num
		currFactor = 2

		while not self.isPrime(currNum):
			if not currNum % currFactor:
				if currFactor not in factors:
					factors[currFactor] = 1
				else:
					factors[currFactor] += 1
				currNum = currNum / currFactor
			else:
				currFactor += 1

		if currNum not in factors:
			factors[currNum] = 1
		else:
			factors[currNum] += 1
			
		total = 1
		for key in factors:
			total *= factors[key] + 1

		return total

	def firstWithNDivisors(self, noDivisors):
		triGen = genTriangular()
		candidate = triGen.next()
		while self.numDivisors(candidate) < noDivisors:
			candidate = triGen.next()

		return candidate

def genTriangular():
	next = 1
	current = 0
	while True:
		current = next + current
		next += 1
		yield current

if __name__ == '__main__':
	fd = findDivisors()
	print fd.firstWithNDivisors(5)
