from .controllers import (get_response, get_message)

routes = [
    {'action': 'presence', 'controller': get_response},
    {'action': 'message', 'controller': get_message}

]