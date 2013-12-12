def divisorSum(num):
	sumDivisors = 0
	for n in range(1, num + 1/2):
		if not num % n:
			sumDivisors += n
	return sumDivisors

def checkAmicable(num):
	sumDivisors = 0
	for n in range(1, num + 1/2):
		if not num % n:
			sumDivisors += n
	return num == divisorSum(sumDivisors) and not sumDivisors == num

def getAmicableSum(num):
	total = 0
	for i in range(num + 1):
		if checkAmicable(i):
			total += i
	return total

if __name__ == '__main__':
	print (str(getAmicableSum(10000)))