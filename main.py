# -*- coding: utf-8 -*-
""" Main window """
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QListWidgetItem,
)
from PySide6.QtCore import (
    Qt,
    QDate,
)
import main_ui


class MainWindow(QMainWindow):
    """ Class MainWindow """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = main_ui.Ui_MainWindow()
        self.ui.setupUi(self)


def main():
    """ main function """
    import sys

    app = QApplication(sys.argv)

    window = MainWindow()
    window.showMaximized()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
