import socket
import threading
import json

HOST = "0.0.0.0"
PORT = 5001

users = {}
online_users = {}

users_lock = threading.Lock()
online_lock = threading.Lock()

def send_json(sock, data):
    sock.sendall((json.dumps(data) + "\n").encode())

def broadcast(data, exclude=None):
    print("BROADCAST:", data)

    with online_lock:
        for user, sock in online_users.items():
            if user != exclude:
                try:
                    send_json(sock, data)
                except:
                    pass

def list_user():
    with online_lock:
        current_user = list(online_users.keys())

        for sock in online_users.values():
            send_json(sock, {
                "type": "users",
                "users": current_user
            })

def client_thread(client_socket):
    username = None

    try:
        file = client_socket.makefile("r")

        while True:
            line = file.readline()

            if not line:
                break

            msg = json.loads(line)
            cmd = msg.get("cmd")

            if cmd == "register":
                user = msg["user"]
                password = msg["pass"]

                with users_lock:
                    if user in users:
                        send_json(client_socket, {
                            "type": "error",
                            "message": "Uzytkownik o tej nazwie istnieje."
                        })
                    else:
                        users[user] = password
                        send_json(client_socket, {
                            "type": "ok",
                            "message": "Rejestracja przebiegła pomyślnie."
                        })

            elif cmd == "login":
                user = msg["user"]
                password = msg["pass"]

                with users_lock:
                    valid = user in users and users[user] == password

                if not valid:
                    send_json(client_socket, {
                        "type": "error",
                        "message": "Nieprawidlowy login."
                    })
                    continue
                
                username = user

                with online_lock:
                    online_users[username] = client_socket

                send_json(client_socket, {
                    "type": "ok",
                    "message": "Zalogowany."
                })

                list_user()

                broadcast({
                    "type": "notification",
                    "message": f"{username} joined"
                }, exclude=username)

            elif cmd == "private":
                recipient = msg["to"]
                text = msg["message"]

                with online_lock:
                    if recipient in online_users:
                        send_json(
                            online_users[recipient],
                            {
                                "type": "private",
                                "from": username,
                                "message": text
                            }
                        )

            elif cmd == "broadcast":
                text = msg["message"]
                broadcast({
                    "type": "broadcast",
                    "from": username,
                    "message": text
                })

    except Exception as e:
        print("Client error:", e)

    finally:
        if username:
            with online_lock:
                online_users.pop(username, None)

            broadcast({
                "type": "notification",
                "message": f"{username} wyszedl"
            })

            list_user()

        client_socket.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Serwer nasluchuje na {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        print("Polaczono:", addr)

        thread = threading.Thread(target=client_thread, args=(client_socket,))
        thread.daemon = True
        thread.start()

if __name__ == "__main__":
    main()
