from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QScrollArea, QHBoxLayout
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

    # Create a horizontal layout for the buttons
    button_layout = QHBoxLayout()
    button_layout.setSpacing(20)
    button_layout.setContentsMargins(20, 20, 20, 20)

    # Sort button
    sort_button = QPushButton("Sort", view)
    sort_button.setObjectName("SortButton")
    sort_button.setStyleSheet(
        """
        QPushButton {
            background-color: #3498db;
            color: white;
            font-size: 18px;
            font-weight: bold;
            border-radius: 25px;
            padding: 10px 20px;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
        }
        QPushButton:hover {
            background-color: #2980b9;
        }
        QPushButton:pressed {
            background-color: #1c5985;
            box-shadow: inset 2px 2px 5px rgba(0, 0, 0, 0.3);
        }
        """
    )

    # Add Music button
    add_music_button = QPushButton("+", view)
    add_music_button.setObjectName("AddMusicButton")
    add_music_button.setStyleSheet(
        """
        QPushButton {
            background-color: #3498db;
            color: white;
            font-size: 20px;
            font-weight: bold;
            width: 50px;
            height: 50px;
            border-radius: 25px;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
        }
        QPushButton:hover {
            background-color: #2980b9;
        }
        QPushButton:pressed {
            background-color: #1c5985;
            box-shadow: inset 2px 2px 5px rgba(0, 0, 0, 0.3);
        }
        """
    )

    # Add buttons to layout
    button_layout.addWidget(sort_button, alignment=Qt.AlignLeft | Qt.AlignBottom)
    button_layout.addStretch()
    button_layout.addWidget(add_music_button, alignment=Qt.AlignRight | Qt.AlignBottom)

    # Add the layout to the parent layout
    layout.addLayout(button_layout)

    return view
