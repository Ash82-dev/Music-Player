import os
import socket
import threading
import json

import pygame

# Initialize pygame and play the music
pygame.mixer.init()

# A simple in-memory user database (username:password)
user_db = {
    "a": "1"
}

# This dictionary will store the authenticated users' sockets
authenticated_users = {}

# Get the absolute path of the directory containing server.py
base_dir = os.path.dirname(os.path.abspath(__file__))
music_folder = os.path.join(base_dir, "..", "data", "music")

clients = []


def handle_client(client_socket):
    global clients

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
            elif action == "play_music":
                song_name = data.get("song_name")
                response = play_music(song_name)
                broadcast_message(f"Playing {song_name}")
            elif action == "pause_music":
                response = pause_music()

            client_socket.send(json.dumps(response).encode())
        except Exception as e:
            print(f"Error: {e}")
            break

    print(f"client [DISCONNECTED]")
    clients.remove(client_socket)
    client_socket.close()


def broadcast_message(message):
    """Send a message to all connected clients."""
    global clients

    for client in clients:
        try:
            client.send(json.dumps({"action": "broadcast", "message": message}).encode('utf-8'))
        except Exception:
            clients.remove(client)


def get_music_list():
    """Return a list of available .mp4 music files."""
    music_files = []
    try:
        for filename in os.listdir(music_folder):
            if filename.endswith(".mp3"):
                music_files.append(filename)
    except Exception as e:
        print(f"Error reading music files: {e}")
    return music_files


def register_user(username, password, client_socket):
    """Handle user registration."""
    if username in user_db:
        return {
            "status": "Username already taken",
            "data": []  # You can add an empty array or any relevant data here
        }

    user_db[username] = password
    authenticated_users[client_socket] = username
    return {
            "status": "Registration successful!",
            "data": get_music_list()
        }


def login_user(username, password, client_socket):
    """Handle user login."""
    if username in user_db and user_db[username] == password:
        authenticated_users[client_socket] = username
        return {
                "status": "success",
                "data": get_music_list()
            }
    else:
        return {
                "status": "failure",
                "data": []  # You can add an empty array or any relevant data here
        }


def play_music(song_name):
    """Play music from the data/music folder with .mp3 extension using pygame."""
    try:
        # Ensure the file has the correct extension
        if not song_name.endswith(".mp3"):
            song_name += ".mp3"

        # Construct the full file path
        file_path = os.path.join(music_folder, song_name)

        if not os.path.exists(file_path):
            print(f"Song not found: {file_path}")
            return {"status": "Song not found"}

        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        print(f"Playing song: {song_name}")
        return {"status": "Playing music"}
    except Exception as e:
        print(f"Error playing music: {e}")
        return {"status": "Error playing music"}


def pause_music():
    """Pause the currently playing music."""
    try:
        pygame.mixer.music.pause()
        return {"status": "Music paused"}
    except Exception as e:
        print(f"Error pausing music: {e}")
        return {"status": "Error pausing music"}


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(5)
    print("Server running...")

    while True:
        client_socket, addr = server.accept()
        print(f"Connected to {addr}")

        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket,)).start()


if __name__ == "__main__":
    start_server()
