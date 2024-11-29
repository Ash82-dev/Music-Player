from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton

def message_view():
    """Create and return the message sending view."""
    view = QWidget()
    layout = QVBoxLayout(view)

    # Create widgets for sending messages
    message_label = QLabel("Enter your message", view)
    message_input = QLineEdit(view)
    send_button = QPushButton("Send", view)

    # Add widgets to layout
    layout.addWidget(message_label)
    layout.addWidget(message_input)
    layout.addWidget(send_button)

    # Set object names for easy reference
    message_input.setObjectName("message_input")
    send_button.setObjectName("Send")

    return view
