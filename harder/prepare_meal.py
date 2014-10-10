def prepare_meal(number):
    step = 0
    for i in range(1, 100):
        if number % (3 ** i) == 0:
            step = i
    if number % 5 == 0:
        if step > 0:
            return "spam " * step + "and eggs"
        return "eggs"
    return "spam " * step

print (prepare_meal(45))
