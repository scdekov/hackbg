def is_an_bn(word):
    if len(word) == 0 or len(word) % 2 == 1:
        return False
    for i in range(0, (len(word) // 2) - 1):
        if word[i] != 'a':
            return False
    for i in range(len(word) // 2, len(word) - 1):
        if word[i] != 'b':
            return False
    return True

print (is_an_bn("aaabb"))
