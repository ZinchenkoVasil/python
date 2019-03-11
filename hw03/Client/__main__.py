# Программа клиента для отправки приветствия серверу и получения ответа
from socket import *
import json
import sys
import time

message_from_client = {
        "action": "presence",
        "time": "",
        "type": "status",
        "user": {
                "account_name":  "Vasia",
                "status":      "Yep, I am here!"
        }
}

quit_session = {
    "action": "quit"
}

try:
    addr = sys.argv[1]
except IndexError:
    addr = 'localhost'

try:
    port  = int(sys.argv[2])
except:
    port = 7777

s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
s.connect((addr, port))   # Соединиться с сервером
message_from_client['time'] = time.ctime(time.time())
s.send(json.dumps(message_from_client).encode())
data = s.recv(1000000)
response = json.loads(data.decode('utf-8'))
if int(response["response"]) == 200:
    print("OK")
else:
    print(response["alert"])
s.send(json.dumps(quit_session).encode())
s.close()
