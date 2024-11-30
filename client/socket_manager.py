import socket
import json

# Global variable to track whether the user is authenticated
is_authenticated = False
client_socket = None


# Function to initialize the socket connection
def initialize_socket():
    global client_socket
    if client_socket is None:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 12345))


# Function to register the user
def register_user(username, password):
    global is_authenticated, client_socket

    initialize_socket()

    user_data = {
        'action': 'register',
        'username': username,
        'password': password
    }

    # Send data to the server
    client_socket.send(json.dumps(user_data).encode('utf-8'))
    response = client_socket.recv(1024).decode('utf-8')

    # Registration is successful if no errors are returned
    if response == "Registration successful!":
        is_authenticated = True

    return response


# Function to login the user
def login_user(username, password):
    global is_authenticated, client_socket

    # Ensure the socket is initialized
    initialize_socket()

    # Prepare the login data to be sent to the server
    login_data = {
        'action': 'login',
        'username': username,
        'password': password
    }

    # Send login data to the server
    client_socket.send(json.dumps(login_data).encode('utf-8'))
    response = client_socket.recv(1024).decode('utf-8')

    if response == "success":
        is_authenticated = True
    else:
        is_authenticated = False

    return "Login successful!" if is_authenticated else "Login failed!"
