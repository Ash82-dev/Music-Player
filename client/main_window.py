from PyQt5.QtWidgets import QWidget, QVBoxLayout, QStackedWidget, QPushButton, QLineEdit, QMessageBox, QDesktopWidget
import socket_manager
from views.signup_view import signup_view
from views.login_view import login_view
from views.message_view import message_view
from views.music_view import music_view


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget(self)
        self.setWindowTitle("Music Player")
        self.setGeometry(100, 100, 800, 600)
        self.center_window()

        self.main_view()

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
        message = message_view()
        music = music_view()

        # Add views to the stacked widget
        self.stacked_widget.addWidget(signup)
        self.stacked_widget.addWidget(login)
        self.stacked_widget.addWidget(message)
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
        message.findChild(QPushButton, "Send").clicked.connect(self.send_message)

    def switch_to_login(self):
        """Switch to the login view."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.widget(1))

    def switch_to_signup(self):
        """Switch to the signup view."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.widget(0))

    def switch_to_message_window(self):
        """Switch to the message window after successful signup."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.widget(2))

    def switch_to_music_view(self):
        """Switch to the music player view."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.widget(3))

    def handle_signup(self):
        """Handle the signup logic."""
        username = self.stacked_widget.widget(0).findChild(QLineEdit, "signup_username_input").text()
        password = self.stacked_widget.widget(0).findChild(QLineEdit, "signup_password_input").text()

        if not username or not password:
            QMessageBox.warning(self, "Input Error", "Both username and password fields must be filled out.")
            return

        response = socket_manager.register_user(username, password)

        if response == "Registration successful!":
            self.switch_to_music_view()
        else:
            QMessageBox.information(self, "Error", response)

    def handle_login(self):
        """Handle the login logic."""
        username = self.stacked_widget.widget(1).findChild(QLineEdit, "login_username_input").text()
        password = self.stacked_widget.widget(1).findChild(QLineEdit, "login_password_input").text()

        response = socket_manager.login_user(username, password)

        if response == "Login successful!":
            self.switch_to_music_view()
        else:
            QMessageBox.information(self, "Error", response)

    def send_message(self):
        """Handle message sending."""
        message = self.stacked_widget.widget(2).findChild(QLineEdit, "message_input").text()
        response = socket_manager.send_message_to_server(message)
        QMessageBox.information(self, "Server Response", response)
