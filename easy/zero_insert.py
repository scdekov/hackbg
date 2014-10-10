def zero_insert(n):
    n = [a for a in str(n)]
    if len(n) == 1:
        return int(n[0])
    if len(n) == 2 and n[0] == n[1]:
        if (int(n[0]) + int(n[1])) % 10 == 0:
            n.insert(n[1], '0')
            return (int("".join(n)))
    counter = -1
    c = 0
    for num in n:
        print (n)
        if c != 0:
            if (int(num) + int(n[counter])) % 10 == 0:
                n.insert(counter + 1, '0')
            if int(num) == int(n[counter]):
                n.insert(counter + 1, '0')
        counter = counter + 1
        c = c + 1
    return (int("".join(n)))

print (zero_insert(5555))


