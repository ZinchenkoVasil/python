""" OpenWeatherMap (экспорт)
Сделать скрипт, экспортирующий данные из базы данных погоды,
созданной скриптом openweather.py. Экспорт происходит в формате CSV или JSON.
Скрипт запускается из командной строки и получает на входе:
    export_openweather.py --csv filename [<город>]
    export_openweather.py --json filename [<город>]
    export_openweather.py --html filename [<город>]

При выгрузке в html можно по коду погоды (weather.id) подтянуть
соответствующие картинки отсюда:  http://openweathermap.org/weather-conditions
Экспорт происходит в файл filename.
Опционально можно задать в командной строке город. В этом случае
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.
"""

import csv
import json
import sys
import os
import sqlite3

#выборка конкретного города
def Select_By_City(db_filename, city):
    with sqlite3.connect(db_filename) as conn:
    # Select
    # Объекты connection имеют атрибут row_factory, который позволяет вызывать
    # код, контролирующий тип объкта, создаваемого для каждой строки в запросе
    # Объекты Row дают доступ к данным по индексу и имени
        conn.row_factory = sqlite3.Row

        cur = conn.cursor()
        cur.execute("select * from weather where city = :city",
                    {'city': city})

        lst = []
        for row in cur.fetchall():
            id, name, date_registr, temperature, id_weather = row
            c = {}
            c["id"] = id
            c["name"] = name
            c["date_registr"] = date_registr
            c["temperature"] = temperature
            c["id_weather"] = id_weather
            lst.append(c)
        return lst

#выборка всех городов из БД
def Select_All(db_filename):
    with sqlite3.connect(db_filename) as conn:
    # Select
    # Объекты connection имеют атрибут row_factory, который позволяет вызывать
    # код, контролирующий тип объкта, создаваемого для каждой строки в запросе
    # Объекты Row дают доступ к данным по индексу и имени
        conn.row_factory = sqlite3.Row

        cur = conn.cursor()
        cur.execute("select * from weather")

        lst = []
        for row in cur.fetchall():
            id, name, date_registr, temperature, id_weather = row
            c = {}
            c["id"] = id
            c["name"] = name
            c["date_registr"] = date_registr
            c["temperature"] = temperature
            c["id_weather"] = id_weather
            lst.append(c)
        return lst


# анализ параметров скрипта
# 1) filename 2) mode (csv, json) 3) необязательный параметр city_name
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'file_out.csv'
if len(sys.argv) > 2:
    mode = sys.argv[2]
else:
    mode = '-csv' #'-json'
if len(sys.argv) > 3:
    city_name = sys.argv[3]
else:
    city_name = None
#city_name = "Sankt-Peterburg"


db_filename = 'weather.db'

if os.path.exists(db_filename):
    if city_name:
        cities = Select_By_City(db_filename, city_name)
    else:
        cities = Select_All(db_filename)

    if mode == '-json':
# Записываем объект Python в файл в виде JSON
        try:
            with open(filename, 'w', encoding='UTF-8', ) as f:
                json.dump(cities, f, ensure_ascii=False)
            print("файл создался успешно!")
        except:
            print("Error!")

    elif mode == '-csv':
        # Запись в CSV
        # Создание диалекта
        csv.register_dialect('excel-semicolon', delimiter=';')
        encoding = 'windows-1251'
        with open(filename, 'w', encoding=encoding) as csvfile:
             #   fieldnames = ('id_city', 'name_city', 'date_registration', 'temperature', 'id_weather')
            fieldnames = ('id_города', 'Город', 'Дата', 'Температура', 'id_погоды')
            writer = csv.writer(csvfile, dialect='excel-semicolon')
            writer.writerow(fieldnames)
            for city in cities:
                city["temperature"] = int(city["temperature"])
                #досадная ошибка: в EXEL дробные показываются в виде дат
                try:
                    writer.writerow(city.values())
                except:
                    print("Error!")
    else:
        print("формат выходного файла задан неправильно! Введите вторым параметром скрипта [json] или [csc]")
else:
    print("файл БД  'weather.db' не найден!")