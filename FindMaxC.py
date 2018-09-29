strNumber = input("введите число: ")
Number = int(strNumber) #проверка на число
#самый короткий и простой способ выполнения задания
max = max(strNumber)
print("максимальная цифра в числе: ", max)

#использование цикла while
max = '0'
i = 0
while i < len(strNumber):
    if  strNumber[i] > max:
        max = strNumber[i]
    i += 1     
print("максимальная цифра в числе: ", max)

#использование цикла for 
max = '0'
for n in strNumber:
    if  n > max:
        max = n 
print("максимальная цифра в числе: ", max)
