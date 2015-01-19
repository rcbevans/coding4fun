def gen_n_digit_number(num_digits):
	num = []
	for i in range(num_digits):
		num.append('9')
	return int(''.join(num))

def is_palindrome(number):
	return str(number) == str(number)[::-1]

def largest_palindrome_product(num_digits):
	num1 = gen_n_digit_number(num_digits)
	num2 = gen_n_digit_number(num_digits)
	palindromes = []
	while num1 > gen_n_digit_number(num_digits - 1) and num2 > gen_n_digit_number(num_digits - 1):
		if is_palindrome(num1 * num2):
			palindromes.append(num1 * num2)
			if len(palindromes) > 1 and palindromes[-1] > palindromes[-2]:
				return palindromes[-1]
		num1 -= 1
		if num1 <= gen_n_digit_number(num_digits - 1):
			num1 = gen_n_digit_number(num_digits)
			num2 -= 1
	return max(palindromes)

if __name__ == '__main__':
	largest = largest_palindrome_product(int(raw_input("Digits: ")))
	print "The largest Palindrome product is " + str(largest)