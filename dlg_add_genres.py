# -*- coding: utf-8 -*-
""" Dialog add genres """
from sqlite3 import DatabaseError
from PySide6.QtWidgets import (
    QDialog,
    QApplication,
    QMessageBox,
    QWidget,
    # QSpacerItem,
    # QSizePolicy,
    # QHBoxLayout,
    # QLabel,
    # QPushButton,
    # QListWidgetItem,
)
from PySide6.QtCore import (
    Qt,
    Signal,
    Slot,
)
# from PySide6.QtGui import QFont
from my_classes.songs import Songs
from gui import dlg_add_genres_ui


class DlgAddGenre(QDialog):
    """ Class DlgAddGenre. """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = dlg_add_genres_ui.Ui_dlg_add_genres()
        self.ui.setupUi(self)

        self.setModal(True)


