def sum_matrix(m):
	su  = 0
	for el in m:
		su = su + sum(el)
	return su

print (sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))