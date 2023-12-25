import socket
import threading

from typing import Tuple

HEADER: int = 64
PORT: int = 5000
SERVER: str = socket.gethostbyname(socket.gethostname())
ADDR: Tuple[str, int] = (SERVER, PORT)
FORMAT: str = "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn: socket.socket, addr: Tuple[str, int]):
    print(f"[CONNECTIONS] New connection: {addr}")
    connected: bool = True
    while connected:
        msg_length: int = int(conn.recv(HEADER).decode(FORMAT))
        msg: str = conn.recv(msg_length).decode(FORMAT)
        print(f"[{addr}] {msg}")


def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread: threading.Thread = threading.Thread(
            target=handle_client, args=(conn, addr)
        )
        thread.start()
        print(f"[CONNECTIONS] Active connections: {threading.activeCount() - 1}")


print("[STARTING] Server is starting...")
start()
