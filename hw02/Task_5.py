#5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
#Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.
i = 0
start_code = 32
stop_code = 127
for code in range(start_code, stop_code + 1):
    litera = chr(code)
    if (code - start_code + 1) % 10 == 0:
        print('\n')
    print(code,'-',litera, end = ' | ')
