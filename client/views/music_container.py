from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt


class MusicContainer(QFrame):
    def __init__(self, name, duration):
        super().__init__()
        self.setFrameShape(QFrame.StyledPanel)
        self.setStyleSheet("""
            border: 1px solid #aaa; 
            padding: 10px; 
            border-radius: 5px;
        """)

        # Layout for music container
        layout = QHBoxLayout(self)
        layout.setSpacing(10)

        # Song details layout
        details_layout = QVBoxLayout()
        self.name_label = QLabel(name, self)
        self.duration_label = QLabel(duration, self)

        details_layout.addWidget(self.name_label)
        details_layout.addWidget(self.duration_label)

        # Control buttons layout (Play, Forward, Backward)
        controls_layout = QHBoxLayout()

        # Play button (▶ or ⏸)
        self.play_button = QPushButton("▶", self)
        self.play_button.setObjectName("PlayButton")

        # Forward button (>>)
        self.forward_button = QPushButton(">>", self)
        self.forward_button.setObjectName("ForwardButton")

        # Backward button (<<)
        self.backward_button = QPushButton("<<", self)
        self.backward_button.setObjectName("BackwardButton")

        # Add buttons to the controls layout
        controls_layout.addWidget(self.backward_button)
        controls_layout.addWidget(self.play_button)
        controls_layout.addWidget(self.forward_button)

        # Add details and control layouts to the main layout
        layout.addLayout(details_layout)
        layout.addLayout(controls_layout)
