from is_prime import is_prime


def prime_factorization(n):
    dividers = []
    counter = 2
    p = n
    while n != 1:
        if is_prime(counter) and n % counter == 0:
            dividers.append(counter)
            n /= counter
        else:
            counter += 1
    result = []
    for i in range(2, p + 1):
        if dividers.count(i) > 0:
            result.append((i, dividers.count(i)))
    return result


def main():
    print (prime_factorization(356))

if __name__ == '__main__':
    main()

