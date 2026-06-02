import socket

HOST = "0.0.0.0"
PORT = 9999
BUFFER_SIZE = 1024

users = {}

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print(f"Serwer nasłuchuje na {HOST}:{PORT}")

while True:
    data, addr = sock.recvfrom(BUFFER_SIZE)

    if len(data) == 0:
        if addr in users:
            nickname = users[addr]
            print(f"[DISCONNECT] {nickname} {addr}")
            del users[addr]
        continue

    packet_type = data[:1]
    payload = data[1:]

    if packet_type == b"\0":
        nickname = payload.decode("utf-8")

        users[addr] = nickname

        print(f"[LOGIN] {nickname} {addr}")

    elif packet_type == b"\1":
        if addr not in users:
            print(f"[IGNORED] Nieznany uztkownik {addr}")
            continue

        nickname = users[addr]
        message = payload.decode("utf-8")

        print(f"[MESSAGE] {nickname}: {message}")

        outgoing = f"{nickname}: {message}".encode("utf-8")

        for client_addr in users:
            if client_addr != addr:
                sock.sendto(outgoing, client_addr)