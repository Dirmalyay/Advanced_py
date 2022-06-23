import socketserver
import struct
import gevent
from gevent.event import Event


class EchoTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024).strip()
        print('Address: {}'.format(self.client_address[0]))
        print('Data: {}'.format(data.decode()))
        k = data.decode()
        sum_res = 0
        gevent.sleep(3)
        for i in k.split(","):
            sum_res += int(i)
        print("Sum: ", sum_res)
        self.request.sendall(struct.pack(">q", sum_res))


def server1():
    with socketserver.TCPServer(('localhost', 6666), EchoTCPHandler) as server:
        server.serve_forever()
        gevent.sleep(5)


event = Event()
endless_request = gevent.spawn(server1)
tasks = [
   endless_request,
]

gevent.wait(tasks)
