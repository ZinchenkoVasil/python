#1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
while True:
    res = None
    operand1 = float(input("введите операнд1: "))
    operand2 = float(input("введите операнд2: "))
    while True:
        operation = input("введите операцию: ")
        if operation == '0':
            break
        elif operation == '+':
            res = operand1 + operand2
            print("Результат операции: ", res)
            break
        elif operation == '-':
            res = operand1 - operand2
            print("Результат операции: ", res)
            break
        elif operation == '*':
            res = operand1 * operand2
            print("Результат операции: ", res)
            break
        elif operation == '/':
            if operand2 == 0:
                print("делитель = 0, невозможно поделить на 0")
            else:
                res = operand1 / operand2
                print("Результат операции: ", res)
            break
        else:
            print("операция введена неправильно!")
    if operation == '0':
        break



