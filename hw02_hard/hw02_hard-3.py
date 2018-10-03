#-Задача-2
#Студент: Зинченко Василий

N = int(input("введите номер комнаты: "))
n = 1
n_room = 1
n_floor = 1
#поиск n
N_room = 0
N_floor = 0
while True:
    n += 1
    old_n_room = n_room
    n_room = n_room + n * n
    if N <= n_room  - n and N > old_n_room: #найден диапазон этажей равной ширины!
        #поиск этажа
        n_room = old_n_room
        while True:
            n_floor += 1
            n_room += n
            if N <= n_room:
                N_room = N - (n_room - n)
                N_floor = n_floor
                break
        break
    elif N <= n_room:    #мы точно нашли этаж и номер комнаты
        N_floor = n_floor + n #мы точно нашли этаж
        N_room = N - (n_room  - n)
        break
    else:
        n_floor += n


print("этаж №: ", N_floor)
print("№ комнаты на этаже: ", N_room)



