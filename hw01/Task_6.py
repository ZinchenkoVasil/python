#6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

number_litera = int(input("ввод латинской строчной буквы (нумерация с 0): "))
ord_first_litera = ord('a')
ord_litera = number_litera + ord_first_litera
litera = chr(ord_litera)
print("это буква: ", litera)
