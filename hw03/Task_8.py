#8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку.
# В конце следует вывести полученную матрицу.

#ввод матрицы
matrix = []
for y in range(4):
    lst = []
    for x in range(4):
        item = int(input(f"столбец {x}, строка {y} введите элемент  матрицы: "))
        lst.append(item)
    lst.append(None)
    matrix.append(lst)
print(matrix)

for y in range(4):
    summ = 0
    for x in range(4):
        item = (matrix[y])[x]
        summ += item
    (matrix[y])[4] = summ
print(matrix)





