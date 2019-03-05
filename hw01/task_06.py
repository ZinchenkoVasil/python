import locale
def_coding = locale.getpreferredencoding()
print(def_coding)
f_n = open("test_file.txt", "w", encoding='utf-8')
f_n.write("сетевое программирование\n")
f_n.write("сокет\n")
f_n.write("декоратор\n")
f_n.close()
print(f_n)

with open('test_file.txt', encoding='utf-8') as f_n:
    for el_str in f_n:
        print(el_str)


