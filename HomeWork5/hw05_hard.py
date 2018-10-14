#Студент: Зинченко Василий

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")

    print("cp <full_path or relative_path> <file_name> - создает копию указанного файла  ('.' - текущая директория)")
    print("rm <full_path or relative_path> <file_name> - удаляет указанный файл ('.' - текущая директория)")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную ('.' - текущая директория)")
    print("ls - отображение полного пути текущей директории")

def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

#ls - отображение полного пути текущей директории
def show_current_dir():
    print("текущая директория = ", os.getcwd())

def remove_file():
    if not file_name:
        print("Необходимо указать имя файла третьим параметром")
        return
    change_dir()
    try:
        if os.path.exists(file_name):
            os.remove(file_name)
            if not os.path.exists(file_name):
                print("файл {} удален".format(file_name))
            else:
                print("файл {} не удален".format(file_name))
        else:
            print("файл {} не существует в текущей директории".format(file_name))
    except:
        print("файл {} не удалось удалить (возможно, недостаточно прав)".format(file_name))

#смена текущей директории
#надо учесть что может быть относительный или абсолютный путь
def change_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    if dir_name == '.':
        print("Остаемся в текущей директории")
        return
    if os.path.exists(dir_name):
        os.chdir(dir_name)
        print("директория {} стала текущей".format(dir_name))
        show_current_dir()
    else:
        print("директория {} не существует".format(dir_name))

def copy_file():
    if not file_name:
        print("Необходимо указать имя файла третьим параметром")
        return
    change_dir()
    try:
        if os.path.exists(file_name):
            #копируем в текущий каталог
            point = file_name.find('.')
            if point > - 1:
                dst = file_name[:point] + '_copy' + file_name[point:]
            else:
                dst = file_name + '_copy'
            shutil.copy(file_name, dst)
            print("файл {} скопирован".format(file_name))
        else:
            print("файл {} не существует в текущей директории".format(file_name))
    except:
        print("файл {} не удалось скопировать".format(file_name))


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": remove_file,
    "cd": change_dir,
    "ls": show_current_dir
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

try:
    file_name = sys.argv[3]
except IndexError:
    file_name = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")




