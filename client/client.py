import sys
import threading
from PyQt5.QtWidgets import QApplication
from server.socket_manager import initialize_socket, listen_to_server
import main_window


def main():
    # Initialize the application
    app = QApplication(sys.argv)

    # Create the main window
    window = main_window.Window()
    window.show()

    # Initialize socket connection
    initialize_socket()

    # Start a thread to listen to server messages
    listen_thread = threading.Thread(target=listen_to_server, daemon=True)
    listen_thread.start()

    # Execute the application
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
