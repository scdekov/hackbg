def sum_of_digits(n):
	n = abs(n)
	sum = 0
	while n != 0 :
		sum += n % 10
		n = n // 10
	return sum


print (sum_of_digits(-10))
