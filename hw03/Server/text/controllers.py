#ответ сервера на запрос установления соединения
from Server.decorators import *

#def get_upper_text(data):
#    return data.upper()
@log
def get_response(account_name, data):
    if account_name:
        return "Hello, " + account_name
    else:
        return "Hello"

@log
def get_message(account_name, data):
    if account_name:
        return account_name + ": " + data
    else:
        return data


