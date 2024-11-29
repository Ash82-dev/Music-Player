from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton


def signup_view(window):
    """Create the signup view."""
    view = QWidget(window)
    layout = QVBoxLayout(view)

    # Create widgets for signup
    signup_password_input = QLineEdit(view)
    signup_password_input.setEchoMode(QLineEdit.Password)
    signup_username_input = QLineEdit(view)

    signup_password_label = QLabel("Password", view)
    signup_username_label = QLabel("Username", view)

    signup_button = QPushButton("Sign Up", view)
    switch_to_login_button = QPushButton("Switch to Login", view)

    # Add widgets to layout
    layout.addWidget(signup_username_label)
    layout.addWidget(signup_username_input)
    layout.addWidget(signup_password_label)
    layout.addWidget(signup_password_input)
    layout.addWidget(signup_button)
    layout.addWidget(switch_to_login_button)

    # Assign the widget objects so that other files can interact with them
    signup_button.setObjectName("Sign Up")
    switch_to_login_button.setObjectName("Switch to Login")
    signup_username_input.setObjectName("signup_username_input")
    signup_password_input.setObjectName("signup_password_input")

    return view
