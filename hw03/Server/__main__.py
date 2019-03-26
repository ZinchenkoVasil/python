# Программа сервера для получения приветствия от клиента и отправки ответа
from socket import *
import json
import sys
import argparse
from Server.text import routes

import logging
import select
from socket import socket, AF_INET, SOCK_STREAM

def parsing(data):
    logger.debug("сервер принял сообщение от клиента")
    request = json.loads(data)
    logger.debug("парсинг сообщения от клиента")
    client_action = request.get('action')
    resolved_routes = list(
        filter(
            lambda itm: itm.get('action') == client_action, routes))
    route = resolved_routes[0] if resolved_routes else None
    response_dict = {}
    if route:
        controller = route.get('controller')
        if "user" in request:
            user = request.get('user')
            user = user['account_name']
        else:
            user = ''
        if "message" in request:
            data = request.get('message')
        else:
            data = ''
        response_string = controller(user, data)
        response_dict['response'] = 200
        response_dict['alert'] = response_string
    else:
        response_dict['response'] = 401
        response_dict['alert'] = "Action don't support"
        logger.error("Action don't support")
        logger.error("клиент работает по неизвестному протоколу!")
    return response_dict


def read_requests(r_clients, all_clients):
   """ Чтение запросов из списка клиентов
   """
#   responses = {}  # Словарь ответов сервера вида {сокет: запрос}
   response = None
   for sock in r_clients:
       try:
           data = sock.recv(1024).decode('utf-8')
           response = parsing(data) #парсинг сообщения от клиента
           print("сообщение от клиента получено")
       except:
           print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
           sock.close()
           all_clients.remove(sock)

   return response


def write_responses(response, w_clients, all_clients):
   """ Эхо-ответ сервера клиентам, от которых были запросы
   """

   for sock in w_clients:
#       for request in requests:
           try:
               # Подготовить и отправить ответ сервера
               print("Подготовить и отправить ответ сервера")
               resp = json.dumps(response).encode('utf-8')
               # Эхо-ответ
               sock.send(resp)
               print(f"Эхо-ответ {resp} выслали всем слушающим клиентам")
           except:  # Сокет недоступен, клиент отключился
               print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
               sock.close()
               all_clients.remove(sock)

def mainloop():
   """ Основной цикл обработки запросов клиентов
   """
   address = ('', 10000)
   clients = []

   s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
   logger.debug("Создает сокет TCP")
   s.bind((args.addr, args.port))  # Присваивает порт
   logger.debug("Присваивает порт")
   s.listen(5)  # Переходит в режим ожидания запросов;
   logger.debug("Переходит в режим ожидания запросов")
   s.settimeout(0.2)  # Таймаут для операций с сокетом
   while True:
       try:
           conn, addr = s.accept()  # Проверка подключений
       except OSError as e:
           pass  # timeout вышел
       else:
           print("Получен запрос на соединение от %s" % str(addr))
           clients.append(conn)
       finally:
           # Проверить наличие событий ввода-вывода
           wait = 10
           r = []
           w = []
           try:
               r, w, e = select.select(clients, clients, [], wait)
#               print("r_clients:", r)
#               print("w_clients", w)
           except:
               pass  # Ничего не делать, если какой-то клиент отключился

           response = read_requests(r, clients)  # Сохраним запросы клиентов
           if response:
               write_responses(response, w, clients)  # Выполним отправку ответов клиентам


# Обратите внимание, логгер уже создан в модуле log_config,
# теперь нужно его просто получить
logger = logging.getLogger('server.main')
logger.info('Запуск сервера-------------------------------------------------------------')

parser = argparse.ArgumentParser()
parser.add_argument('-a', dest='addr', action='store', type=str, required=False, help='IP-address', default='')
parser.add_argument('-p', dest='port', action='store', type=int, required=False, help='Port', default=7777)
args = parser.parse_args(sys.argv[1:])
mainloop()
