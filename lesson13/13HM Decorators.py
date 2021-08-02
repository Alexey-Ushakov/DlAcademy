import socket
import time
import json
import re
from log_config import app_log
from functools import wraps


host = '0.0.0.0'
port = 35200
clients = {}

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))
quit = False
print('[Server Started]')

def decorator(func):

    @wraps(func)
    def inner(*args, **kwargs):
        app_log.info('This is logging info {}'.format(*args))
        r = func(*args, **kwargs)
        return r
    # inner.__name__ = func.__name__
    # inner.__doc__ = func.__doc__
    return inner

@decorator
def loging(addr, data):
    """
    This func
    :param addr:
    :param data:
    :return:
    """
    itsattime = time.strftime('%Y-%m-%d-%H.%M.%S', time.localtime())
    print(addr, itsattime, '', end="")
    print(data)


while not quit:
    try:
        data, addr = s.recvfrom(1024)
        data = json.loads(data)  # Со словарем будет проще работать

        if addr not in clients:  # Делаем словарь из адрессов и привязываем к ним имена что отправляються
            # первым сообщением
            clients.update({addr: data["name"]})
            print(clients)

        loging(addr, data)

        who_send_massege = re.findall(r"\w+", data['message'])  # Условие если первым словом в сообщение являетсья имя
        # другого пользователя который есть в чате сообщение отправиться только ему
        if who_send_massege[0] in clients.values():
            for addr_n, name in clients.items():
                if who_send_massege[0] == name:
                    s.sendto(json.dumps(data).encode("utf-8"), addr_n)
        else:
            for client in clients:
                if addr != client:
                    s.sendto(json.dumps(data).encode('utf-8'), client)

    except Exception as ex:
        print(ex)
        print('\n[ Server Stopped ]')
        quit = True

s.close()

