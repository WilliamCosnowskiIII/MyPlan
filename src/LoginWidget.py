from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QTextEdit, QLineEdit, QVBoxLayout, QPushButton, QFrame


class LoginWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.layout.setSpacing(0)
        usernameLineEdit = QLineEdit()
        usernameLineEdit.setFixedHeight(25)
        usernameLineEdit.setPlaceholderText("Username")
        passwordLineEdit = QLineEdit()
        passwordLineEdit.setFixedHeight(25)
        passwordLineEdit.setPlaceholderText("Password")
        passwordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        login = QPushButton("Login")

        self.layout.addWidget(usernameLineEdit)
        self.layout.addWidget(passwordLineEdit)
        self.layout.addWidget(login)

        self.setLayout(self.layout)

        self.setFixedSize(600, 400)
        self.show()
