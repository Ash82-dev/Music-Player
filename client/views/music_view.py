from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QScrollArea, QFrame
from PyQt5.QtCore import Qt


def music_container(name, duration):
    """Create a container for a single music item."""
    container = QFrame()
    container.setFrameShape(QFrame.StyledPanel)
    container.setStyleSheet("margin: 10px; padding: 20px; border: 1px solid lightgray;")

    layout = QHBoxLayout(container)

    # Music Name and Duration
    name_label = QLabel(name)
    duration_label = QLabel(duration)
    duration_label.setStyleSheet("font-size: 14px; color: gray;")

    # Add name and duration to a vertical layout
    text_layout = QVBoxLayout()
    text_layout.addWidget(name_label)
    text_layout.addWidget(duration_label)

    # Play/Pause Button
    play_button = QPushButton("▶")
    play_button.setFixedSize(50, 50)

    # Forward and Backward Buttons
    forward_button = QPushButton(">>")
    forward_button.setFixedSize(50, 50)
    backward_button = QPushButton("<<")
    backward_button.setFixedSize(50, 50)

    # Add widgets to the layout
    layout.addLayout(text_layout)  # Name and duration on the left
    layout.addWidget(backward_button)
    layout.addWidget(play_button)
    layout.addWidget(forward_button)

    # Connect play button to toggle play/pause
    def toggle_play_pause():
        play_button.setText("⏸" if play_button.text() == "▶" else "▶")
    play_button.clicked.connect(toggle_play_pause)

    return container


def music_view():
    """Create the main music player view."""
    view = QWidget()
    layout = QVBoxLayout(view)
    layout.setSpacing(20)

    # Scroll area to hold music items
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_content = QWidget()
    scroll_layout = QVBoxLayout(scroll_content)
    scroll_layout.setSpacing(20)

    scroll_area.setWidget(scroll_content)
    layout.addWidget(scroll_area)

    # Add button at the bottom to add new music
    add_button = QPushButton("+")
    add_button.setFixedSize(60, 60)
    add_button.setStyleSheet("font-size: 24px; background-color: lightblue; border-radius: 30px;")
    layout.addWidget(add_button, alignment=Qt.AlignCenter)

    # Add a few initial music items (for demonstration)
    music_items = [
        ("Song 1", "3:45"),
        ("Song 2", "4:20"),
        ("Song 3", "2:50"),
    ]
    for name, duration in music_items:
        scroll_layout.addWidget(music_container(name, duration))

    # Function to add a new music item dynamically
    def add_music():
        new_item = music_container("New Song", "0:00")
        scroll_layout.addWidget(new_item)

    add_button.clicked.connect(add_music)

    return view
