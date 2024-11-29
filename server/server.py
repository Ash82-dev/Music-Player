import socket
import threading


def handle_client(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        print(f"Received: {message}")
        client_socket.send(f"ECHO: {message}".encode())
    client_socket.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(5)
    print("Server running...")

    while True:
        client_socket, addr = server.accept()
        print(f"Connected to {addr}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()


if __name__ == "__main__":
    start_server()
