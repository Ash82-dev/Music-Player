from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QSpacerItem, QSizePolicy, QHBoxLayout
from PyQt5.QtCore import Qt


def login_view():
    """Create and return the login view."""
    view = QWidget()
    layout = QVBoxLayout(view)
    layout.setSpacing(20)
    layout.setContentsMargins(40, 30, 40, 30)

    # Header Section
    header_label = QLabel("Welcome Back!", view)
    header_label.setAlignment(Qt.AlignCenter)
    header_label.setStyleSheet("font-size: 24px; font-weight: bold;")

    # Form Section
    form_layout = QVBoxLayout()
    form_layout.setSpacing(15)

    username_label = QLabel("Username", view)
    username_input = QLineEdit(view)
    username_input.setFixedHeight(40)

    password_label = QLabel("Password", view)
    password_input = QLineEdit(view)
    password_input.setEchoMode(QLineEdit.Password)
    password_input.setFixedHeight(40)

    # Buttons Section
    button_layout = QVBoxLayout()
    button_layout.setSpacing(15)

    login_button = QPushButton("Login", view)
    login_button.setFixedHeight(50)

    switch_to_signup_button = QPushButton("Switch to Sign Up", view)
    switch_to_signup_button.setFixedHeight(50)

    # Add elements to their respective layouts
    form_layout.addWidget(username_label)
    form_layout.addWidget(username_input)
    form_layout.addWidget(password_label)
    form_layout.addWidget(password_input)

    button_layout.addWidget(login_button)
    button_layout.addWidget(switch_to_signup_button)

    # Center the form and buttons
    layout.addWidget(header_label)
    layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
    layout.addLayout(form_layout)
    layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum))
    layout.addLayout(button_layout)
    layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    # Set object names for further styling or testing
    username_input.setObjectName("login_username_input")
    password_input.setObjectName("login_password_input")
    login_button.setObjectName("Login")
    switch_to_signup_button.setObjectName("Switch to Sign Up")

    return view
