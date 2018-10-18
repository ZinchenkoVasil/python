# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Subject:
    def __init__(self, code, name, teacher):
        self.code = code
        self.name = name
        self.teacher = teacher

    def set_teacher(self, teacher):
        self.teacher = teacher

class Class_room:
    def __init__(self, name):
        self.name = name
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def remove_subject(self, subject):
        self.subjects.remove(subject)

class Person:
    def __init__(self, surname, first_name, patronymic):
        self.first_name = first_name  #класс person
        self.surname = surname
        self.patronymic = patronymic

    def get_fio(self):
        return self.surname + ' ' + self.first_name[0] + '.' + self.patronymic[0] + '.'


class Student(Person):
    def __init__(self, surname, first_name, patronymic, mather, father):
        super().__init__(surname, first_name, patronymic)
        self.mather = mather #класс person
        self.father = father #

    def set_class_room(self, class_room):
        self.class_room = class_room

teacher1 = Person('Преображенский', 'Иван', 'Васильевич')
teacher2 = Person('Ковалевская', 'Софья', 'Александровна')
teacher3 = Person("Толстой", 'Лев', 'Николаевич')

subject1 = Subject(1, 'Физкультура', teacher1)
subject2 = Subject(2, 'Математика', teacher2)
subject3 = Subject(3, 'Русский язык', teacher3)

lst_class_rooms = ['1А', '1Б', '1В']
class_rooms = []
for room in lst_class_rooms:
    class_room = Class_room(room)
    class_room.add_subject(subject1)
    class_room.add_subject(subject2)
    class_room.add_subject(subject3)
    class_rooms.append(class_room)

print("1. Получить полный список всех классов школы")
print("полный список всех классов школы:")
for class_room in class_rooms:
    print("Класс ", class_room.name)

print("2. Получить список всех учеников в указанном классе (каждый ученик отображается в формате 'Фамилия И.О.'")

students = []
father = Person('Зинченко', 'Александр', 'Васильевич')
mather = Person('Зинченко', 'Софья', 'Александровна')
student = Student('Зинченко', 'Василий', 'Александрович', mather, father)
student.set_class_room(class_rooms[0])
students.append(student)

father = Person('Иванов', 'Александр', 'Васильевич')
mather = Person('Иванова', 'Софья', 'Александровна')
student = Student('Иванов', 'Иван', 'Александрович', mather, father)
student.set_class_room(class_rooms[0])
students.append(student)

room = '1А'
print("Список класса", room)
for student in students:
    if student.class_room.name == room:
        print(student.get_fio())


print("3. Получить список всех предметов указанного ученика (Ученик --> Класс  --> Предметы)")
student_fio = 'Зинченко В.А.'
print("Список предметов", student_fio)

for student in students:
    if student.get_fio() == student_fio:
        for subject in student.class_room.subjects:
            print(subject.name)

print("4. Узнать ФИО родителей указанного ученика")
student_fio = 'Зинченко В.А.'
print("Студент: ",student_fio)
for student in students:
    if student.get_fio() == student_fio:
        print("Родители: ", student.mather.get_fio(), student.father.get_fio())

print("5. Получить список всех Учителей, преподающих в указанном классе (класс class_room -> предметы subjects -> учителя teacher)")
room = '1А'
for class_room in class_rooms:
    if class_room.name == room:
        for subject in student.class_room.subjects:
            print(subject.name, ':', subject.teacher.get_fio())