# Программа сервера для получения приветствия от клиента и отправки ответа
from socket import *
import json
import sys
import argparse
from text import routes

parser = argparse.ArgumentParser()
parser.add_argument('-a', dest='addr', action='store', type=str, required=False, help='IP-address', default='')
parser.add_argument('-p', dest='port', action='store', type=int, required=False, help='Port', default=7777)
args = parser.parse_args(sys.argv[1:])
s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
s.bind((args.addr, args.port))                # Присваивает порт 8888
s.listen(5)                       # Переходит в режим ожидания запросов;
response_dict = {}                                  # Одновременно обслуживает не более                                  # 5 запросов.
while True:
    client, addr = s.accept()
    data = client.recv(1000000)
    request = json.loads(data.decode())
    client_action = request.get('action')
    resolved_routes = list(
        filter(
            lambda itm: itm.get('action') == client_action, routes))
    route = resolved_routes[0] if resolved_routes else None
    if route:
        controller = route.get('controller')
        if "user" in request:
            user = request.get('user')
            response_string = controller(user['account_name'])
        else:
            response_string = controller('')
        response_dict['response'] = 200
        response_dict['alert'] = response_string
    else:
        response_dict['response'] = 401
        response_dict['alert'] = "Action don't support"
    client.send(json.dumps(response_dict).encode())

    if client_action == "quit":
        client.close()
