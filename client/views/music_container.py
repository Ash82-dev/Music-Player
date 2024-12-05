from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtGui import QFont


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
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(10)

        # Song details layout
        details_layout = QVBoxLayout()
        self.name_label = QLabel(name, self)
        self.duration_label = QLabel(duration, self)

        details_layout.addWidget(self.name_label)
        details_layout.addWidget(self.duration_label)

        # Add song details to main layout
        main_layout.addLayout(details_layout)

        # Control buttons layout (Play, Forward, Backward, Remove)
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

        # Remove button (🚮)
        self.remove_button = QPushButton("🚮", self)
        self.remove_button.setObjectName("RemoveButton")
        self.remove_button.setToolTip("Remove this song")

        # Add buttons to the controls layout
        controls_layout.addWidget(self.backward_button)
        controls_layout.addWidget(self.play_button)
        controls_layout.addWidget(self.forward_button)
        controls_layout.addWidget(self.remove_button)

        # Add controls to the main layout
        main_layout.addLayout(controls_layout)

        # Rating layout (Stars)
        rating_layout = QHBoxLayout()
        self.rating_stars = []
        for i in range(1, 6):
            star_button = QPushButton("★", self)
            star_button.setFont(QFont("Arial", 14))
            star_button.setStyleSheet("color: #aaa; border: none;")
            star_button.setCheckable(True)
            star_button.clicked.connect(lambda _, idx=i: self.update_rating(idx))
            self.rating_stars.append(star_button)
            rating_layout.addWidget(star_button)

        # Add rating layout to the main layout
        main_layout.addLayout(rating_layout)

        # Initialize selected rating
        self.current_rating = None

    def update_rating(self, rating):
        # Update the rating and visually highlight stars
        self.current_rating = rating
        for idx, star in enumerate(self.rating_stars):
            if idx < rating:
                star.setStyleSheet("color: #ffcc00; border: none;")
            else:
                star.setStyleSheet("color: #aaa; border: none;")

    def get_rating(self):
        return self.current_rating
