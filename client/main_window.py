from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget, QStackedWidget, QPushButton, QLineEdit, QMessageBox, QDesktopWidget
from server import socket_manager
from server.socket_manager import register_callback, initialize_socket
from views.login_view import login_view
from views.music_container import MusicContainer
from views.music_player_view import music_player_view
from views.signup_view import signup_view

# Global music list
music_list = []


def handle_forward(song_name):
    """Handle forward button click."""
    socket_manager.forward_music(song_name)


def handle_backward(song_name):
    """Handle backward button click."""
    socket_manager.backward_music(song_name)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget(self)
        self.setWindowTitle("Music Player")
        self.setGeometry(100, 100, 600, 800)
        self.center_window()

        self.main_view()

        # Register the callback
        initialize_socket()
        register_callback(self.handle_broadcast)

    def handle_broadcast(self, music_data):
        """handle the broadcast data from server."""
        global music_list

        if len(music_list) == len(music_data):
            self.update_buttons(music_data)
        else:
            self.update_list(music_data)

    def update_buttons(self, music_list):
        """Update the play/pause buttons in MusicContainer widgets based on music_list."""
        music_view = self.stacked_widget.widget(2)
        container_area = music_view.findChild(QWidget, "MusicContainerArea")

        music_dict = {music["filename"]: music for music in music_list}
        for music_container in container_area.findChildren(MusicContainer):
            filename = music_container.name_label.text()
            if filename in music_dict:
                is_playing = music_dict[filename]["is_playing"]
                music_container.play_button.setText("⏸" if is_playing else "▶")

    def update_list(self, updated_music_list):
        """Handle removing music from the UI and update the global music list."""
        global music_list

        # Step 1: Update the global music list with the updated music list
        # First, create a set of filenames from the updated list for easy lookup
        updated_filenames = {music["filename"] for music in updated_music_list}

        # Update music_list by adding new items and keeping the existing ones
        music_list = [music for music in music_list if
                      music["filename"] in updated_filenames]  # Keep only those in updated list
        music_list.extend(music for music in updated_music_list if
                          music["filename"] not in [m["filename"] for m in music_list])  # Add missing items

        # Step 2: Remove music containers that are not in the updated list
        music_view = self.stacked_widget.widget(2)  # Music player view
        container_area = music_view.findChild(QWidget, "MusicContainerArea")
        container_layout = container_area.layout()

        # Iterate over all MusicContainer widgets
        for music_container in container_area.findChildren(MusicContainer):
            container_filename = music_container.name_label.text()  # Assuming name_label holds the filename

            # If the filename of the container is not in the updated music list, remove it
            if container_filename not in updated_filenames:
                container_layout.removeWidget(music_container)
                music_container.deleteLater()

    def center_window(self):
        """Center the main window on the screen."""
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.frameGeometry()
        screen_center = screen_geometry.center()
        window_geometry.moveCenter(screen_center)
        self.move(window_geometry.topLeft())

    def main_view(self):
        """Set up the views and layout."""
        # Create the views
        signup = signup_view()
        login = login_view()
        music = music_player_view()

        # Add views to the stacked widget
        self.stacked_widget.addWidget(signup)
        self.stacked_widget.addWidget(login)
        self.stacked_widget.addWidget(music)

        # Set the initial view to the signup view
        self.stacked_widget.setCurrentWidget(signup)

        # Set the layout for the main window
        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

        # Connect buttons to actions
        signup.findChild(QPushButton, "Sign Up").clicked.connect(self.handle_signup)
        signup.findChild(QPushButton, "Switch to Login").clicked.connect(self.switch_to_login)
        login.findChild(QPushButton, "Login").clicked.connect(self.handle_login)
        login.findChild(QPushButton, "Switch to Sign Up").clicked.connect(self.switch_to_signup)

        # Connect the "+" button
        music.findChild(QPushButton, "AddMusicButton").clicked.connect(self.handle_add_music)

    def switch_to_login(self):
        """Switch to the login view."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.widget(1))

    def switch_to_signup(self):
        """Switch to the signup view."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.widget(0))

    def switch_to_music_view(self):
        """Switch to the music player view."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.widget(2))

    def handle_signup(self):
        """Handle the signup logic."""
        global music_list
        username = self.stacked_widget.widget(0).findChild(QLineEdit, "signup_username_input").text()
        password = self.stacked_widget.widget(0).findChild(QLineEdit, "signup_password_input").text()

        if not username or not password:
            QMessageBox.warning(self, "Input Error", "Both username and password fields must be filled out.")
            return

        response, music_list = socket_manager.register_user(username, password)

        if response == "Registration successful!":
            self.switch_to_music_view()
            for music in music_list:
                self.add_music(music["filename"], music["duration"])
            self.update_buttons(music_list)
        else:
            QMessageBox.information(self, "Error", response)

    def handle_login(self):
        """Handle the login logic."""
        global music_list
        username = self.stacked_widget.widget(1).findChild(QLineEdit, "login_username_input").text()
        password = self.stacked_widget.widget(1).findChild(QLineEdit, "login_password_input").text()

        response, music_list = socket_manager.login_user(username, password)

        if response == "Login successful!":
            self.switch_to_music_view()
            for music in music_list:
                self.add_music(music["filename"], music["duration"])
            self.update_buttons(music_list)
        else:
            QMessageBox.information(self, "Error", response)

    def handle_add_music(self):
        """Handle adding a new music container."""
        global music_list

        # Example new music data (replace with user input later)
        new_song = {"name": f"New Song {len(music_list) + 1}", "duration": "00:00"}
        self.add_music(new_song["name"], new_song["duration"])

    def add_music(self, name, duration):
        """Add a new music container to the view and global music list."""
        music_view = self.stacked_widget.widget(2)
        container_area = music_view.findChild(QWidget, "MusicContainerArea")
        container_layout = container_area.layout()

        music_container = MusicContainer(name, duration)

        music_container.play_button.clicked.connect(lambda: self.toggle_play_pause(name))
        music_container.forward_button.clicked.connect(lambda: handle_forward(name))
        music_container.backward_button.clicked.connect(lambda: handle_backward(name))
        music_container.remove_button.clicked.connect(lambda: self.remove_music(name))

        container_layout.addWidget(music_container)

    def toggle_play_pause(self, song_name):
        """Handle play/pause toggle."""
        button = self.sender()

        if button.text() == "▶":
            # If the button shows "▶", play the song
            if not song_name.strip():
                QMessageBox.warning(self, "Error", "Please enter a song name!")
                return

            # Send play request to the server
            response = socket_manager.play_music(song_name)

            if response == "Playing music":
                # Reset all other play/pause buttons to "Play"
                self.reset_play_buttons()

                button.setText("⏸")  # Update button text to "Pause"
            else:
                QMessageBox.warning(self, "Error", response)
        else:
            # Pause the music
            response = socket_manager.pause_music()

            if response == "Music paused":
                button.setText("▶")  # Update button text to "Play"
            else:
                QMessageBox.warning(self, "Error", response)

    def reset_play_buttons(self):
        """Reset all other play/pause buttons to '▶'."""
        # Iterate over all the buttons and reset them to "Play"
        for widget in self.stacked_widget.widget(2).findChildren(QPushButton):
            if widget.text() == "⏸":
                widget.setText("▶")

    def remove_music(self, song_name):
        """Handle removing music."""
        global music_list

        for music in music_list:
            if music["filename"] == song_name:
                music_list.remove(music)

        socket_manager.remove_music(song_name)

        # Find the music view and the container area
        music_view = self.stacked_widget.widget(2)  # Music player view
        container_area = music_view.findChild(QWidget, "MusicContainerArea")
        container_layout = container_area.layout()

        # Iterate over the MusicContainer widgets and find the one with the matching name
        for music_container in container_area.findChildren(MusicContainer):
            if music_container.name_label.text() == song_name:
                # Remove the container from the layout and delete the widget
                container_layout.removeWidget(music_container)
                music_container.deleteLater()
                break  # Exit the loop once the matching container is removed
