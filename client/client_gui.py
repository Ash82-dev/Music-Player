import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, \
    QStackedWidget
import client_logic


class AuthWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.signup_password_input = QLineEdit(self)
        self.signup_password_label = QLabel("Password", self)
        self.signup_username_input = QLineEdit(self)
        self.signup_username_label = QLabel("Username", self)
        self.message_input = QLineEdit(self)
        self.send_button = QPushButton("Send", self)
        self.message_label = QLabel("Enter your message", self)
        self.switch_to_signup_button = QPushButton("Switch to Sign Up", self)
        self.login_button = QPushButton("Login", self)
        self.login_password_input = QLineEdit(self)
        self.login_password_label = QLabel("Password", self)
        self.login_username_input = QLineEdit(self)
        self.login_username_label = QLabel("Username", self)
        self.switch_to_login_button = QPushButton("Switch to Login", self)
        self.signup_button = QPushButton("Sign Up", self)
        self.setWindowTitle("Authentication")
        self.setGeometry(100, 100, 300, 250)

        # Create the QStackedWidget to hold the views
        self.stacked_widget = QStackedWidget(self)

        # Create the SignUp, LogIn, and Message views
        self.signup_view = self.create_signup_view()
        self.login_view = self.create_login_view()
        self.message_view = self.create_message_view()

        # Add views to stacked widget
        self.stacked_widget.addWidget(self.signup_view)
        self.stacked_widget.addWidget(self.login_view)
        self.stacked_widget.addWidget(self.message_view)

        # Set the initial view to the signup view
        self.stacked_widget.setCurrentWidget(self.signup_view)

        # Set the layout for the main window
        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

    def create_signup_view(self):
        """Create the signup view."""
        view = QWidget(self)
        layout = QVBoxLayout(view)

        # Create widgets for signup
        self.signup_password_input.setEchoMode(QLineEdit.Password)

        # Connect buttons
        self.signup_button.clicked.connect(self.handle_signup)
        self.switch_to_login_button.clicked.connect(self.switch_to_login)

        # Add widgets to layout
        layout.addWidget(self.signup_username_label)
        layout.addWidget(self.signup_username_input)
        layout.addWidget(self.signup_password_label)
        layout.addWidget(self.signup_password_input)
        layout.addWidget(self.signup_button)
        layout.addWidget(self.switch_to_login_button)

        return view

    def create_login_view(self):
        """Create the login view."""
        view = QWidget(self)
        layout = QVBoxLayout(view)

        # Create widgets for login
        self.login_password_input.setEchoMode(QLineEdit.Password)

        # Connect buttons
        self.login_button.clicked.connect(self.handle_login)
        self.switch_to_signup_button.clicked.connect(self.switch_to_signup)

        # Add widgets to layout
        layout.addWidget(self.login_username_label)
        layout.addWidget(self.login_username_input)
        layout.addWidget(self.login_password_label)
        layout.addWidget(self.login_password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.switch_to_signup_button)

        return view

    def create_message_view(self):
        """Create the message sending view."""
        view = QWidget(self)
        layout = QVBoxLayout(view)

        # Create widgets for sending messages

        # Connect the send button
        self.send_button.clicked.connect(self.send_message)

        # Add widgets to layout
        layout.addWidget(self.message_label)
        layout.addWidget(self.message_input)
        layout.addWidget(self.send_button)

        return view

    def switch_to_login(self):
        """Switch to the login view."""
        self.stacked_widget.setCurrentWidget(self.login_view)

    def switch_to_signup(self):
        """Switch to the signup view."""
        self.stacked_widget.setCurrentWidget(self.signup_view)

    def handle_signup(self):
        """Handle the signup logic."""
        username = self.signup_username_input.text()
        password = self.signup_password_input.text()

        response = client_logic.register_user(username, password)
        QMessageBox.information(self, "Success", response)

        if response == "Registration successful!":
            self.switch_to_message_window()

    def switch_to_message_window(self):
        """Switch to the message window after successful signup."""
        self.stacked_widget.setCurrentWidget(self.message_view)

    def handle_login(self):
        """Handle the login logic."""
        username = self.login_username_input.text()
        password = self.login_password_input.text()

        response = client_logic.login_user(username, password)
        QMessageBox.information(self, "Success", response)

        if response == "Login successful!":
            self.switch_to_message_window()

    def send_message(self):
        """Handle message sending."""
        message = self.message_input.text()
        response = client_logic.send_message_to_server(message)
        QMessageBox.information(self, "Server Response", response)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AuthWindow()  # Start with the authentication window (signup by default)
    window.show()
    sys.exit(app.exec_())
