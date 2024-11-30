import socket
import threading
import json

# A simple in-memory user database (username:password)
user_db = {}

# This dictionary will store the authenticated users' sockets
authenticated_users = {}


def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break

            data = json.loads(message)  # Parse the incoming message
            action = data.get("action")

            if action == "register":
                username = data.get("username")
                password = data.get("password")
                response = register_user(username, password, client_socket)
            elif action == "login":
                username = data.get("username")
                password = data.get("password")
                response = login_user(username, password, client_socket)

            client_socket.send(response.encode())
        except Exception as e:
            print(f"Error: {e}")
            break

    client_socket.close()


def register_user(username, password, client_socket):
    """Handle user registration."""
    if username in user_db:
        return "Username already taken"

    user_db[username] = password
    authenticated_users[client_socket] = username
    return "Registration successful!"


def login_user(username, password, client_socket):
    """Handle user login."""
    if username in user_db and user_db[username] == password:
        authenticated_users[client_socket] = username
        return "success"
    else:
        return "failure"


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
