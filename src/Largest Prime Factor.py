def largest_prime_factor(input, current_factor):
	while current_factor**2 < input:
		if input % current_factor:
			current_factor += 1
		else:
			return largest_prime_factor(input/current_factor, current_factor)
	return input

if __name__ == '__main__':
	print "Largest prime factor is " + str(largest_prime_factor(int(raw_input("Enter Input Number: ")), 2))