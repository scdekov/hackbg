def contains_digit(number, digit):
	while number > 0:
		if number % 10 == digit:
			return True
		number /= 10
	return False

print (contains_digit(1231231234,5))