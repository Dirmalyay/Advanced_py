# Создайте UDP сервер, который ожидает сообщения о новых устройствах в сети.
# Он принимает сообщения определенного формата, в котором будет идентификатор устройства и печатает новые
# подключения в консоль. Создайте UDP клиента, который будет отправлять уникальный идентификатор устройства на сервер,
# уведомляя о своем присутствии.
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 7777))

while True:
    try:
        res = sock.recv(1024)
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        print(res.decode('utf-8'))

# with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
#    print('8888 is bind')
#    sock.bind(('127.0.0.1', 7777))
#
#    while True:
#        result = sock.recv(1024)
#        print('Message', result.decode('utf-8'))
