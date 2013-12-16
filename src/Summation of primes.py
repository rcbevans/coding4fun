import math

def primes_below(n):
	prime, total = 3, 2
	while prime < n:
		if not filter(lambda x : not prime % x, [2] + range(3, int(math.sqrt(prime)) + 1, 2)):
			total += prime
		prime += 2
	return total

if __name__ == '__main__':
	print str(primes_below(int(raw_input("N: "))))