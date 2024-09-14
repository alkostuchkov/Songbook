# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_edit_genres_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_dlg_edit_genres(object):
    def setupUi(self, dlg_edit_genres):
        if not dlg_edit_genres.objectName():
            dlg_edit_genres.setObjectName(u"dlg_edit_genres")
        dlg_edit_genres.resize(562, 193)
        font = QFont()
        font.setFamilies([u"Lucida Console"])
        font.setPointSize(12)
        font.setBold(False)
        dlg_edit_genres.setFont(font)
        dlg_edit_genres.setModal(False)
        self.verticalLayout_3 = QVBoxLayout(dlg_edit_genres)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_genre = QLabel(dlg_edit_genres)
        self.lbl_genre.setObjectName(u"lbl_genre")
        self.lbl_genre.setFont(font)

        self.horizontalLayout.addWidget(self.lbl_genre)

        self.le_genre = QLineEdit(dlg_edit_genres)
        self.le_genre.setObjectName(u"le_genre")
        self.le_genre.setFont(font)
        self.le_genre.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.le_genre)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 24, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.btn_finish_and_save = QPushButton(dlg_edit_genres)
        self.btn_finish_and_save.setObjectName(u"btn_finish_and_save")
        self.btn_finish_and_save.setFont(font)
        self.btn_finish_and_save.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_finish_and_save.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btn_finish_and_save)

        self.btn_cancel = QPushButton(dlg_edit_genres)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setFont(font)
        self.btn_cancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cancel.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btn_cancel)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        QWidget.setTabOrder(self.le_genre, self.btn_finish_and_save)
        QWidget.setTabOrder(self.btn_finish_and_save, self.btn_cancel)

        self.retranslateUi(dlg_edit_genres)

        QMetaObject.connectSlotsByName(dlg_edit_genres)
    # setupUi

    def retranslateUi(self, dlg_edit_genres):
        dlg_edit_genres.setWindowTitle(QCoreApplication.translate("dlg_edit_genres", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0436\u0430\u043d\u0440\u0430", None))
        self.lbl_genre.setText(QCoreApplication.translate("dlg_edit_genres", u"\u0416\u0430\u043d\u0440: ", None))
        self.btn_finish_and_save.setText(QCoreApplication.translate("dlg_edit_genres", u"  \u0417\u0430\u043a\u043e\u043d\u0447\u0438\u0442\u044c\n"
" \u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.btn_cancel.setText(QCoreApplication.translate("dlg_edit_genres", u" \u041e\u0442\u043c\u0435\u043d\u0430\n"
" (\u0412\u044b\u0445\u043e\u0434)", None))
    # retranslateUi

