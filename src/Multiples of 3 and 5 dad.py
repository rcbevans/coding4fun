#for numbers 1..1000 step 1
#	if number % 3 == 0 or number % 5 == 0
#		total = total + number

if __name__ == '__main__':
	total = 0
	for i in range(1, 1000, 1):
		if not i % 3 or not i % 5:
			total += i
	print total
