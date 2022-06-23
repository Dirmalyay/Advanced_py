import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 7777))

sock.send(b'6,8')
result = sock.recv(64)
print('Response:', int.from_bytes(result, 'big'))
sock.close()
