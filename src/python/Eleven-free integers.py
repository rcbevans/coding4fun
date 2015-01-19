from math import log

def get_nth_eleven_free_integer(n):
	count = 0
	candidate = 1
	while count < n:
		broken = False
		string = str(candidate)
		if len(string) == 1:
			count += 1
		elif len(string) == 2:
			if log(int(string), 11) % 1:
				count += 1
		else:
			for i in range(2, len(string) + 1, 1):
				for j in range(0, len(string) + 1 - i):
					substring = string[j:j+i]
					if not int(substring) == 0 and not int(substring) == 1 and not log(int(substring), 11) % 1.0:
						broken = True
						break
				if broken:
					break
			if not broken:
				count += 1
		candidate += 1
	return candidate - 1


if __name__ == '__main__':
	print str(get_nth_eleven_free_integer(int(raw_input("N: "))))