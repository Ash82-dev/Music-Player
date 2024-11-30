from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton


def login_view():
    """Create and return the login view."""
    view = QWidget()
    layout = QVBoxLayout(view)
    layout.setSpacing(20)

    # Create widgets for login
    username_label = QLabel("Username", view)
    password_label = QLabel("Password", view)

    username_input = QLineEdit(view)
    password_input = QLineEdit(view)
    password_input.setEchoMode(QLineEdit.Password)

    login_button = QPushButton("Login", view)
    switch_to_signup_button = QPushButton("Switch to Sign Up", view)

    # Add widgets to layout
    layout.addWidget(username_label)
    layout.addWidget(username_input)
    layout.addWidget(password_label)
    layout.addWidget(password_input)
    layout.addWidget(login_button)
    layout.addWidget(switch_to_signup_button)

    # Set object names for easy reference
    username_input.setObjectName("login_username_input")
    password_input.setObjectName("login_password_input")
    login_button.setObjectName("Login")
    switch_to_signup_button.setObjectName("Switch to Sign Up")

    return view
