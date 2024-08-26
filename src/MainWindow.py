from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFrame

from src.LoginWidget import LoginWidget


class MainWindow(QWidget):


    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        # label: QLabel = QLabel("MyPlan")
        # self.layout.addWidget(label)

        self.layout.addWidget(LoginWidget())

        self.setLayout(self.layout)
        self.resize(1200,900)
        self.setWindowTitle("My Plan")
