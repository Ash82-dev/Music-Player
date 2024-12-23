import os
import socket
import threading
import json
from mutagen.mp3 import MP3
from data.user_db.database import get_user_list, add_user, hash_password
import vlc


# Get the absolute path of the directory containing server.py
base_dir = os.path.dirname(os.path.abspath(__file__))
music_folder = os.path.join(base_dir, "..", "data", "music")

clients = []
music_files = []
current_music = ""
authenticated_users = {}
player = vlc.MediaPlayer()


def handle_client(client_socket):
    global clients

    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break

            data = json.loads(message)
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
                broadcast_message()
            elif action == "pause_music":
                response = pause_music()
                broadcast_message()
            elif action == "forward_music":
                song_name = data.get("song_name")
                response = forward_music(song_name)
            elif action == "backward_music":
                song_name = data.get("song_name")
                response = backward_music(song_name)
            elif action == "remove_music":
                song_name = data.get("song_name")
                response = remove_music(song_name)
                broadcast_message()
            elif action == "update_music_list":
                response = update_music_list()
                broadcast_message()

            client_socket.send(json.dumps(response).encode())
        except Exception as e:
            print(f"Error: {e}")
            break

    print(f"client [DISCONNECTED]")
    clients.remove(client_socket)
    client_socket.close()


def broadcast_message():
    """Send a message to all connected clients."""
    global clients

    for client in clients:
        try:
            client.send(json.dumps({"action": "broadcast", "music_list": music_files}).encode('utf-8'))
        except Exception:
            clients.remove(client)


def get_music_list():
    """Return a list of available .mp3 music files."""
    all_music = []

    try:
        for filename in os.listdir(music_folder):
            if filename.endswith(".mp3"):
                file_path = os.path.join(music_folder, filename)
                try:
                    audio = MP3(file_path)
                    duration = int(audio.info.length)
                    formatted_duration = format_duration(duration)
                    is_playing = current_music == filename
                    all_music.append({"filename": filename, "duration": formatted_duration, "is_playing": is_playing})
                except Exception as e:
                    print(f"Error reading metadata for {filename}: {e}")
    except Exception as e:
        print(f"Error reading music files: {e}")
    return all_music


def format_duration(seconds):
    """Convert duration in seconds to minutes:seconds format."""
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{int(minutes)}:{int(seconds):02}"


def register_user(username, password, client_socket):
    """Handle user registration."""
    if username in get_user_list():
        return {
            "status": "Username already taken",
            "data": []
        }

    add_user(username, password)
    authenticated_users[client_socket] = username
    return {
            "status": "Registration successful!",
            "data": music_files
        }


def login_user(username, password, client_socket):
    """Handle user login."""
    user_db = get_user_list()
    if username in user_db and user_db[username] == hash_password(password):
        authenticated_users[client_socket] = username
        return {
                "status": "success",
                "data": music_files
            }
    else:
        return {
                "status": "failure",
                "data": []
        }


def play_music(song_name):
    """Play music from the data/music folder with .mp3 extension using pygame."""
    global current_music

    for music in music_files:
        if music["filename"] == song_name:
            music["is_playing"] = True
        else:
            music["is_playing"] = False

    try:
        if not song_name.endswith(".mp3"):
            song_name += ".mp3"

        file_path = os.path.join(music_folder, song_name)

        if not os.path.exists(file_path):
            print(f"Song not found: {file_path}")
            return {"status": "Song not found"}

        if current_music == song_name:
            player.play()
        else:
            media = vlc.Media(file_path)
            player.set_media(media)
            player.play()

        current_music = song_name
        return {"status": "Playing music"}
    except Exception as e:
        print(f"Error playing music: {e}")
        return {"status": "Error playing music"}


def pause_music():
    """Pause the currently playing music."""
    for music in music_files:
        if music["filename"] == current_music:
            music["is_playing"] = False

    try:
        player.pause()
        return {"status": "Music paused"}
    except Exception as e:
        print(f"Error pausing music: {e}")
        return {"status": "Error pausing music"}


def forward_music(song_name):
    """Skip forward 10 seconds in the current track."""
    if song_name != current_music:
        return {"status": "failed"}

    current_pos = player.get_time() / 1000
    new_pos = current_pos + 10
    player.set_time(int(new_pos * 1000))
    return {"status": "success"}


def backward_music(song_name):
    """Skip backward 10 seconds in the current track."""
    if song_name != current_music:
        return {"status": "failed"}

    current_pos = player.get_time() / 1000
    new_pos = max(0, current_pos - 10)
    player.set_time(int(new_pos * 1000))
    return {"status": "success"}


def remove_music(song_name):
    """remove music from music_list"""
    global music_files

    if song_name == current_music and player.is_playing():
        player.pause()

    for music in music_files:
        if music["filename"] == song_name:
            music_files.remove(music)
            return {"status": "success"}
    return {"status": "failed"}


def update_music_list():
    global music_files

    music_list = get_music_list()
    if music_list != music_files:
        music_files = music_list
        return {
            "status": "music_list_updated"
        }
    else:
        return {
            "status": "no_update"
        }


def start_server():
    global music_files
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(5)
    music_files = get_music_list()
    print("Server running...")

    while True:
        client_socket, addr = server.accept()
        print(f"Connected to {addr}")

        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket,)).start()


if __name__ == "__main__":
    start_server()
