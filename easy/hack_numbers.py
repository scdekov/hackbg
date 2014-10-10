def is_palindrome(n):
    n = bin(n)
    n = n[2::]
    p = n[::-1]
    for i in range(0, len(n)-1):
        if n[i] != p[i]:
            return False
    return True


def is_ones_odd(n):
    n = bin(n)
    counter = 0
    for a in str(n):
        if a == '1':
            counter = counter +1
    return counter % 2 == 1

def hack_numbers(n):
    p = n
    while True:
        if is_palindrome(p) and is_ones_odd(p):
            return p
        p = p + 1

print (hack_numbers(10))


