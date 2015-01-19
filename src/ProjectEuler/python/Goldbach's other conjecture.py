from math import sqrt, ceil
def get_prime():
	num = 2
	while(True):
		for i in range (2, int(ceil(sqrt(num)))):
			if not num % i:
				break
		else:
			yield num
		num += 1

if __name__ == '__main__':
	print is_prime(3)
	print is_prime(6)
	numbers = range(1, 10000)
	numbers = filter(lambda x : not is_prime(x) and x % 2, numbers)
	primes = filter(lambda x : is_prime(x), range(1, 10000))
	found = False
	print numbers
	for i in numbers:
		found = False
		for j in primes:
			if j < i:
				if not sqrt((i - j) / 2) % 1:
					found = True
					break
			else:
				break
		else:
			print "Not found for " + str(i)
		if not found:
			print str(i)
			break
	else:
		print "Not found in given range"
	print "Done"