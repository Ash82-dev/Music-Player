import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import client_logic


class SignupWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.message_window = MessageWindow()
        self.setWindowTitle("Sign Up")
        self.setGeometry(100, 100, 300, 200)

        # Create widgets for signup
        self.username_label = QLabel("Username", self)
        self.username_input = QLineEdit(self)
        self.password_label = QLabel("Password", self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.signup_button = QPushButton("Sign Up", self)

        # Set layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.signup_button)

        self.signup_button.clicked.connect(self.handle_signup)

    def handle_signup(self):
        username = self.username_input.text()
        password = self.password_input.text()

        response = client_logic.register_user(username, password)
        QMessageBox.information(self, "Success", response)
        self.close()  # Close the signup window
        self.message_window.show()


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.message_window = MessageWindow()
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 300, 200)

        # Create widgets for login
        self.username_label = QLabel("Username", self)
        self.username_input = QLineEdit(self)
        self.password_label = QLabel("Password", self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton("Login", self)

        # Set layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.login_button.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        response = client_logic.login_user(username, password)
        if response == "Login successful!":
            QMessageBox.information(self, "Success", "Login successful!")
            self.close()  # Close the login window
            self.message_window.show()
        else:
            QMessageBox.warning(self, "Error", "Login failed!")


class MessageWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Message Window")
        self.setGeometry(100, 100, 400, 200)

        # Create widgets for sending messages
        self.message_label = QLabel("Enter your message", self)
        self.message_input = QLineEdit(self)
        self.send_button = QPushButton("Send", self)

        # Set layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.message_label)
        layout.addWidget(self.message_input)
        layout.addWidget(self.send_button)

        self.send_button.clicked.connect(self.send_message)

    def send_message(self):
        message = self.message_input.text()
        response = client_logic.send_message_to_server(message)
        QMessageBox.information(self, "Server Response", response)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SignupWindow()
    window.show()
    sys.exit(app.exec_())
