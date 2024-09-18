# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_add_songs_ui.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QCheckBox,
    QComboBox, QDateEdit, QDateTimeEdit, QDialog,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QTextEdit, QVBoxLayout, QWidget)

class Ui_dlg_add_songs(object):
    def setupUi(self, dlg_add_songs):
        if not dlg_add_songs.objectName():
            dlg_add_songs.setObjectName(u"dlg_add_songs")
        dlg_add_songs.resize(843, 632)
        font = QFont()
        font.setFamilies([u"Lucida Console"])
        font.setPointSize(12)
        font.setBold(False)
        dlg_add_songs.setFont(font)
        self.horizontalLayout_3 = QHBoxLayout(dlg_add_songs)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.splitter_2 = QSplitter(dlg_add_songs)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Horizontal)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.vl_song = QVBoxLayout(self.layoutWidget)
        self.vl_song.setObjectName(u"vl_song")
        self.vl_song.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vl_song.addItem(self.verticalSpacer_7)

        self.lbl_song = QLabel(self.layoutWidget)
        self.lbl_song.setObjectName(u"lbl_song")
        self.lbl_song.setFont(font)

        self.vl_song.addWidget(self.lbl_song)

        self.le_song = QLineEdit(self.layoutWidget)
        self.le_song.setObjectName(u"le_song")
        self.le_song.setFont(font)
        self.le_song.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.vl_song.addWidget(self.le_song)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.vl_genres = QVBoxLayout(self.layoutWidget1)
        self.vl_genres.setObjectName(u"vl_genres")
        self.vl_genres.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vl_genres.addItem(self.verticalSpacer_6)

        self.lbl_genres = QLabel(self.layoutWidget1)
        self.lbl_genres.setObjectName(u"lbl_genres")
        self.lbl_genres.setFont(font)
        self.lbl_genres.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.vl_genres.addWidget(self.lbl_genres)

        self.lw_genres = QListWidget(self.layoutWidget1)
        self.lw_genres.setObjectName(u"lw_genres")
        font1 = QFont()
        font1.setFamilies([u"Lucida Console"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.lw_genres.setFont(font1)
        self.lw_genres.viewport().setProperty("cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.lw_genres.setStyleSheet(u"")
        self.lw_genres.setAlternatingRowColors(True)
        self.lw_genres.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.lw_genres.setSelectionRectVisible(True)

        self.vl_genres.addWidget(self.lw_genres)

        self.splitter.addWidget(self.layoutWidget1)
        self.layoutWidget2 = QWidget(self.splitter)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_category = QLabel(self.layoutWidget2)
        self.lbl_category.setObjectName(u"lbl_category")

        self.horizontalLayout.addWidget(self.lbl_category)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cb_categories = QComboBox(self.layoutWidget2)
        self.cb_categories.setObjectName(u"cb_categories")

        self.horizontalLayout_2.addWidget(self.cb_categories)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.splitter.addWidget(self.layoutWidget2)
        self.layoutWidget3 = QWidget(self.splitter)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.hl_song_image = QHBoxLayout(self.layoutWidget3)
        self.hl_song_image.setObjectName(u"hl_song_image")
        self.hl_song_image.setContentsMargins(0, 0, 0, 0)
        self.btn_choose_image_file = QPushButton(self.layoutWidget3)
        self.btn_choose_image_file.setObjectName(u"btn_choose_image_file")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_choose_image_file.sizePolicy().hasHeightForWidth())
        self.btn_choose_image_file.setSizePolicy(sizePolicy)

        self.hl_song_image.addWidget(self.btn_choose_image_file)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl_song_image.addItem(self.horizontalSpacer_4)

        self.lbl_song_image = QLabel(self.layoutWidget3)
        self.lbl_song_image.setObjectName(u"lbl_song_image")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_song_image.sizePolicy().hasHeightForWidth())
        self.lbl_song_image.setSizePolicy(sizePolicy1)
        self.lbl_song_image.setScaledContents(True)
        self.lbl_song_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.hl_song_image.addWidget(self.lbl_song_image)

        self.splitter.addWidget(self.layoutWidget3)
        self.layoutWidget_2 = QWidget(self.splitter)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.vl_song_text = QVBoxLayout(self.layoutWidget_2)
        self.vl_song_text.setObjectName(u"vl_song_text")
        self.vl_song_text.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vl_song_text.addItem(self.verticalSpacer_4)

        self.lbl_song_text = QLabel(self.layoutWidget_2)
        self.lbl_song_text.setObjectName(u"lbl_song_text")

        self.vl_song_text.addWidget(self.lbl_song_text)

        self.te_song_text = QTextEdit(self.layoutWidget_2)
        self.te_song_text.setObjectName(u"te_song_text")

        self.vl_song_text.addWidget(self.te_song_text)

        self.splitter.addWidget(self.layoutWidget_2)
        self.layoutWidget4 = QWidget(self.splitter)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.hl_recently = QHBoxLayout(self.layoutWidget4)
        self.hl_recently.setObjectName(u"hl_recently")
        self.hl_recently.setContentsMargins(0, 0, 0, 0)
        self.chb_last_performed = QCheckBox(self.layoutWidget4)
        self.chb_last_performed.setObjectName(u"chb_last_performed")
        self.chb_last_performed.setEnabled(True)
        sizePolicy.setHeightForWidth(self.chb_last_performed.sizePolicy().hasHeightForWidth())
        self.chb_last_performed.setSizePolicy(sizePolicy)
        self.chb_last_performed.setBaseSize(QSize(0, 0))
        self.chb_last_performed.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.chb_last_performed.setChecked(False)

        self.hl_recently.addWidget(self.chb_last_performed)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl_recently.addItem(self.horizontalSpacer)

        self.splitter.addWidget(self.layoutWidget4)
        self.layoutWidget5 = QWidget(self.splitter)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.hl_date = QHBoxLayout(self.layoutWidget5)
        self.hl_date.setObjectName(u"hl_date")
        self.hl_date.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.lbl_performed_date = QLabel(self.layoutWidget5)
        self.lbl_performed_date.setObjectName(u"lbl_performed_date")

        self.verticalLayout_3.addWidget(self.lbl_performed_date)

        self.de_last_performed = QDateEdit(self.layoutWidget5)
        self.de_last_performed.setObjectName(u"de_last_performed")
        self.de_last_performed.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.de_last_performed.setReadOnly(False)
        self.de_last_performed.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.de_last_performed.setProperty("showGroupSeparator", False)
        self.de_last_performed.setDateTime(QDateTime(QDate(1999, 12, 31), QTime(0, 0, 0)))
        self.de_last_performed.setCurrentSection(QDateTimeEdit.Section.DaySection)
        self.de_last_performed.setCalendarPopup(True)

        self.verticalLayout_3.addWidget(self.de_last_performed)


        self.hl_date.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl_date.addItem(self.horizontalSpacer_3)

        self.splitter.addWidget(self.layoutWidget5)
        self.layoutWidget6 = QWidget(self.splitter)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.vl_comment = QVBoxLayout(self.layoutWidget6)
        self.vl_comment.setObjectName(u"vl_comment")
        self.vl_comment.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vl_comment.addItem(self.verticalSpacer_8)

        self.lbl_comment = QLabel(self.layoutWidget6)
        self.lbl_comment.setObjectName(u"lbl_comment")

        self.vl_comment.addWidget(self.lbl_comment)

        self.te_comment = QTextEdit(self.layoutWidget6)
        self.te_comment.setObjectName(u"te_comment")

        self.vl_comment.addWidget(self.te_comment)

        self.splitter.addWidget(self.layoutWidget6)
        self.splitter_2.addWidget(self.splitter)
        self.layoutWidget7 = QWidget(self.splitter_2)
        self.layoutWidget7.setObjectName(u"layoutWidget7")
        self.vl_buttons = QVBoxLayout(self.layoutWidget7)
        self.vl_buttons.setObjectName(u"vl_buttons")
        self.vl_buttons.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 24, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.vl_buttons.addItem(self.verticalSpacer_2)

        self.btn_add_song = QPushButton(self.layoutWidget7)
        self.btn_add_song.setObjectName(u"btn_add_song")
        self.btn_add_song.setFont(font)
        self.btn_add_song.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_add_song.setIconSize(QSize(32, 32))

        self.vl_buttons.addWidget(self.btn_add_song)

        self.btn_cancel = QPushButton(self.layoutWidget7)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setFont(font)
        self.btn_cancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cancel.setIconSize(QSize(32, 32))

        self.vl_buttons.addWidget(self.btn_cancel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vl_buttons.addItem(self.verticalSpacer)

        self.splitter_2.addWidget(self.layoutWidget7)

        self.horizontalLayout_3.addWidget(self.splitter_2)

        QWidget.setTabOrder(self.le_song, self.btn_add_song)
        QWidget.setTabOrder(self.btn_add_song, self.btn_cancel)
        QWidget.setTabOrder(self.btn_cancel, self.lw_genres)

        self.retranslateUi(dlg_add_songs)

        QMetaObject.connectSlotsByName(dlg_add_songs)
    # setupUi

    def retranslateUi(self, dlg_add_songs):
        dlg_add_songs.setWindowTitle(QCoreApplication.translate("dlg_add_songs", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u0435\u0441\u043d\u0438", None))
        self.lbl_song.setText(QCoreApplication.translate("dlg_add_songs", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0435\u0441\u043d\u0438: ", None))
        self.le_song.setPlaceholderText(QCoreApplication.translate("dlg_add_songs", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0435\u0441\u043d\u0438", None))
        self.lbl_genres.setText(QCoreApplication.translate("dlg_add_songs", u"\u0416\u0430\u043d\u0440\u044b:", None))
        self.lbl_category.setText(QCoreApplication.translate("dlg_add_songs", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:", None))
        self.btn_choose_image_file.setText(QCoreApplication.translate("dlg_add_songs", u"...", None))
        self.lbl_song_image.setText(QCoreApplication.translate("dlg_add_songs", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c\n"
"\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.lbl_song_text.setText(QCoreApplication.translate("dlg_add_songs", u"\u0422\u0435\u043a\u0441\u0442 \u043f\u0435\u0441\u043d\u0438:", None))
        self.te_song_text.setPlaceholderText(QCoreApplication.translate("dlg_add_songs", u"\u0422\u0435\u043a\u0441\u0442 \u043f\u0435\u0441\u043d\u0438", None))
        self.chb_last_performed.setText(QCoreApplication.translate("dlg_add_songs", u"\u041d\u0435\u0434\u0430\u0432\u043d\u043e \u0438\u0441\u043f\u043e\u043b\u043d\u044f\u043b\u0430\u0441\u044c", None))
        self.lbl_performed_date.setText(QCoreApplication.translate("dlg_add_songs", u"\u0414\u0430\u0442\u0430 \u0438\u0441\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f:", None))
        self.de_last_performed.setDisplayFormat(QCoreApplication.translate("dlg_add_songs", u"dd MMMM yyyy", None))
        self.lbl_comment.setText(QCoreApplication.translate("dlg_add_songs", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439:", None))
        self.te_comment.setPlaceholderText(QCoreApplication.translate("dlg_add_songs", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", None))
        self.btn_add_song.setText(QCoreApplication.translate("dlg_add_songs", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c\n"
"\u043f\u0435\u0441\u043d\u044e", None))
        self.btn_cancel.setText(QCoreApplication.translate("dlg_add_songs", u" \u041e\u0442\u043c\u0435\u043d\u0430\n"
" (\u0412\u044b\u0445\u043e\u0434)", None))
    # retranslateUi

