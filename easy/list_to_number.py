def list_to_number(digits):
	 new = ""
	 for num in digits:
	 	new += str(num)
	 return int(new)

print (list_to_number([1,2,3]))