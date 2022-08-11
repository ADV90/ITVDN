"""Создайте FTP(UNIX) сокет, который принимает сообщение с двумя числами, разделенными запятой. Сервер должен
конвертировать строковое сообщения в два числа и вычислять его сумму. После успешного вычисления возвращать ответ
клиенту.
"""

import socket


def client_program():
    # client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client_socket.connect(("127.0.0.1", 8888))
    host = socket.gethostname()
    port = 8888
    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input('Введите два числа через ",": ')

    while message.strip().casefold() != 'stop':
        client_socket.send(message.encode("utf-8"))
        data = client_socket.recv(1024).decode()

        print('Received from server: ' + data)

        message = input('Введите два числа через ",": ')

    client_socket.close()


if __name__ == '__main__':
    client_program()
