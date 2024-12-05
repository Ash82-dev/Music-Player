from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt


def signup_view():
    """Create and return the signup view."""
    view = QWidget()
    layout = QVBoxLayout(view)
    layout.setSpacing(20)
    layout.setContentsMargins(40, 30, 40, 30)

    # Header Section
    header_label = QLabel("Create an Account", view)
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

    signup_button = QPushButton("Sign Up", view)
    signup_button.setFixedHeight(50)

    switch_to_login_button = QPushButton("Switch to Login", view)
    switch_to_login_button.setFixedHeight(50)

    # Add elements to their respective layouts
    form_layout.addWidget(username_label)
    form_layout.addWidget(username_input)
    form_layout.addWidget(password_label)
    form_layout.addWidget(password_input)

    button_layout.addWidget(signup_button)
    button_layout.addWidget(switch_to_login_button)

    # Center the form and buttons
    layout.addWidget(header_label)
    layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
    layout.addLayout(form_layout)
    layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum))
    layout.addLayout(button_layout)
    layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    # Set object names for further styling or testing
    username_input.setObjectName("signup_username_input")
    password_input.setObjectName("signup_password_input")
    signup_button.setObjectName("Sign Up")
    switch_to_login_button.setObjectName("Switch to Login")

    return view
