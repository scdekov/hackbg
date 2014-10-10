def contains_digits(number, digits):
    number = str(number)
    number = [a for a in number]
    for dig in digits:
        if not str(dig) in number:
            return False
    return True

print (contains_digits(402123, [0, 3, 4]))
