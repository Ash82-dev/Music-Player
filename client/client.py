import sys
from PyQt5.QtWidgets import QApplication
import client_gui


def main():
    # Initialize the application
    app = QApplication(sys.argv)

    # Start the login/signup window
    window = client_gui.SignupWindow()
    window.show()

    # Start the application's event loop
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
