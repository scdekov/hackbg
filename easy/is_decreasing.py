def is_decreasing(seq):
    crr=seq[0]
    for elem in seq:
        if crr >= elem and elem != seq[0]:
            return False
        crr = elem
    return True

print (is_decreasing([100, 50, 20]))