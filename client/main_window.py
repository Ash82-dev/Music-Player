from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget, QMessageBox
import socket_manager
from auth_view import auth_view


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Authentication")
        self.setGeometry(100, 100, 300, 250)
        auth_view(self)

    def switch_to_login(self):
        """Switch to the login view."""
        self.stacked_widget.setCurrentWidget(self.login_view)

    def switch_to_signup(self):
        """Switch to the signup view."""
        self.stacked_widget.setCurrentWidget(self.signup_view)

    def handle_signup(self):
        """Handle the signup logic."""
        username = self.signup_view.findChild(QLineEdit, "signup_username_input").text()
        password = self.signup_view.findChild(QLineEdit, "signup_password_input").text()

        response = socket_manager.register_user(username, password)
        QMessageBox.information(self, "Success", response)

        if response == "Registration successful!":
            self.switch_to_message_window()

    def switch_to_message_window(self):
        """Switch to the message window after successful signup."""
        self.stacked_widget.setCurrentWidget(self.message_view)

    def handle_login(self):
        """Handle the login logic."""
        username = self.login_view.findChild(QLineEdit, "login_username_input").text()
        password = self.login_view.findChild(QLineEdit, "login_password_input").text()

        response = socket_manager.login_user(username, password)
        QMessageBox.information(self, "Success", response)

        if response == "Login successful!":
            self.switch_to_message_window()

    def send_message(self):
        """Handle message sending."""
        message = self.message_view.findChild(QLineEdit, "message_input").text()
        response = socket_manager.send_message_to_server(message)
        QMessageBox.information(self, "Server Response", response)
