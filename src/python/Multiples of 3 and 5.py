if __name__ == '__main__':
	print "Sum is " + str(sum(filter(lambda n : (n % 3 == 0) or (n % 5 == 0), range(int(raw_input("Enter max range: "))))))