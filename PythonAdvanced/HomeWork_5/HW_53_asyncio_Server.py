"""Разработайте сокет сервер на основе библиотеки asyncio. Сокет сервер принимает сообщение с двумя числами,
разделенными запятой. Сервер должен конвертировать строковое сообщения в два числа и вычислять его сумму. После
успешного вычисления возвращать ответ клиенту.
"""

import socket


def serv():
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.bind(('127.0.0.1', 8888))
    host = socket.gethostname()
    port = 8888
    server_socket = socket.socket()
    server_socket.bind((host, port))
    print('TCP-server started')
    server_socket.listen(1)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        try:
            lst = []
            for t in data.split(','):
                try:
                    lst.append(float(t))
                except ValueError:
                    pass
            # lst = [int(x) for x in data.split(',')]
            print(lst)
            if len(lst) != 0:
                data = str(sum(lst))
                print(data)
            else:
                data = 'Сервер получил неверное значение'
        except ValueError and KeyboardInterrupt:
            data = 'Сервер получил неверное значение'
        finally:
            conn.send(data.encode("utf-8"))

    conn.close()


if __name__ == '__main__':
    serv()
