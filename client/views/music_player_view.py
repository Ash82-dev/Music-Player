from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QScrollArea
from PyQt5.QtCore import Qt


def music_player_view():
    """Create and return the music player view."""
    view = QWidget()

    # Main layout
    layout = QVBoxLayout(view)
    layout.setSpacing(10)
    layout.setContentsMargins(10, 10, 10, 10)

    # Scroll area for dynamic music containers
    scroll_area = QScrollArea(view)
    scroll_area.setWidgetResizable(True)
    scroll_area.setStyleSheet("border: none;")

    # Scrollable widget inside the scroll area
    scroll_widget = QWidget(scroll_area)
    scroll_layout = QVBoxLayout(scroll_widget)
    scroll_layout.setSpacing(15)

    scroll_area.setWidget(scroll_widget)
    scroll_widget.setObjectName("MusicContainerArea")

    # Add the scroll area to the main layout
    layout.addWidget(scroll_area)

    # "+" Button in the bottom-right corner
    add_music_button = QPushButton("+", view)
    add_music_button.setObjectName("AddMusicButton")
    add_music_button.setStyleSheet(
        """
        QPushButton {
            background-color: #0078d4;
            color: white;
            font-size: 18px;
            border-radius: 25px;
            width: 50px;
            height: 50px;
        }
        QPushButton:hover {
            background-color: #005a9e;
        }
        """
    )
    layout.addWidget(add_music_button, alignment=Qt.AlignBottom | Qt.AlignRight)

    return view
