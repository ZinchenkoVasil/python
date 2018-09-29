import math
a = int(input("Введите а: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
D = b*b - 4*a*c
if D == 0:
    x = (-b)/(2*a)
    print("уравнение имеет один корень: ", x)
elif D < 0:
    print("уравнение не имеет корней!")
else:
    print("уравнение имеет 2 корня! ")
    x1 = (-b + math.sqrt(D))/(2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("1 корень уравнения: ", x1)
    print("2 корень уравнения: ", x2)





