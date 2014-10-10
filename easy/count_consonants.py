def count_consonants(str):
    counter = 0
    str = [x for x in str.lower()]
    for symb in str:
        if symb in "bcdfghjklmnpqrstvwxz":
            counter += 1
    return counter

print (count_consonants("Theistareykjarbunga"))
