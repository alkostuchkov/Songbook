# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_add_categories_ui.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QVBoxLayout, QWidget)

class Ui_dlg_add_categories(object):
    def setupUi(self, dlg_add_categories):
        if not dlg_add_categories.objectName():
            dlg_add_categories.setObjectName(u"dlg_add_categories")
        dlg_add_categories.resize(562, 328)
        font = QFont()
        font.setFamilies([u"Lucida Console"])
        font.setPointSize(12)
        font.setBold(False)
        dlg_add_categories.setFont(font)
        dlg_add_categories.setModal(True)
        self.verticalLayout_3 = QVBoxLayout(dlg_add_categories)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_category = QLabel(dlg_add_categories)
        self.lbl_category.setObjectName(u"lbl_category")
        self.lbl_category.setFont(font)

        self.horizontalLayout.addWidget(self.lbl_category)

        self.le_category = QLineEdit(dlg_add_categories)
        self.le_category.setObjectName(u"le_category")
        self.le_category.setFont(font)
        self.le_category.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.le_category)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.splitter = QSplitter(dlg_add_categories)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setFont(font)
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbl_adding_categiries = QLabel(self.layoutWidget)
        self.lbl_adding_categiries.setObjectName(u"lbl_adding_categiries")
        self.lbl_adding_categiries.setFont(font)
        self.lbl_adding_categiries.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_2.addWidget(self.lbl_adding_categiries)

        self.lw_adding_categiries = QListWidget(self.layoutWidget)
        self.lw_adding_categiries.setObjectName(u"lw_adding_categiries")
        font1 = QFont()
        font1.setFamilies([u"Lucida Console"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.lw_adding_categiries.setFont(font1)
        self.lw_adding_categiries.viewport().setProperty("cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.lw_adding_categiries.setStyleSheet(u"")
        self.lw_adding_categiries.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)

        self.verticalLayout_2.addWidget(self.lw_adding_categiries)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setFont(font)
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 24, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.btn_add_category_to_list = QPushButton(self.layoutWidget1)
        self.btn_add_category_to_list.setObjectName(u"btn_add_category_to_list")
        self.btn_add_category_to_list.setFont(font)
        self.btn_add_category_to_list.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_add_category_to_list.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btn_add_category_to_list)

        self.btn_del_category_from_list = QPushButton(self.layoutWidget1)
        self.btn_del_category_from_list.setObjectName(u"btn_del_category_from_list")
        self.btn_del_category_from_list.setFont(font)
        self.btn_del_category_from_list.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_del_category_from_list.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btn_del_category_from_list)

        self.btn_finish_and_save = QPushButton(self.layoutWidget1)
        self.btn_finish_and_save.setObjectName(u"btn_finish_and_save")
        self.btn_finish_and_save.setFont(font)
        self.btn_finish_and_save.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_finish_and_save.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btn_finish_and_save)

        self.btn_cancel = QPushButton(self.layoutWidget1)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setFont(font)
        self.btn_cancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cancel.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.btn_cancel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.splitter.addWidget(self.layoutWidget1)

        self.verticalLayout_3.addWidget(self.splitter)

        QWidget.setTabOrder(self.le_category, self.btn_add_category_to_list)
        QWidget.setTabOrder(self.btn_add_category_to_list, self.btn_del_category_from_list)
        QWidget.setTabOrder(self.btn_del_category_from_list, self.btn_finish_and_save)
        QWidget.setTabOrder(self.btn_finish_and_save, self.btn_cancel)
        QWidget.setTabOrder(self.btn_cancel, self.lw_adding_categiries)

        self.retranslateUi(dlg_add_categories)

        QMetaObject.connectSlotsByName(dlg_add_categories)
    # setupUi

    def retranslateUi(self, dlg_add_categories):
        dlg_add_categories.setWindowTitle(QCoreApplication.translate("dlg_add_categories", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
        self.lbl_category.setText(QCoreApplication.translate("dlg_add_categories", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f: ", None))
        self.lbl_adding_categiries.setText(QCoreApplication.translate("dlg_add_categories", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0434\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u043c\u044b\u0445 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439:", None))
        self.btn_add_category_to_list.setText(QCoreApplication.translate("dlg_add_categories", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c\n"
"\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
        self.btn_del_category_from_list.setText(QCoreApplication.translate("dlg_add_categories", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c\n"
"\u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
        self.btn_finish_and_save.setText(QCoreApplication.translate("dlg_add_categories", u"  \u0417\u0430\u043a\u043e\u043d\u0447\u0438\u0442\u044c\n"
" \u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.btn_cancel.setText(QCoreApplication.translate("dlg_add_categories", u" \u041e\u0442\u043c\u0435\u043d\u0430\n"
" (\u0412\u044b\u0445\u043e\u0434)", None))
    # retranslateUi

