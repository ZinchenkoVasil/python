#5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random
lst = [random.randint(-10, 10) for i in range(10)]
print(lst)
max = - 11
i = 0
while i < len(lst):
    if lst[i] < 0 and lst[i] > max:
        max = lst[i]
        i_max = i
    i += 1


print("значение максимального отрицательного элемента: ", max)
print("его позиция в массиве: ", i_max)