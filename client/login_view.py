from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

def login_view(window):
    """Create the login view."""
    view = QWidget(window)
    layout = QVBoxLayout(view)

    # Create widgets for login
    login_password_input = QLineEdit(view)
    login_password_input.setEchoMode(QLineEdit.Password)
    login_username_input = QLineEdit(view)

    login_password_label = QLabel("Password", view)
    login_username_label = QLabel("Username", view)

    login_button = QPushButton("Login", view)
    switch_to_signup_button = QPushButton("Switch to Sign Up", view)

    # Add widgets to layout
    layout.addWidget(login_username_label)
    layout.addWidget(login_username_input)
    layout.addWidget(login_password_label)
    layout.addWidget(login_password_input)
    layout.addWidget(login_button)
    layout.addWidget(switch_to_signup_button)

    # Assign the widget objects so that other files can interact with them
    login_button.setObjectName("Login")
    switch_to_signup_button.setObjectName("Switch to Sign Up")
    login_username_input.setObjectName("login_username_input")
    login_password_input.setObjectName("login_password_input")

    return view
