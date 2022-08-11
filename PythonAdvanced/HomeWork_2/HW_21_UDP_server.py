"""Создайте UDP сервер, который ожидает сообщения о новых устройствах в сети. Он принимает сообщения определенного
формата, в котором будет идентификатор устройства и печатает новые подключения в консоль. Создайте UDP клиента,
который будет отправлять уникальный идентификатор устройства на сервер, уведомляя о своем присутствии.
"""

import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 8888))
    print('UDP-server started')

    while True:
        try:
            result = sock.recv(1024)
        except KeyboardInterrupt:
            sock.close()
            break
        else:
            msg = result.decode('utf-8')
            if msg.strip().casefold() == "stop":
                break
            else:
                print('Добавлено устройство:', msg)
    print('UDP-server finished')
    sock.close()


if __name__ == '__main__':
    main()
