import sys
from PyQt5.QtWidgets import QApplication
import gui


def main():
    # Initialize the application
    app = QApplication(sys.argv)

    # Start the authentication window (signup by default)
    window = gui.AuthWindow()  # This will start the AuthWindow
    window.show()  # Display the authentication window

    # Start the application's event loop
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
