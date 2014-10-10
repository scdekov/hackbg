def nth_fibonacci(n):
	if n==1:
		return 0
	if n==2:
		return 1
	first=0
	second=1
	res=0
	for i in range(2,n):
		res = first + second
		first = second
		second = res
	return res


print (nth_fibonacci(10))
