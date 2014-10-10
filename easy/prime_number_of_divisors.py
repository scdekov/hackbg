def prime_number_of_divisors(n):
	divisors = 0
	for i in range(1,n+1) :
		if n % i == 0 :
			divisors += 1
	for i in range(2,divisors):
		if divisors % i == 0:
			return False
	return True

def main():
	print (prime_number_of_divisors(8))


if __name__ == '__main__':
	main()