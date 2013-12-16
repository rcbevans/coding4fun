from math import sqrt, ceil

MAX_TERM = 1000000

def is_prime(num):
	if num == 2:
		return True
	if not num % 2:
		return False
	for i in range (3, int(ceil(sqrt(num+1))), 2):
		if not num % i:
			return False
	return True

def get_prime():
	num = 2
	yield num
	num += 1
	while(True):
		for i in range (3, int(ceil(sqrt(num+1))), 2):
			if not num % i:
				break
		else:
			yield num
		num += 2

if __name__ == '__main__':
	primeGen = get_prime()
	primes = []
	prime = primeGen.next()
	while prime < MAX_TERM:
		primes.append(prime)
		prime = primeGen.next()
	maxLen, maxPrime, currLen, candidate = 0,0,0,0
	for i in range(len(primes)):
		candidate = primes[i]
		currLen = 1
		for j in range(1, len(primes) - i):
			candidate += primes[i+j]
			currLen += 1
			if candidate > MAX_TERM:
				break
			elif is_prime(candidate) and currLen > maxLen:
				maxLen = currLen
				maxPrime = candidate

	print maxLen, maxPrime
