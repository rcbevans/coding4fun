from math import sqrt

def special_triple():
	for a in range(3, 500):
		for b in range(a, 500):
			c = sqrt(a**2 + b**2)
			if c > b and not c % 1 and a + b + c == 1000:
					return int(a*b*c)

if __name__ == '__main__':
	print str(special_triple())