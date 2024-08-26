import unittest

from PySide6.QtWidgets import QVBoxLayout, QLineEdit, QPushButton

from src.LoginWidget import LoginWidget


class TestLoginWidget(unittest.TestCase):


    def testConstructor(self):
        loginWidget = LoginWidget()


        self.assertEquals(4, loginWidget.children())
        self.assertIsInstance(QVBoxLayout, loginWidget.children()[0])
        self.assertIsInstance(QLineEdit, loginWidget.children()[1])
        self.assertIsInstance(QLineEdit, loginWidget.children()[2])
        self.assertIsInstance(QPushButton, loginWidget.children()[3])
