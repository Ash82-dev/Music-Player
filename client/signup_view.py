from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton

def signup_view():
    """Create and return the signup view."""
    view = QWidget()
    layout = QVBoxLayout(view)

    # Create widgets for signup
    username_label = QLabel("Username", view)
    password_label = QLabel("Password", view)

    username_input = QLineEdit(view)
    password_input = QLineEdit(view)
    password_input.setEchoMode(QLineEdit.Password)

    signup_button = QPushButton("Sign Up", view)
    switch_to_login_button = QPushButton("Switch to Login", view)

    # Add widgets to layout
    layout.addWidget(username_label)
    layout.addWidget(username_input)
    layout.addWidget(password_label)
    layout.addWidget(password_input)
    layout.addWidget(signup_button)
    layout.addWidget(switch_to_login_button)

    # Set object names for easy reference
    username_input.setObjectName("signup_username_input")
    password_input.setObjectName("signup_password_input")
    signup_button.setObjectName("Sign Up")
    switch_to_login_button.setObjectName("Switch to Login")

    return view
