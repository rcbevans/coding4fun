def factorial(num):
	fact = 1
	for i in range(num, 1, -1):
		fact *= i
	return fact

if __name__ == '__main__':
	print factorial(10)
	res = 0
	for c in str(factorial(100)):
		res += int(c)
	print res