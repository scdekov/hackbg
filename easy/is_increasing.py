def is_increasing(seq):
    crr=seq[0]
    for elem in seq:
        if crr >= elem and elem != seq[0]:
            return False
        crr = elem
    return True

print (is_increasing([1]))