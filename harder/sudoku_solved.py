def sudoku_solved(sudoku):
    cols = list(zip(*sudoku))
    for el, v in zip(sudoku, cols):
        for i in range(1, 10):
            if el.count(i) != 1 or v.count(i) != 1:
                return False
    new = {0: [], 1: [], 2: []}

    for el in range(0, 3):
        for v in range(0, 9):
            position = v // 3
            new[position].append(sudoku[el][v])
    for el in new:
        for i in range(1, 10):
            if new[el].count(i) != 1:
                return False

    for el in range(3, 6):
        for v in range(0, 9):
            position = v // 3
            new[position].append(sudoku[el][v])
    for el in new:
        for i in range(1, 10):
            if new[el].count(i) != 2:
                return False

    for el in range(6, 9):
        for v in range(0, 9):
            position = v // 3
            new[position].append(sudoku[el][v])
    for el in new:
        for i in range(1, 10):
            if new[el].count(i) != 3:
                return False

    return True

print (sudoku_solved([
[4, 5, 2, 3, 8, 9, 7, 1, 6],
[3, 8, 7, 4, 6, 1, 2, 9, 5],
[6, 1, 9, 2, 5, 7, 3, 4 ,8],
[9, 3, 5, 1, 2, 6, 8, 7, 4],
[7, 6, 4, 9, 3, 8, 5, 2, 1],
[1, 2, 8, 5, 7, 4, 6, 3, 9],
[5, 7, 1, 8, 9, 2, 4, 6, 3],
[8, 9, 6, 7, 4, 3, 1, 5 ,2],
[2, 4, 3, 6, 1, 5, 9, 8, 7]
]))
