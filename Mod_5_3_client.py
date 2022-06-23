import socket
import gevent


def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 6666))

    sock.send(b'6,8')
    gevent.sleep(1)
    result = sock.recv(64)
    print('Response:', int.from_bytes(result, 'big'))
    sock.close()


tasks = [
    gevent.spawn(client)
]

gevent.joinall(tasks)
