#7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random
lst = [random.randint(-10, 10) for i in range(10)]
print(lst)
min = 11
i = 0
while i < len(lst):
    if lst[i] < min:
        min = lst[i]
        i_min = i
    i += 1
second_min = 11
i =0
while i < len(lst):
    if i != i_min and lst[i] < second_min:
        second_min = lst[i]
    i += 1

print("два наименьших элемента: ", min, second_min)
