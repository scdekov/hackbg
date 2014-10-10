def calculate_coins(sum):
	coins = {1: 0, 2: 0, 100: 0, 5: 0, 10: 0, 50: 0, 20: 0}
	list_of_coins = [100, 50, 20, 10, 5, 2, 1]
	sum = sum * 100
	while sum > 0:
		for coin in list_of_coins:
			if coin <= sum:
				coins[coin] = coins[coin] + 1
				sum = sum - coin
				break
	return coins


print (calculate_coins(8.94))


