#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random
lst = [random.randint(-1000, 1000) for i in range(10)]
print(lst)
max = lst[0]
min = lst[0]
i = 0
i_min = 0
i_max = 0
while i < len(lst):
    if lst[i] > max:
        max = lst[i]
        i_max = i
    if lst[i] < min:
        min = lst[i]
        i_min = i
    i += 1

spam = lst[i_max]
lst[i_max] = lst[i_min]
lst[i_min] = spam
print(lst)
