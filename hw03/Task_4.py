#4. Определить, какое число в массиве встречается чаще всего.


import random
lst = [random.randint(1, 5) for i in range(10)]
print(lst)
dubl = {}
for i in lst:
    if i in dubl:
        dubl[i] += 1
    else:
        dubl[i] = 1
print(dubl)
max = 0
for key in dubl:
    if dubl[key] > max:
        max = dubl[key]
        key_max = key


print(f"в массиве встречается чаще всего число {key_max} ({max} раз)")


