def sum_of_divisors(n):
	sum = 0
	for i in range(1,n+1):
		if n % i == 0 :
			sum += i
	return sum

print (sum_of_divisors(1000))
