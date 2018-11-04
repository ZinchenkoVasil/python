#9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random
#ввод матрицы
matrix = []
for y in range(4):
    lst = []
    min = 11
    for x in range(4):
        item = random.randint(-10, 10)
        lst.append(item)
    matrix.append(lst)
    print(lst)
print(matrix)

max = -11
for x in range(4):
    min_in_column = 11
    for y in range(4):
        if matrix[y][x] < min_in_column:
            min_in_column = matrix[y][x]
    print(f"минимальный элемент {x} столбца матрицы: {min_in_column}")
    if min_in_column > max:
        max = min_in_column
print("максимум среди минимумов: ", max)




