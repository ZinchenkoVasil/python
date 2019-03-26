# Программа клиента для отправки приветствия серверу и получения ответа
import argparse
from socket import *
import json
import sys
import time

from Log.client_log_config import *

# Обратите внимание, логгер уже создан в модуле log_config,
# теперь нужно его просто получить
#logger = logging.getLogger('client.main')

message_from_client = {
        "action": "presence",
        "time": "",
        "type": "status",
        "user": {
                "account_name":  "Vasia",
                "status":      "Yep, I am here!"
        }
}

message_from_client2 = {
        "action": "message",
        "time": "",
        "message": "",
        "user": {
                "account_name":  "Vasia",
                "status":      "Yep, I am here!"
        }
}

def echo_client():
    # Начиная с Python 3.2 сокеты имеют протокол менеджера контекста
    # При выходе из оператора with сокет будет автоматически закрыт
    with socket(AF_INET, SOCK_STREAM) as sock: # Создать сокет TCP
        sock.connect((args.addr, args.port))   # Соединиться с сервером
        logger.debug("Соединиться с сервером")
        message_from_client['time'] = time.ctime(time.time())
        user = input('Имя пользователя: ')
        message_from_client["user"]["account_name"] = user
        sock.send(json.dumps(message_from_client).encode())
        logger.debug("Послали сообщение серверу")
        data = sock.recv(1000000)
        logger.debug("Приняли сообщение от сервера")
        response = json.loads(data.decode('utf-8'))
        if int(response["response"]) == 200:
            print("OK")
        print(response["alert"])
        while True:
            if args.w:
                msg = input('Ваше сообщение: ')
                if msg == 'exit':
                    break
                message_from_client2['message'] = msg
                message_from_client2["user"]["account_name"] = user
                sock.send(json.dumps(message_from_client2).encode())
                print("Сообщение только что отправлено!")
            print("сейчас будем принимать ответ от сервера")
            data = sock.recv(1024)
            logger.debug("Приняли сообщение от сервера")
            response = json.loads(data.decode('utf-8'))
            if int(response["response"]) == 200:
                print("OK")
            print(response["alert"])



if __name__ == '__main__':
    logger.info('Запуск клиента-------------------------------------------------------------')
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', dest='addr', action='store', type=str, required=False, help='IP-address', default='localhost')
    parser.add_argument('-p', dest='port', action='store', type=int, required=False, help='Port', default=7777)
    parser.add_argument('--w', action='store_true', default=False)
    parser.add_argument('--r', action='store_true', default=True)

    args = parser.parse_args(sys.argv[1:])
    echo_client()
