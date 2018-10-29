#5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

litera1 = input("Ввод 1 буквы: ")
litera2 = input("Ввод 2 буквы: ")
first_number = ord('a')
number1 = ord(litera1)
number2 = ord(litera2)
pos1 = number1 - first_number
print(f"1 буква стоит на {pos1} позиции (нумерация с 0)")
pos2 = number2 - first_number
print(f"2 буква стоит на {pos2} позиции (нумерация с 0)")
literas_beetwen = abs(pos1 - pos2) - 1
print(f"Между этими буквами находится {literas_beetwen} букв")

