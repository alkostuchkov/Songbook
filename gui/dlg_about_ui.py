# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_about_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTextBrowser, QVBoxLayout, QWidget)
import res_rc

class Ui_dlg_about(object):
    def setupUi(self, dlg_about):
        if not dlg_about.objectName():
            dlg_about.setObjectName(u"dlg_about")
        dlg_about.resize(650, 315)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dlg_about.sizePolicy().hasHeightForWidth())
        dlg_about.setSizePolicy(sizePolicy)
        dlg_about.setMinimumSize(QSize(650, 315))
        dlg_about.setMaximumSize(QSize(650, 315))
        font = QFont()
        font.setFamilies([u"Lucida Console"])
        font.setPointSize(12)
        dlg_about.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/songbook.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        dlg_about.setWindowIcon(icon)
        self.horizontalLayout_2 = QHBoxLayout(dlg_about)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_prog_icon = QLabel(dlg_about)
        self.lbl_prog_icon.setObjectName(u"lbl_prog_icon")
        self.lbl_prog_icon.setFrameShape(QFrame.Shape.NoFrame)
        self.lbl_prog_icon.setPixmap(QPixmap(u":/icons/songbook.ico"))

        self.verticalLayout_2.addWidget(self.lbl_prog_icon)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tw_about = QTabWidget(dlg_about)
        self.tw_about.setObjectName(u"tw_about")
        self.tw_about.setFont(font)
        self.tw_about.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.tw_about.setTabPosition(QTabWidget.TabPosition.North)
        self.tab_about_program = QWidget()
        self.tab_about_program.setObjectName(u"tab_about_program")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_about_program)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tbr_about_program = QTextBrowser(self.tab_about_program)
        self.tbr_about_program.setObjectName(u"tbr_about_program")
        self.tbr_about_program.viewport().setProperty("cursor", QCursor(Qt.CursorShape.ArrowCursor))

        self.horizontalLayout_3.addWidget(self.tbr_about_program)

        self.tw_about.addTab(self.tab_about_program, "")
        self.tab_about_author = QWidget()
        self.tab_about_author.setObjectName(u"tab_about_author")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_about_author)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tbrAboutAuthor = QTextBrowser(self.tab_about_author)
        self.tbrAboutAuthor.setObjectName(u"tbrAboutAuthor")
        self.tbrAboutAuthor.viewport().setProperty("cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.tbrAboutAuthor.setOpenExternalLinks(True)

        self.horizontalLayout_4.addWidget(self.tbrAboutAuthor)

        self.tw_about.addTab(self.tab_about_author, "")
        self.tab_thanks = QWidget()
        self.tab_thanks.setObjectName(u"tab_thanks")
        self.horizontalLayout_5 = QHBoxLayout(self.tab_thanks)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tbrThanks = QTextBrowser(self.tab_thanks)
        self.tbrThanks.setObjectName(u"tbrThanks")
        self.tbrThanks.viewport().setProperty("cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.tbrThanks.setOpenExternalLinks(True)

        self.horizontalLayout_5.addWidget(self.tbrThanks)

        self.tw_about.addTab(self.tab_thanks, "")
        self.tab_licence = QWidget()
        self.tab_licence.setObjectName(u"tab_licence")
        self.verticalLayout_4 = QVBoxLayout(self.tab_licence)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.lbl_licence = QLabel(self.tab_licence)
        self.lbl_licence.setObjectName(u"lbl_licence")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(13)
        font1.setUnderline(True)
        self.lbl_licence.setFont(font1)
        self.lbl_licence.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.lbl_licence)

        self.lbl_licence_pic = QLabel(self.tab_licence)
        self.lbl_licence_pic.setObjectName(u"lbl_licence_pic")
        self.lbl_licence_pic.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lbl_licence_pic.setPixmap(QPixmap(u":/icons/gpl_v3.png"))
        self.lbl_licence_pic.setScaledContents(True)

        self.verticalLayout.addWidget(self.lbl_licence_pic)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout_6.addLayout(self.verticalLayout)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.tw_about.addTab(self.tab_licence, "")

        self.verticalLayout_3.addWidget(self.tw_about)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_close = QPushButton(dlg_about)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setFont(font)
        self.btn_close.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/cancel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_close.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btn_close)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.retranslateUi(dlg_about)

        self.tw_about.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(dlg_about)
    # setupUi

    def retranslateUi(self, dlg_about):
        dlg_about.setWindowTitle(QCoreApplication.translate("dlg_about", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.lbl_prog_icon.setText("")
        self.tbr_about_program.setHtml(QCoreApplication.translate("dlg_about", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Lucida Console'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial'; font-size:13pt;\">\u041f\u0435\u0441\u0435\u043d\u043d\u0438\u043a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial'; font-size:13pt;\">\u0412\u0435\u0440\u0441\u0438\u044f 0.0.1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px;"
                        " margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial'; font-size:13pt;\">\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430-\u043f\u0435\u0441\u0435\u043d\u043d\u0438\u043a \u0434\u043b\u044f \u043c\u043e\u0435\u0439 \u0434\u043e\u0447\u0435\u0440\u0438 \u041e\u043b\u044c\u0433\u0438</span></p></body></html>", None))
        self.tw_about.setTabText(self.tw_about.indexOf(self.tab_about_program), QCoreApplication.translate("dlg_about", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.tbrAboutAuthor.setHtml(QCoreApplication.translate("dlg_about", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Lucida Console'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial'; font-size:13pt;\">\u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440 \u041a\u043e\u0441\u0442\u044e\u0447\u043a\u043e\u0432 &lt;</span><a href=\"mailto:alkostuchkov@gmail.com\"><span style=\" font-family:'Arial'; font-size:13pt; text-decoration: underline; color:#0000ff;\">alkostuchkov@gmail.com</span></a><span style=\" font-family:'Arial'; font-size:13pt"
                        ";\">&gt;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Arial'; font-size:13pt;\"><br /></p></body></html>", None))
        self.tw_about.setTabText(self.tw_about.indexOf(self.tab_about_author), QCoreApplication.translate("dlg_about", u"\u041e\u0431 \u0430\u0432\u0442\u043e\u0440\u0435", None))
        self.tbrThanks.setHtml(QCoreApplication.translate("dlg_about", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Lucida Console'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial'; font-size:13pt;\">\u0421\u043b\u0430\u0432\u0430 \u0413\u043e\u0441\u043f\u043e\u0434\u0443 \u0418\u0438\u0441\u0443\u0441\u0443 \u0425\u0440\u0438\u0441\u0442\u0443</span></p></body></html>", None))
        self.tw_about.setTabText(self.tw_about.indexOf(self.tab_thanks), QCoreApplication.translate("dlg_about", u"\u0411\u043b\u0430\u0433\u043e\u0434\u0430\u0440\u043d\u043e\u0441\u0442\u0438", None))
        self.lbl_licence.setText(QCoreApplication.translate("dlg_about", u"GNU GENERAL PUBLIC LICENSE", None))
        self.lbl_licence_pic.setText("")
        self.tw_about.setTabText(self.tw_about.indexOf(self.tab_licence), QCoreApplication.translate("dlg_about", u"\u041b\u0438\u0446\u0435\u043d\u0437\u0438\u044f", None))
        self.btn_close.setText(QCoreApplication.translate("dlg_about", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

