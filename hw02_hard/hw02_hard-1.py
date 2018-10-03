#-Задача-1
#Студент: Зинченко Василий

equation = input("Введите уравнение вида y = kx + b: ")
number = equation.find('=')
numberX = equation.find('x')
print('k =', equation[number + 2:numberX])
k = float(equation[number + 2:numberX])
numberPlus = equation.find('+')
print('b =', equation[numberPlus + 2:])
b = float(equation[numberPlus + 2:])
x = float(input("Введите x: "))
y = k*x + b
print("y = ", y)