from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton


def message_view(window):
    """Create the message sending view."""
    view = QWidget(window)
    layout = QVBoxLayout(view)

    # Create widgets for sending messages
    message_label = QLabel("Enter your message", view)
    message_input = QLineEdit(view)
    send_button = QPushButton("Send", view)

    # Add widgets to layout
    layout.addWidget(message_label)
    layout.addWidget(message_input)
    layout.addWidget(send_button)

    # Assign the widget objects so that other files can interact with them
    message_input.setObjectName("message_input")
    send_button.setObjectName("Send")

    return view
