import socket
import select
import sys

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9999
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.setblocking(False)

nickname = input("Podaj nickname: ")

sock.sendto(b"\0" + nickname.encode("utf-8"), (SERVER_IP, SERVER_PORT))

print("Zacznij pisanie wiadomości. Aby wyjść napisz /q")

while True:
    readable, _, _ = select.select([sock, sys.stdin], [], [])

    for source in readable:
        if source == sys.stdin:
            message = input()

            if message == "/q":
                sock.sendto(b"", (SERVER_IP, SERVER_PORT))
                print("Połączenie zakończone")
                sys.exit(0)

            packet = b"\1" + message.encode("utf-8")

            sock.sendto(packet, (SERVER_IP, SERVER_PORT))

        elif source == sock:
            data, addr = sock.recvfrom(BUFFER_SIZE)
            print(data.decode("utf-8"))