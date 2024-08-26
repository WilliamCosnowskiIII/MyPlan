import unittest

from PySide6.QtWidgets import QVBoxLayout

from src.LoginWidget import LoginWidget
from src.MainWindow import MainWindow


class TestMainWindow(unittest.TestCase):


    def testConstructor(self):
        mainWindow = MainWindow()

        self.assertEquals(2, mainWindow.children())
        self.assertIsInstance(QVBoxLayout, mainWindow.children()[0])
        self.assertIsInstance(LoginWidget, mainWindow.children()[1])
