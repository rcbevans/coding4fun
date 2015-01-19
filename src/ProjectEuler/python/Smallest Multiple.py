from math import sqrt, floor
from time import time

def smallest_multiple1(max_divisor):
	current_max = max_divisor
	while False in map(lambda x : not current_max % x, range(1, max_divisor)):
		current_max += max_divisor
	return current_max

def primeGen():
	yield 2
	yield 3
	n = 1
	while True:
		yield 6*n - 1
		yield 6*n + 1
		n += 1

def addfactor(factor, n):
	if n not in factor:
		factor[n] = 1
	else:
		factor[n] += 1

def factorize(num):
	factors = {}
	curr = num
	pg = primeGen()
	i = pg.next()
	while curr > 1:
		if not curr % i:
			addfactor(factors, i)
			curr = curr / i
		else:
			i = pg.next()
	return factors

def smallest_multiple2(max_divisor):
	currentFactors = {}
	for i in range(1, max_divisor + 1):
		factors = factorize(i)
		for factor in factors:
			if not factor in currentFactors:
				currentFactors[factor] = factors[factor]
			else:
				currentFactors[factor] = max(currentFactors[factor], factors[factor])

	result = 1
	for key in currentFactors:
		result *= key**currentFactors[key]

	return result


if __name__ == '__main__':
	maxDivisor = int(raw_input("Enter Max Divisor: "))
	start = time()
	print "Smallest multiple, old method, is " + str(smallest_multiple1(maxDivisor))
	fin = time()
	time1 = fin - start
	print "took", time1, "s"
	start = time()
	print "Smallest multiple, new method is " + str(smallest_multiple2(maxDivisor))
	fin = time()
	time2 = fin - start
	print "took", time2, "s"
	print "speedup of", time1/time2