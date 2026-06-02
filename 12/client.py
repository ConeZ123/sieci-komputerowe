import socket
import json
import threading

HOST="127.0.0.1"
PORT = 5001

def send_json(sock, data):
    sock.sendall((json.dumps(data) + "\n").encode())

def receive_thread(sock):
    file = sock.makefile("r")

    while True:
        try:
            line = file.readline()
            if not line:
                print("Rozlaczono z serwerem")
                break

            msg = json.loads(line)
            print("\n[SERVER]", msg)
        except:
            break

def send_thread(sock):
    print("""
Komendy:
register <uzytkownik> <haslo>
login <uzytkownik> <haslo>
msg <uzytkownik> <tresc>
all <text>
quit
""")
    
    while True:
        command = input("> ")

        if command == "quit":
            sock.close()
            break

        parts = command.split()

        if not parts:
            continue

        if parts[0] == "register" and len(parts) == 3:
            send_json(sock, {
                "cmd": "register",
                "user": parts[1],
                "pass": parts[2]
            })

        elif parts[0] == "login" and len(parts) == 3:
            send_json(sock, {
                "cmd": "login",
                "user": parts[1],
                "pass": parts[2]
            })

        elif parts[0] == "msg" and len(parts) >= 3:
            recipient = parts[1]
            text = " ".join(parts[2:])

            send_json(sock, {
                "cmd": "private",
                "to": recipient,
                "message": text
            })

        elif parts[0] == "all" and len(parts) >= 2:
            text = " ".join(parts[1:])

            send_json(sock, {
                "cmd": "broadcast",
                "message": text
            })

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    threading.Thread(target=receive_thread, args=(sock,), daemon=True).start()
    send_thread(sock)

if __name__ == "__main__":
    main()
