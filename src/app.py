import sys

from PySide6.QtWidgets import QApplication

from src.MainWindow import MainWindow


def main():

    app = QApplication([])

    mainWindow: MainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()


