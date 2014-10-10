def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


def goldbach(n):
    res = []
    for i in range(0, n):
        if is_prime(i) is True:
            for j in range(i, n):
                if is_prime(j) is True and i + j == n:
                    res.append((i, j))
    return res

print (goldbach(10))
