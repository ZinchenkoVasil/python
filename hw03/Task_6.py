#6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

import random
lst = [random.randint(-10, 10) for i in range(10)]
print(lst)
max = - 11
min = 11
for item in lst:
    if item > max:
        max = item
    if item < min:
        min = item
print("минимум: ", min)
print("максимум: ", max)
summ = 0
for item in lst:
    if item != min and item != max:
        summ += item
print("сумма всех элементов массива: ", sum(lst))
print("сумма  элементов, находящихся между минимальным и максимальным элементами: ", summ)