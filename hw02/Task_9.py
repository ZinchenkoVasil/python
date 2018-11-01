#9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
def colculate_sumF(n): #на вход ф-ции передается определенная цифра
    if n <= 0:
        print("число ненатуральное")
        return None
    sumF = 0
    while n > 0:
        sumF += n % 10
        n //= 10
    return sumF

max = 0
N = 0
while True:
    n = int(input("введите число n: "))
    if n == 0:
        break
    elif n <= 0:
        print("число ненатуральное")
        continue
    sumF = colculate_sumF(n)
    if sumF > max:
        max = sumF
        N = n
print("Среди натуральных чисел, которые были введены, найдено наибольшее по сумме цифр: ", N)
print("сумма цифр: ", max)