# Разработайте сокет сервер на основе библиотеки asyncio. Сокет сервер должен выполнять сложение двух чисел,
# как из предыдущего примера по многопоточности.
import socket
import asyncio


async def handle_client(client):
    loop = asyncio.get_event_loop()
    request = None
    while request != 'q':
        request = (await loop.sock_recv(client, 255)).decode('utf8')
        response = str(eval(request)) + '\n'
        await loop.sock_sendall(client, response.encode('utf8'))
        client.close()


async def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 7777))
    server.listen(5)
    server.setblocking(False)
    loop = asyncio.get_event_loop()
    while True:
        client, _ = await loop.sock_accept(server)
        loop.create_task(handle_client(client))

asyncio.run(run_server())