if __name__ == '__main__':
	print sum(filter(lambda x : x == sum(map(lambda n: int(n)**5, list(str(x)))), range(2, 200000)))