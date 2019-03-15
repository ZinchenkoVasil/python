#ответ сервера на запрос установления соединения


#def get_upper_text(data):
#    return data.upper()

def get_response(account_name):
    if account_name:
        return "Hello, " + account_name
    else:
        return "Hello"
