#Студент Зинченко Василий
#Задача-1
import math

print("--------------------------------------Задача-1-------------------------------------")
lst = [2,-5,8,9,-25,25,4]
lst2 = []
sqrt_i = 0
for i in lst:
    i = float(i)
    if i > 0:
        sqrt_i = math.sqrt(i)
        if int(sqrt_i) == sqrt_i:
            lst2.append(sqrt_i)
print(lst2)

#Задача-2
print("--------------------------------------Задача-2-------------------------------------")
mm = ['','января','февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

day = ['','первое','второе','третье','четвертое','пятое','шестое','седьмое','восьмое','девятое','десятое','одинадцатое','двенадцатое','тринадцатое','четырнадцатое','пятнадцатое',
          'шетнадцатое','семнадцатое','восемнадцатое','девятнадцатое','двадцатое','тридцатое','тридцатьпервое']

date = input("введите дату в формате 'dd.mm.yyyy': ")
d = int(date[:2])
m = int(date[3:5])
y = date[6:]

if d > 20 and d < 30:
    str_date = "двадцать" + day[d % 20]
elif d == 30:
    str_date = day[21]
elif d == 31:
    str_date = day[22]
else:
    str_date = day[d]
str_date += ' ' + mm[m] + ' ' + y + ' года'
print(str_date)

#Задача-3
import random
print("--------------------------------------Задача-3-------------------------------------")
n = int(input("введите кол-во элементов списка: "))
lst = []
for i in range(0,n):
    lst.append(random.randint(-100,100))
print(lst)

#Задача-4
import random
print("--------------------------------------Задача-4-------------------------------------")
n = int(input("введите кол-во элементов списка: "))
lst = []
for i in range(0,n):
    item = input("введите элемент списка: ")
    lst.append(item)
print(lst)

buf = set(lst)
lst2 = list(buf)
print(lst2)

lst3 = []
string = str(lst)
for item in lst:
    i = string.find(item)
    j = string.find(item,i+1)
    if j < 0:
        lst3.append(item)
print(lst3)

      

