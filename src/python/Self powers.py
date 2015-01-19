if __name__ == '__main__':
	print str(sum(map(lambda x: x**x, range(1, 1000 + 1))))[-10::1]