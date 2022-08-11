import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        msg = input('Введите сообщение на сервер: ')
        msgb = msg.encode('utf-8')
        sock.sendto(msgb, ('127.0.0.1', 8888))

        if msg.strip().lower() == "stop":
            break


if __name__ == '__main__':
    main()
