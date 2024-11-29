from PyQt5.QtWidgets import QVBoxLayout, QStackedWidget, QPushButton
from signup_view import signup_view
from login_view import login_view
from message_view import message_view


def auth_view(window):
    """Create the authentication UI components and layout for the window."""
    # Create the QStackedWidget to hold the views
    window.stacked_widget = QStackedWidget(window)

    # Create the views by calling the functions
    window.signup_view = signup_view(window)
    window.login_view = login_view(window)
    window.message_view = message_view(window)

    # Add views to stacked widget
    window.stacked_widget.addWidget(window.signup_view)
    window.stacked_widget.addWidget(window.login_view)
    window.stacked_widget.addWidget(window.message_view)

    # Set the initial view to the signup view
    window.stacked_widget.setCurrentWidget(window.signup_view)

    # Set the layout for the main window
    layout = QVBoxLayout(window)
    layout.addWidget(window.stacked_widget)

    # Connect buttons to actions
    window.signup_view.findChild(QPushButton, "Sign Up").clicked.connect(window.handle_signup)
    window.signup_view.findChild(QPushButton, "Switch to Login").clicked.connect(window.switch_to_login)
    window.login_view.findChild(QPushButton, "Login").clicked.connect(window.handle_login)
    window.login_view.findChild(QPushButton, "Switch to Sign Up").clicked.connect(window.switch_to_signup)
    window.message_view.findChild(QPushButton, "Send").clicked.connect(window.send_message)
