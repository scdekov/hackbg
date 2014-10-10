def count_vowels(str):
    counter = 0
    str = [x for x in str]
    for symb in str:
        if symb in "aeiouy":
            counter += 1
    return counter

print (count_vowels("Theistareykjarbunga"))