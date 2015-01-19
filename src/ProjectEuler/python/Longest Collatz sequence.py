def collatzlength(num):
	n, count = num, 1
	while n > 1:
		count += 1
		if not n % 2:
			n = n/2
		else:
			n = 3*n + 1
	return (num, count)

if __name__ == '__main__':
	maxnum, maxlen = 999999,0
	for i in range(maxnum, 1, -1):
		(num, count) = collatzlength(i)
		if count > maxlen :
			maxlen = count
			maxnum = num
	print str(maxnum)