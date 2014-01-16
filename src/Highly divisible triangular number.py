from math import sqrt, floor
from time import time

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

		while currNum > 1:
			if not currNum % currFactor:
				if currFactor not in factors:
					factors[currFactor] = 1
				else:
					factors[currFactor] += 1
				currNum = currNum / currFactor
			else:
				currFactor += 1
			
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


class findDivisors2:
	def __init__(self):
		self.primes = self.initPrimes(10000)

	def initPrimes(self, num):
		candidate = 3
		primes = [2]
		while len(primes) < num:
			if self.isPrime(candidate):
				primes.append(candidate)
			candidate += 1
		return primes

	def isPrime(self, num):
		for i in range(2, int(floor(sqrt(num)) + 1)):
			if not num % i:
				return False
		return True

	def primeGen(self):
		index = 0
		while index < len(self.primes):
			yield self.primes[index]
			index += 1

	def factorize(self, num):
		factors = {}
		curr = num
		pg = self.primeGen()
		i = pg.next()
		while curr > 1:
			if not curr % i:
				self.addfactor(factors, i)
				curr = curr / i
			else:
				i = pg.next()
		return factors

	def addfactor(self, factor, n):
		if n not in factor:
			factor[n] = 1
		else:
			factor[n] += 1

	def firstWithNDivisors(self, num):
		gt = genTriangular()
		candidate = gt.next()
		noDivisors = -1
		while noDivisors < num:
			candidate = gt.next()
			factors = self.factorize(candidate)
			total = 1
			for key in factors:
				total *= factors[key] + 1
			noDivisors = total
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
	start = time()
	res = fd.firstWithNDivisors(500)
	fin = time()
	t1 = fin - start
	print "Took", t1, "s", res
	fd2 = findDivisors2()
	start = time()
	res2 = fd2.firstWithNDivisors(500)
	fin = time()
	t2 = fin - start
	print "Took", t2, "s", res
