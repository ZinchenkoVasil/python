"""
== OpenWeatherMap ==
OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.
Необходимо решить следующие задачи:
== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.

    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID,
    используя дополнительную библиотеку GRAB (pip install grab)
        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up
        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in
        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys

        Ключ имеет смысл сохранить в локальный файл, например, "app.id"

== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz

    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка
     (воспользоваться модулем gzip
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)

    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}


== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a
    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a
    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a
    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations",
    "main":{"temp":280.03,"pressure":1006,"humidity":83,"temp_min":273.15,"temp_max":284.55},
    "wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":
    {"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,"sunset":1465149961},
    "id":520068,"name":"Noginsk","cod":200}
== Сохранение данных в локальную БД ==
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):
    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных
2. Выводить список стран из файла и предлагать пользователю выбрать страну
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))
3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.
При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.
При работе с XML-файлами:
Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>
Чтобы работать с пространствами имен удобно пользоваться такими функциями:
    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''
    tree = ET.parse(f)
    root = tree.getroot()
    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}
    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...
"""

#1-----------------------------------------
# Создание файла базы данных
import os
import sqlite3
import datetime
import json
import requests
from requests.auth import HTTPDigestAuth

def create_db(db_filename):
    conn = sqlite3.connect(db_filename)
    conn.close()


# Создание схемы
# Схема определяет таблицы в базе данных

    #os.remove(db_filename)
    with sqlite3.connect(db_filename) as conn:
        conn.execute("""
        create table weather (            
            id_city           INTEGER PRIMARY KEY,
            city              VARCHAR(255),
            date_registr      DATE,
            temperature       INTEGER,
            id_weather        INTEGER                         
        );
        """)



def Insert_db(db_filename, city):
    # Insert
    with sqlite3.connect(db_filename) as conn:
        conn.execute("""
            insert into weather (id_city,name,date_registr,temperature,id_weather) VALUES (?,?,?,?,?)""", (
                city["id"],
                city["name"],
                datetime.date.today(),
                city["temperature"],
                city["id_weather"]
            )
        )

def Select_db(db_filename, city_id, date_registr):
    with sqlite3.connect(db_filename) as conn:
    # Select
    # Объекты connection имеют атрибут row_factory, который позволяет вызывать
    # код, контролирующий тип объкта, создаваемого для каждой строки в запросе
    # Объекты Row дают доступ к данным по индексу и имени
        conn.row_factory = sqlite3.Row

        cur = conn.cursor()
        cur.execute("select * from weather where city_id = :city_id and date_registr = :date_registr",{'city_id': city_id, 'date_registr': date_registr})
        city = {}
        for row in cur.fetchall():
            id, name, date_registr, temperature, id_weather = row
            city["id"] = id
            city["name"] = name
            city["date_registr"] = date_registr
            city["temperature"] = temperature
            city["id_weather"] = id_weather
        return city

def Update_db(db_filename, city):
    with sqlite3.connect(db_filename) as conn:
    # Update
        cur = conn.cursor()
        cur.execute("update weather set temperature=:temperature where id=:id and date_registr = :date_registr",
                        {'temperature': city["temperature"], 'id': city["id"], 'date_registr': city["date_registr"]})


db_filename = 'weather.db'
if not os.path.exists(db_filename):
    create_db(db_filename)

#2---------------------------------------------------------------------------------------------------------------------
if os.path.exists("city.list.json"):
    # Читаем JSON из файла и преобразуем к типу Python
    with open('city.list.json', 'r', encoding='UTF-8') as f:
        read_data = json.load(f)
        country = {}
        for item in read_data:
            country[item["country"]] = ""
    print("Коды стран (оосортированы по алфавиту): ")
    lst = []
    for c in country.keys():
        lst.append(c)
    lst.sort()
    print(lst)

    Find = False
    while not Find:
        code_country = input("введите код или название страны: ")
        code_country = code_country[0:2]
        code_country = code_country.upper()
        for c in lst:
            if c == code_country:
                Find = True
                break
        else:
            print("Код страны введен неправильно!")

    cities = []
    for item in read_data:
        if item["country"] == code_country:
            cities.append(item["id"])
            print(item["name"])

#список городов получен теперь надо файл погоды скачать!
#3-------------------------------------------------------------------------------
    # Replace with the correct URL
    for city in cities:
        url = "http://api.openweathermap.org/data/2.5/group?id="+str(city)+"&units=metric&appid=a8cf5599161b452f38b6a8e25eb33847"

    # It is a good practice not to hardcode the credentials. So ask the user to enter credentials at runtime
        myResponse = requests.get(url, auth=HTTPDigestAuth("Vasiliy", "barsik111111"), verify=True)
    # print (myResponse.status_code)

    # For successful API call, response code will be 200 (OK)
        if (myResponse.ok):

        # Loading the response data into a dict variable
        # json.loads takes in only binary or string variables so using content to fetch binary content
        # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
            jData = json.loads(myResponse.content)

            print("The response contains {0} properties".format(len(jData)))
            print("\n")
            for key in jData:
                print(key + " : " + str(jData[key]))
                city = {}
                city["id"] = key["id"]
                city["name"] = key["name"]
                city["id_weather"] = ((key["weather"])[0])["id"]
                city["temperature"] = (key["main"])["temp"]
                city["date_registr"] = datetime.date.today()
                if Select_db(db_filename, city["id"],datetime.date.today()):
                    Update_db(db_filename, city)
                else:
                    Insert_db(db_filename, city)
        else:
        # If response code is not ok (200), print the resulting http error code with description
            myResponse.raise_for_status()


