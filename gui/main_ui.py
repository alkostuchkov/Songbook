# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QSpacerItem, QSplitter, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(904, 612)
        icon = QIcon()
        icon.addFile(u":/icons/songbook.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.act_add_category = QAction(MainWindow)
        self.act_add_category.setObjectName(u"act_add_category")
        icon1 = QIcon()
        icon1.addFile(u":/icons/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.act_add_category.setIcon(icon1)
        font = QFont()
        font.setFamilies([u"Lucida Console"])
        font.setPointSize(12)
        self.act_add_category.setFont(font)
        self.act_add_genre = QAction(MainWindow)
        self.act_add_genre.setObjectName(u"act_add_genre")
        self.act_add_genre.setIcon(icon1)
        self.act_add_genre.setFont(font)
        self.act_add_song = QAction(MainWindow)
        self.act_add_song.setObjectName(u"act_add_song")
        self.act_add_song.setIcon(icon1)
        self.act_add_song.setFont(font)
        self.act_edit_category = QAction(MainWindow)
        self.act_edit_category.setObjectName(u"act_edit_category")
        icon2 = QIcon()
        icon2.addFile(u":/icons/edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.act_edit_category.setIcon(icon2)
        self.act_edit_category.setFont(font)
        self.act_edit_genre = QAction(MainWindow)
        self.act_edit_genre.setObjectName(u"act_edit_genre")
        self.act_edit_genre.setIcon(icon2)
        self.act_edit_genre.setFont(font)
        self.act_edit_song = QAction(MainWindow)
        self.act_edit_song.setObjectName(u"act_edit_song")
        self.act_edit_song.setIcon(icon2)
        self.act_edit_song.setFont(font)
        self.act_delete_category = QAction(MainWindow)
        self.act_delete_category.setObjectName(u"act_delete_category")
        icon3 = QIcon()
        icon3.addFile(u":/icons/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.act_delete_category.setIcon(icon3)
        self.act_delete_category.setFont(font)
        self.act_delete_genre = QAction(MainWindow)
        self.act_delete_genre.setObjectName(u"act_delete_genre")
        self.act_delete_genre.setIcon(icon3)
        self.act_delete_genre.setFont(font)
        self.act_delete_song = QAction(MainWindow)
        self.act_delete_song.setObjectName(u"act_delete_song")
        self.act_delete_song.setIcon(icon3)
        self.act_delete_song.setFont(font)
        self.act_clear_db = QAction(MainWindow)
        self.act_clear_db.setObjectName(u"act_clear_db")
        icon4 = QIcon()
        icon4.addFile(u":/icons/cancel_2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.act_clear_db.setIcon(icon4)
        self.act_clear_db.setFont(font)
        self.act_abput_program = QAction(MainWindow)
        self.act_abput_program.setObjectName(u"act_abput_program")
        self.act_abput_program.setIcon(icon)
        self.act_abput_program.setFont(font)
        self.act_about_author = QAction(MainWindow)
        self.act_about_author.setObjectName(u"act_about_author")
        icon5 = QIcon()
        icon5.addFile(u":/icons/author.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.act_about_author.setIcon(icon5)
        self.act_about_author.setFont(font)
        self.act_about_qt = QAction(MainWindow)
        self.act_about_qt.setObjectName(u"act_about_qt")
        icon6 = QIcon()
        icon6.addFile(u":/icons/qt.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.act_about_qt.setIcon(icon6)
        self.act_about_qt.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.spl_filter_sort = QSplitter(self.splitter)
        self.spl_filter_sort.setObjectName(u"spl_filter_sort")
        self.spl_filter_sort.setOrientation(Qt.Orientation.Horizontal)
        self.layoutWidget = QWidget(self.spl_filter_sort)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_categories = QLabel(self.layoutWidget)
        self.lbl_categories.setObjectName(u"lbl_categories")
        font1 = QFont()
        font1.setFamilies([u"Lucida Console"])
        font1.setPointSize(14)
        self.lbl_categories.setFont(font1)
        self.lbl_categories.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_categories)

        self.lw_categories = QListWidget(self.layoutWidget)
        self.lw_categories.setObjectName(u"lw_categories")
        self.lw_categories.setFont(font)
        self.lw_categories.setAlternatingRowColors(True)
        self.lw_categories.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.lw_categories.setSelectionRectVisible(True)

        self.verticalLayout.addWidget(self.lw_categories)

        self.spl_filter_sort.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.spl_filter_sort)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbl_genrs = QLabel(self.layoutWidget1)
        self.lbl_genrs.setObjectName(u"lbl_genrs")
        self.lbl_genrs.setFont(font1)
        self.lbl_genrs.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_genrs)

        self.lw_genres = QListWidget(self.layoutWidget1)
        self.lw_genres.setObjectName(u"lw_genres")
        self.lw_genres.setFont(font)
        self.lw_genres.setAlternatingRowColors(True)
        self.lw_genres.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.lw_genres.setSelectionRectVisible(True)

        self.verticalLayout_2.addWidget(self.lw_genres)

        self.spl_filter_sort.addWidget(self.layoutWidget1)
        self.layoutWidget2 = QWidget(self.spl_filter_sort)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lbl_sort = QLabel(self.layoutWidget2)
        self.lbl_sort.setObjectName(u"lbl_sort")
        self.lbl_sort.setFont(font1)
        self.lbl_sort.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.lbl_sort)

        self.cb_sort = QComboBox(self.layoutWidget2)
        self.cb_sort.addItem("")
        self.cb_sort.addItem("")
        self.cb_sort.addItem("")
        self.cb_sort.setObjectName(u"cb_sort")
        self.cb_sort.setFont(font1)

        self.verticalLayout_3.addWidget(self.cb_sort)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.spl_filter_sort.addWidget(self.layoutWidget2)
        self.splitter.addWidget(self.spl_filter_sort)
        self.spl_songs = QSplitter(self.splitter)
        self.spl_songs.setObjectName(u"spl_songs")
        self.spl_songs.setOrientation(Qt.Orientation.Horizontal)
        self.lw_songs = QListWidget(self.spl_songs)
        self.lw_songs.setObjectName(u"lw_songs")
        self.lw_songs.setFont(font)
        self.lw_songs.setAlternatingRowColors(True)
        self.lw_songs.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.lw_songs.setSelectionRectVisible(True)
        self.spl_songs.addWidget(self.lw_songs)
        self.lbl_song_image = QLabel(self.spl_songs)
        self.lbl_song_image.setObjectName(u"lbl_song_image")
        self.lbl_song_image.setFont(font1)
        self.lbl_song_image.setFrameShape(QFrame.Shape.StyledPanel)
        self.lbl_song_image.setPixmap(QPixmap(u"../songs_images/song_image_test.png"))
        self.lbl_song_image.setScaledContents(True)
        self.lbl_song_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spl_songs.addWidget(self.lbl_song_image)
        self.te_song_text = QTextEdit(self.spl_songs)
        self.te_song_text.setObjectName(u"te_song_text")
        self.te_song_text.setFont(font)
        self.te_song_text.setReadOnly(True)
        self.spl_songs.addWidget(self.te_song_text)
        self.splitter.addWidget(self.spl_songs)
        self.le_search = QLineEdit(self.splitter)
        self.le_search.setObjectName(u"le_search")
        self.le_search.setFont(font)
        self.splitter.addWidget(self.le_search)

        self.verticalLayout_4.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 904, 22))
        self.menubar.setFont(font)
        self.menu_add = QMenu(self.menubar)
        self.menu_add.setObjectName(u"menu_add")
        self.menu_edit = QMenu(self.menubar)
        self.menu_edit.setObjectName(u"menu_edit")
        self.menu_delete = QMenu(self.menubar)
        self.menu_delete.setObjectName(u"menu_delete")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_add.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_delete.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_add.addAction(self.act_add_category)
        self.menu_add.addAction(self.act_add_genre)
        self.menu_add.addAction(self.act_add_song)
        self.menu_edit.addAction(self.act_edit_category)
        self.menu_edit.addAction(self.act_edit_genre)
        self.menu_edit.addAction(self.act_edit_song)
        self.menu_delete.addAction(self.act_delete_category)
        self.menu_delete.addAction(self.act_delete_genre)
        self.menu_delete.addAction(self.act_delete_song)
        self.menu_delete.addSeparator()
        self.menu_delete.addAction(self.act_clear_db)
        self.menu_help.addAction(self.act_abput_program)
        self.menu_help.addAction(self.act_about_author)
        self.menu_help.addAction(self.act_about_qt)

        self.retranslateUi(MainWindow)

        self.lw_songs.setCurrentRow(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0441\u0435\u043d\u043d\u0438\u043a", None))
        self.act_add_category.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e(\u0438\u0438)", None))
        self.act_add_genre.setText(QCoreApplication.translate("MainWindow", u"\u0416\u0430\u043d\u0440(\u044b)", None))
        self.act_add_song.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0441\u043d\u044e", None))
        self.act_edit_category.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
        self.act_edit_genre.setText(QCoreApplication.translate("MainWindow", u"\u0416\u0430\u043d\u0440", None))
        self.act_edit_song.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0441\u043d\u044e", None))
        self.act_delete_category.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e(\u0438\u0438)", None))
        self.act_delete_genre.setText(QCoreApplication.translate("MainWindow", u"\u0416\u0430\u043d\u0440(\u044b)", None))
        self.act_delete_song.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0441\u043d\u044e(\u0438)", None))
        self.act_clear_db.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.act_abput_program.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.act_about_author.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431 \u0430\u0432\u0442\u043e\u0440\u0435", None))
        self.act_about_qt.setText(QCoreApplication.translate("MainWindow", u"\u041e Qt", None))
        self.lbl_categories.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438:", None))
        self.lbl_genrs.setText(QCoreApplication.translate("MainWindow", u"\u0416\u0430\u043d\u0440\u044b:", None))
        self.lbl_sort.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c:", None))
        self.cb_sort.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044e", None))
        self.cb_sort.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0434\u0430\u0442\u0435 \u0438\u0441\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None))
        self.cb_sort.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0434\u0430\u0432\u043d\u043e \u0438\u0441\u043f\u043e\u043b\u043d\u044f\u0432\u0448\u0438\u0435\u0441\u044f", None))

        self.lbl_song_image.setText("")
        self.te_song_text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Lucida Console'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.le_search.setText("")
        self.le_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a...", None))
        self.menu_add.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.menu_edit.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.menu_delete.setTitle(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
    # retranslateUi

