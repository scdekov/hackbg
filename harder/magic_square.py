def magic_square(matrix):
    summ = sum(matrix[0])
    p = list(zip(*matrix))
    for el, v in zip(matrix, p):
        if sum(el) != summ or sum(v) != summ:
            return False
    diagonal = 0
    counter = 0
    for el in matrix:
        diagonal += el[counter]
        counter += 1
    if diagonal != summ:
        return False
    counter = len(matrix) - 1
    diagonal = 0
    for el in matrix:
        diagonal += el[counter]
        counter -= 1
    return diagonal == summ


