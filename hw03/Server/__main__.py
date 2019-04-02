# Программа сервера для получения приветствия от клиента и отправки ответа
import json
import sys
import argparse
from Server.text import routes
from Log.server_log_config import *
import select
from socket import socket, AF_INET, SOCK_STREAM
from queue import Queue
from threading import Thread

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

def read_request(requests,sock,all_clients):
    try:
        data = sock.recv(1024).decode('utf-8')
        request = parsing(data)  # парсинг сообщения от клиента
        requests.put(request)
        print("сообщение от клиента получено")
    except:
        print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
        sock.close()
        all_clients.remove(sock)


def read_requests(r_clients, all_clients):
    requests_queue = Queue()  # Очередь ответов сервера вида
    for sock in r_clients:
#        t = Thread(target=read_request, args=(requests_queue,sock,all_clients))
#        t.start()
        read_request(requests_queue,sock,all_clients)
    return requests_queue #надо в цикле заполнить очередь


def write_response(response,sock,all_clients):
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


def write_responses(response, w_clients, all_clients):
    for sock in w_clients:
        t = Thread(target=write_response, args=(response, sock, all_clients))
        t.start()

def mainloop():
   """ Основной цикл обработки запросов клиентов
   """
   clients = []

   s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
   print("Создает сокет TCP")
   s.bind((args.addr, args.port))  # Присваивает порт
   print("Присваивает порт")
   s.listen(5)  # Переходит в режим ожидания запросов;
   print("Переходит в режим ожидания запросов")
   s.settimeout(0.2)  # Таймаут для операций с сокетом
   while True:
       try:
           conn, addr = s.accept()  # Проверка подключений
       except OSError as e:
#           print("timeout вышел")
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
           except:
               pass  # Ничего не делать, если какой-то клиент отключился

           requests_queue = read_requests(r, clients)  # Сохраним запросы клиентов
           if not requests_queue.empty():
               while True:
                   if requests_queue.empty():
                       break
                   item = requests_queue.get()
                   # Обработать элемент
                   write_responses(item, w, clients)  # Выполним отправку ответов клиентам
                   requests_queue.task_done()
               # Конец. Сообщить, что сигнальная метка была принята, и выйти



# Обратите внимание, логгер уже создан в модуле log_config,
# теперь нужно его просто получить
logger.info('Запуск сервера-------------------------------------------------------------')

parser = argparse.ArgumentParser()
parser.add_argument('-a', dest='addr', action='store', type=str, required=False, help='IP-address', default='')
parser.add_argument('-p', dest='port', action='store', type=int, required=False, help='Port', default=7777)
args = parser.parse_args(sys.argv[1:])
mainloop()
