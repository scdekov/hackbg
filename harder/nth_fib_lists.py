def nth_fib_lists(listA, listB, n):
    if n < 1:
        return False
    if n == 1:
        return listA
    if n == 2:
        return listB
    first = listA
    second = listB
    res = []
    for i in range(2,n):
        res = first + second
        first = second
        second = res
    return res



