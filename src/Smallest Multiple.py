def smallest_multiple(max_divisor):
	current_max = max_divisor
	while False in map(lambda x : not current_max % x, range(1, max_divisor)):
		current_max += max_divisor
	return current_max

if __name__ == '__main__':
	print "Smallest multiple is " + str(smallest_multiple(int(raw_input("Enter Max Divisor: "))))