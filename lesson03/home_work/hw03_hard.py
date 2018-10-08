# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/ort
print("-------------------Начало задания 1----------------------")

#сложение 2 дробных чисел
#функция возвращает результат операции в виде списка (член0 - целая часть, член1 -  числитель  член2 - знаменатель)
def GetResultOperation(ch1, ch2, z1, z2, plus):
    if z1 > z2 and z1 % z2 == 0:
        k = z1 / z2
        result_z = z1
        if plus:
            result_ch = k * ch2 + ch1
        else:
            result_ch = ch1 - k * ch2
    elif z2 > z1 and z2 % z1 == 0:
        k = z2 / z1
        result_z = z2
        if plus:
            result_ch = k * ch1 + ch2
        else:
            result_ch = k * ch1 - ch2
    else:
        result_z = z1 * z2
        if plus:
            result_ch = ch2 * z1 + ch1 * z2
        else:
            result_ch = ch1 * z2 - ch2 * z1

    CelPart = result_ch // result_z
    result_ch = result_ch % result_z

    return (CelPart, result_ch, result_z)

#функция возвращает результат парсинга в виде списка (член0 - целая часть, член1 -  числитель  член2 - знаменатель)
def Parsing_operand(operand):
    if operand.find(' ') != -1: # ищем пробел между целой и дробной частями
    #в операнде присутствует и целая и дробная часть
        Parts = operand.split(" ")
        celPart = int(Parts[0])
        drobnPart = Parts[1]
        if drobnPart.find('/') > - 1:
            lst = drobn.split('/')
            ch = int(lst[0])
            zn = int(lst[1])
            return (celPart, ch, zn)
        else:
            return (0,0,0) #какая-то фигня на входе

    else:
   #надо определиться это целое или дробное число?
        if operand.find('/') > - 1:
            lst = operand.split('/')
            ch = int(lst[0])
            zn = int(lst[1])
            return (0, ch, zn)
        else:
            return (int(operand), 0, 0)  # введено просто целое число


string = input("введите выражение с дробями: ")
if string.find(' + ') > -1:
    lst = string.split(' + ')
    plus = True
elif string.find(' - ') > -1:
    lst = string.split(' - ')
    plus = False
operand1 = lst[0]
result_parsing1 = Parsing_operand(operand1)
operand2 = lst[1]
result_parsing2 = Parsing_operand(operand2)

#3 варианта:
# 1) числа только целые - просто складываем
# 2) числа только дробные - просто операция
# 3) 1 число целое а 2 дробное - преобразование к дробному и дальше пункт 2



#1 вариант
if (result_parsing1[0] > 0 and result_parsing1[1] == 0) and (result_parsing2[0] > 0 and result_parsing2[1] == 0):
    if plus:
        result = result_parsing1[0] + result_parsing2[0]
    else:
        result = result_parsing1[0] - result_parsing2[0]
    print("Результат: ", result)

else:
    # 2 вариант
    celPart1 = result_parsing1[0]
    celPart2 = result_parsing2[0]
    ch1 = result_parsing1[1]
    zn1 = result_parsing1[2]
    ch2 = result_parsing2[1]
    zn2 = result_parsing2[2]

# если число имеет целую и дробную части  то перевести в дробное и дальше пункт 2
    if celPart1 > 0 and ch1 > 0:
        ch1 = celPart1 * zn1 + ch1

    if result_parsing2[0] > 0 and result_parsing2[1] > 0:
        ch2 = celPart2 * zn2 + ch2

    if celPart1 > 0 and ch1 == 0:
        ch1 = zn2 * celPart1
        zn1 = zn2

    if celPart2 > 0 and ch2 == 0:
        ch2 = zn1 * celPart2
        zn2 = zn1

    result = GetResultOperation(ch1, ch2, zn1, zn2, plus)
    if result[0] == 0:
        print("Результат: ", str(result[1])+"/"+str(result[2]))
    elif result[1] == 0:
        print("Результат: ", str(result[0]))
    else:
        print("Результат: ", str(result[0]) + " " + str(result[1]) + "/" + str(result[2]))

print("-------------------Конец задания 1----------------------")


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во , которые были отработаны, указаны в файле "data/hours_of"

#не забудь сделать через JOIN формирование полного имени файла (соединение файла и директории)!!!!!!!!!!!!!!!!!!!!!!!!!
import os

def Colculate(Salary, Normal_Work_hours, Real_Work_hours):
    if Real_Work_hours == Normal_Work_hours:
        money = Salary
        return money
    elif Real_Work_hours < Normal_Work_hours:
        money = (Salary / Normal_Work_hours) * Real_Work_hours
        return money
    else:
        money = Salary + (Real_Work_hours - Normal_Work_hours) * (Salary/Normal_Work_hours) * 2
        return money

fullName = os.path.join('data','workers')
with open(fullName, 'rt', encoding='UTF-8') as fin:
    i = 0
    employees = []
    for line in fin:
        if i == 0:
            i += 1
            continue
        else:
            employee = {"FirstName": line[:7],
                        "SecondName": line[8:20],
                        "Salary": int(line[21:35]),
                        "Normal_Work_hours": int(line[51:])}
            employees.append(employee)

fullName = os.path.join('data', 'hours_of')
with open(fullName, 'rt', encoding='UTF-8') as fin:
    i = 0
    hours_of = []
    for line in fin:
        if i == 0:
            i += 1
            continue
        else:
            employee = {"FirstName": line[:7],
                        "SecondName": line[8:20],
                        "Real_Work_hours": int(line[24:])}
            hours_of.append(employee)

for employee in employees:
    for worker in hours_of:
        if employee["FirstName"] == worker["FirstName"] and employee["SecondName"] == worker["SecondName"]:
            money = Colculate(employee["Salary"],employee["Normal_Work_hours"],worker["Real_Work_hours"])
            print(worker["FirstName"], worker["SecondName"], " заработал: ", int(money))


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

#в этом алгоритме мы исходим из факта, что список отсортирован по буквам алфавита!!!!!!!!!!!!!
import os
fullName = os.path.join('data', 'fruits.txt')
with open(fullName, 'rt', encoding='UTF-8') as fin:
    Current_litera = 'А'
    lstLitera = ['А']      #заполняем 1 элемент списка буквой
    lstFruits = []
    for fruit in fin:#проходим по файлу и получаем список списков
        if fruit == '\n':
            continue
        if fruit[0] == Current_litera: #если фрукт начинается с текущей буквы
            lstLitera.append(fruit)
        else:
            lstFruits.append(lstLitera)
            if Current_litera == 'Я': #дошли до буквы 'Я' выходим из цикла
                break
            else:
                Current_litera = chr(ord(Current_litera)+1) #переходим к следующей букве
                lstLitera = [Current_litera] #опять заполняем 1 элемент списка текущей буквой

#    print(lstFruits)
    for lstLitera in lstFruits:
        if len(lstLitera) < 2:
            continue
        else:
            litera = lstLitera.pop(0)
            file_name = 'fruits_' + litera +".txt"
            file_name = os.path.join('data', file_name)
            fout = open(file_name, 'wt', encoding='UTF-8')
            for fruit in lstLitera:
                print(fruit, file=fout)
            fout.close()

