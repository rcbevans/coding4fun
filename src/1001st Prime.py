import math

def find_nth_prime(n):
	prime, counter = 3, 1
	while counter < n:
		if not filter(lambda x : not prime % x, [2] + range(3, int(math.sqrt(prime)) + 1, 2)):
			counter += 1
		prime += 2
	return prime -2 

if __name__ == '__main__':
	print str(find_nth_prime(10001))#int(raw_input("N: "))))