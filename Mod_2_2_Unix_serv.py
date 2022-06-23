# Создайте UNIX сокет, который принимает сообщение с двумя числами, разделенными запятой.
# Сервер должен конвертировать строковое сообщения в два числа и вычислять его сумму.
# После успешного вычисления возвращать ответ клиенту.
import socketserver
import struct


class EchoTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024).strip()
        print('Address: {}'.format(self.client_address[0]))
        print('Data: {}'.format(data.decode()))
        k = data.decode()
        sum_res = 0
        for i in k.split(","):
            sum_res += int(i)
        print("Sum: ", sum_res)
        self.request.sendall(struct.pack(">q", sum_res))


if __name__ == '__main__':
    with socketserver.TCPServer(('localhost', 7777), EchoTCPHandler) as server:
        server.serve_forever()
