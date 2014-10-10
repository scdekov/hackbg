def is_number_balanced(n):
    n = str(n)
    n = [a for a in n]
    left_sum = 0
    rigth_sum = 0
    for index in range(0, len(n) // 2):
        left_sum += int(n[index])
    if len(n) % 2 == 0:
        for index in range(len(n) // 2 + 1, len(n)):
            rigth_sum += int(n[index])
    else:
        for index in range(len(n) // 2 + 2, len(n)):
            rigth_sum += int(n[index])
    return rigth_sum == left_sum

print (is_number_balanced(28471))
