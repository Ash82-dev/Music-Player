import sys
from PyQt5.QtWidgets import QApplication
import main_window


def main():
    app = QApplication(sys.argv)

    window = main_window.Window()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
