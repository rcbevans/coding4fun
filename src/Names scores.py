if __name__ == '__main__':
	totalScore = 0
	for i, name in enumerate(sorted(file('names.txt', 'r').read().replace("\"", "").split(","))):
		totalScore += (i + 1) * sum(map(lambda x : ord(x) - 64, list(name)))
	print totalScore