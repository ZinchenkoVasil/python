a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a > b:
    if a > c:
        #a - максимум
        if b > c:
            print(f'среднее b = {b:.3f}')
        else:
            print(f'среднее c = {c:.3f}')
    else:
        print(f'среднее a = {a:.3f}')
else:
    if b > c:
        #b - максимум
        if a > c:
            print(f'среднее a = {a:.3f}')
        else:
            print(f'среднее c = {c:.3f}')
    else:
        #c - максимум
        print(f'среднее b = {b:.3f}')
