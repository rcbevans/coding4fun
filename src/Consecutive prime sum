from math import sqrt, ceil

def is_prime(num):
	if num == 2:
		return True
	if not num % 2:
		return False
	for i in range (3, int(ceil(sqrt(num))), 2):
		if not num % i:
			return False
	return True

def get_prime():
	num = 2
	yield num
	num += 1
	while(True):
		for i in range (3, int(ceil(sqrt(num))), 2):
			if not num % i:
				break
		else:
			yield num
		num += 2

if __name__ == '__main__':
	primeGen = get_prime()
	currentPrime, prevPrime, numConsec, runConsec, maxPrime, maxLen = 0, 0, 0, 0, 0, 0
	while (currentPrime < 100):
		prevPrime = currentPrime
		currentPrime = primeGen.next()
		runConsec += prevPrime
		print "prevPrime " + str(prevPrime) + " current Prime" + str(currentPrime) + " runConsec " + str(runConsec)
		if is_prime(runConsec) and runConsec == currentPrime:
			numConsec += 1
		else:
			if numConsec > maxLen:
				maxLen = numConsec
				maxPrime = prevPrime
			numConsec = 0
			runConsec = prevPrime
	print "maxLen " + str(maxLen) + " prime " + str(maxPrime)