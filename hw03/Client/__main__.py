# Программа клиента для отправки приветствия серверу и получения ответа
import argparse
from socket import *
import json
import sys
import time
from threading import Thread
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

def read_thread(sock):
    while True:
        # необходимо сделать потока на чтение!
        try:
            data = sock.recv(1024)
            logger.debug("Приняли сообщение от сервера")
            response = json.loads(data.decode('utf-8'))
            if int(response["response"]) == 200:
                print("OK")
            print(response["alert"])
        except:
            pass



def write_thread(sock, user):
    while True:
        # необходимо сделать потока на запись!
        msg = input('Ваше сообщение: ')
        if msg == 'exit':
            break
        message_from_client2['message'] = msg
        message_from_client2["user"]["account_name"] = user
        sock.send(json.dumps(message_from_client2).encode())
        print("Сообщение только что отправлено!")


def echo_client(addr, port):

    # Начиная с Python 3.2 сокеты имеют протокол менеджера контекста
    # При выходе из оператора with сокет будет автоматически закрыт
    with socket(AF_INET, SOCK_STREAM) as sock: # Создать сокет TCP
        sock.connect((addr, port))   # Соединиться с сервером
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

        #необходимо сделать 2 потока: на чтение и запись!
        t1 = Thread(target=read_thread, args=(sock, ))
        t1.daemon = True
        t1.start()
        write_thread(sock, user)

if __name__ == '__main__':
    logger.info('Запуск клиента-------------------------------------------------------------')
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', dest='addr', action='store', type=str, required=False, help='IP-address', default='localhost')
    parser.add_argument('-p', dest='port', action='store', type=int, required=False, help='Port', default=7777)
    args = parser.parse_args(sys.argv[1:])

    print("адрес сервера: ", args.addr)
    echo_client(args.addr, args.port)


