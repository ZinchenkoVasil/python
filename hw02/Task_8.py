#8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
def colculate_countF(n, figure): #на вход ф-ции передается определенная цифра
    if n <= 0:
        print("число ненатуральное")
        return None
    countF = 0  # счетчик цифры
    while n > 0:
        x = n % 10
        if x == figure:
            countF += 1
        n //= 10
    return countF

figure = input("введите цифру: ")
if len(figure) == 1:
    figure = int(figure)
    sum = 0
    while True:
        n = int(input("введите число n: "))
        if n == 0:
            break
        elif n < 0:
            n = abs(n)
        countF = colculate_countF(n, figure)
        sum += countF
    print(f"{sum} раз встречается цифра {figure} в введенной последовательности чисел")
else:
    print("это не цифра!")