import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 8888))
    print('UDP-server started')

    while True:
        try:
            result = sock.recv(1024)
        except KeyboardInterrupt:
            break
        else:
            msg = result.decode('utf-8')
            if msg.strip().lower() == "stop":
                break
            else:
                print('Добавлено устройство:', msg)
    print('UDP-server finished')
    sock.close()


if __name__ == '__main__':
    main()
