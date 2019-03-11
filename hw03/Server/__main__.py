# Программа сервера для получения приветствия от клиента и отправки ответа
from socket import *
import json
import sys
import argparse


#ответ сервера
response ={
    "response": 200,
    "alert":"OK"
}

parser = argparse.ArgumentParser()
parser.add_argument('-a', dest='addr', action='store', type=str, required=False, help='IP-address', default='')
parser.add_argument('-p', dest='port', action='store', type=int, required=False, help='Port', default=7777)
args = parser.parse_args(sys.argv[1:])
s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
s.bind((args.addr, args.port))                # Присваивает порт 8888
s.listen(5)                       # Переходит в режим ожидания запросов;
                                  # Одновременно обслуживает не более                                  # 5 запросов.
while True:
    client, addr = s.accept()
    data = client.recv(1000000)
    message_from_client = json.loads(data.decode())
#    print('Сообщение: ', data.decode('utf-8'), ', было отправлено клиентом: ', addr)
    #парсинг сообщения от клиента
    if message_from_client["action"] == "presence":
        user = message_from_client["user"]
        print(f"{user['account_name']}: {user['status']}")
        client.send(json.dumps(response).encode())
    if message_from_client["action"] == "quit":
        client.close()
