def sum_square_diff(number):
	return square_of_sum(number) - sum_of_squares(number)

def square_of_sum(number):
	return sum(range(number))**2

def sum_of_squares(number):
	return sum(map(lambda x : x**2, range(number)))

if __name__ == '__main__':
	print "Difference is " + str(sum_square_diff(int(raw_input("Number of Natural Numbers: "))+1))