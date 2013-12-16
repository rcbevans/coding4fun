def distinct_powers(amin, amax, bmin, bmax):
	powers = []
	for power in [base**pwr for base in range(amin, amax+1) for pwr in range(bmin, bmax+1)]:
		if not power in powers:
			powers.append(power)
	return len(powers)

if __name__ == '__main__':
	print distinct_powers(2, 100, 2, 100)