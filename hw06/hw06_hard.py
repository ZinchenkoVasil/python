# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во , которые были отработаны, указаны в файле "data/hours_of"

#делаю класс Сотрудник
#методы: конструктор, set_Real_work-hours

import os

class Worker:
    def __init__(self, line):
        self.FullName = line[:20]
        self.Salary = int(line[21:35])
        self.Normal_Work_hours = int(line[51:])

    def Colculate(self, Real_Work_hours):
        if Real_Work_hours == self.Normal_Work_hours:
            money = self.Salary
        elif Real_Work_hours < self.Normal_Work_hours:
            money = (self.Salary / self.Normal_Work_hours) * Real_Work_hours
        else:
            money = self.Salary + (Real_Work_hours - self.Normal_Work_hours) * (self.Salary/self.Normal_Work_hours) * 2

        self.money = money

FileName = os.path.join('data', 'workers')
if os.path.exists(FileName):
    with open(FileName, 'rt', encoding='UTF-8') as fin:
        workers = []
        head_line = True
        for line in fin:
            if not head_line:
                try:
                    worker = Worker(line)
                    workers.append(worker)
                except:
                    print("сбой в строке: ")
                    print(line)
            else:
                head_line = False
else:
    print("файл {} не существует".format(FileName))

FileName = os.path.join('data', 'hours_of')
if os.path.exists(FileName):
    with open(FileName, 'rt', encoding='UTF-8') as fin:
        hours_of = {}
        head_line = True
        for line in fin:
            if not head_line:
                try:
                    hours_of[line[:20]] = int(line[24:])
                except:
                    print("сбой в строке (количество рабочих часов задано не ввиде числа): ")
                    print(line)
            else:
                head_line = False

    #перебор всех классов
    for worker in workers:
        if worker.FullName in hours_of:
            Real_Work_hours = hours_of[worker.FullName]
            worker.Colculate(Real_Work_hours)
            print("{} заработал: {}".format(worker.FullName, int(worker.money)))
else:
    print("файл {} не существует".format(FileName))




