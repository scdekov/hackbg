def is_int_palindrome(n):
	number = str(n)
	return number == number[::-1]


print (is_int_palindrome(100001))