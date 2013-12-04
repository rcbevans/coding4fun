def sum_of_even_fibonacci(max_term):
	fibonacci = [1, 2]
	while fibonacci[-1] < max_term:
		fibonacci.append(fibonacci[-1] + fibonacci[-2])
	return sum(filter(lambda x : not x % 2, fibonacci))

if __name__ == '__main__':
	print "Sum is " + str(sum_of_even_fibonacci(int(raw_input("Max Term: "))))