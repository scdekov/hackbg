def sevens_in_a_row(arr,n):
	index = 0
	counter = 0
	for number in arr:
		if arr[index] != 7:
			counter = 0
		if number == 7:
			if n == 1:
				return True
			counter += 1
		index += 1
		if counter == n:
			return True
	return False


print (sevens_in_a_row([1,7,1,7,7], 4))

