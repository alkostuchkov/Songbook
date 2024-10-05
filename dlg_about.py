# -*- coding: utf-8 -*-
""" Dialog about """

# Copyright (C) 2024, Alexander Kostuchkov

import os
import sys
import webbrowser
from PySide6.QtWidgets import (
    QDialog,
    QWidget,
)
from PySide6.QtCore import (
    QEvent,
    Qt,
)
from gui import dlg_about_ui


class DlgAbout(QDialog):
    """ Dialog about program, author and thanks """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = dlg_about_ui.Ui_dlg_about()
        self.ui.setupUi(self)

        self.install_my_event_filters()
        self.ui.btn_close.clicked.connect(self.close)

    def show_licence(self) -> None:
        """ Show licence in default text editor. """
        path_to_licence_file = os.path.dirname(
            os.path.abspath(sys.argv[0])) + os.sep + "COPYING"
        if os.path.exists(path_to_licence_file):
            webbrowser.open(path_to_licence_file)

    def install_my_event_filters(self) -> None:
        """ Install my event filters. """
        self.ui.lbl_licence.installEventFilter(self)
        self.ui.lbl_licence_pic.installEventFilter(self)

    def eventFilter(self, obj, e) -> bool:
        """ Event filter. """
        # if obj == self.ui.lbl_licence or obj == self.ui.lbl_licence_pic:
        if obj in (self.ui.lbl_licence, self.ui.lbl_licence_pic):
            if e.type() == QEvent.MouseButtonPress:
                if e.buttons() & Qt.LeftButton:
                    self.show_licence()
                    return True
        return QWidget.eventFilter(self, obj, e)
