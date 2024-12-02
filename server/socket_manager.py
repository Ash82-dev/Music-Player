import socket
import json
from queue import Queue

# Global variable to track whether the user is authenticated
is_authenticated = False
client_socket = None
message_queue = Queue()


def initialize_socket():
    """Initialize the socket connection if not already connected."""
    global client_socket
    if client_socket is None:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 12345))


def listen_to_server():
    """Continuously listen for messages from the server."""
    global client_socket

    try:
        while True:
            if client_socket:
                message = client_socket.recv(1024).decode('utf-8')
                if message:
                    response = json.loads(message)

                    action = response.get('action')
                    if action == "broadcast":
                        print(response["music_list"])
                    else:
                        message_queue.put(message)
    except Exception as e:
        print(f"[ERROR] Disconnected from server: {e}")
        client_socket = None


def register_user(username, password):
    """Register the user with the server."""
    global is_authenticated, client_socket

    initialize_socket()

    user_data = {
        'action': 'register',
        'username': username,
        'password': password
    }

    client_socket.send(json.dumps(user_data).encode('utf-8'))

    # Wait for a response from the queue
    response = json.loads(message_queue.get())  # Blocks until a message is available
    status = response.get("status")
    data = response.get("data", [])

    if status == "Registration successful!":
        is_authenticated = True

    return status, data


def login_user(username, password):
    """Login the user with the server."""
    global is_authenticated, client_socket

    initialize_socket()

    login_data = {
        'action': 'login',
        'username': username,
        'password': password
    }

    client_socket.send(json.dumps(login_data).encode('utf-8'))

    # Wait for a response from the queue
    response = json.loads(message_queue.get())  # Blocks until a message is available
    status = response.get("status")
    data = response.get("data", [])

    if status == "success":
        is_authenticated = True
        return "Login successful!", data
    else:
        is_authenticated = False
        return "Login failed!", data


def play_music(song_name):
    """Send a play music request to the server."""
    global client_socket

    initialize_socket()

    music_request = {
        'action': 'play_music',
        'song_name': song_name
    }

    client_socket.send(json.dumps(music_request).encode('utf-8'))

    # Wait for a response from the queue
    response = json.loads(message_queue.get())  # Blocks until a message is available
    status = response.get("status")

    return status


def pause_music():
    """Send a pause music request to the server."""
    global client_socket

    if not client_socket:
        return "Not connected to the server"

    pause_data = {
        'action': 'pause_music'
    }

    try:
        client_socket.send(json.dumps(pause_data).encode('utf-8'))

        # Wait for a response from the queue
        response = json.loads(message_queue.get())  # Blocks until a message is available
        status = response.get("status")

        return status
    except Exception as e:
        print(f"Error sending pause music request: {e}")
        return "Error pausing music"


def update_music_list():
    print(1)