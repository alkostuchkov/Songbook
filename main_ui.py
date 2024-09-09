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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QSpacerItem,
    QSplitter, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(904, 612)
        self.act_add_category = QAction(MainWindow)
        self.act_add_category.setObjectName(u"act_add_category")
        self.act_add_genre = QAction(MainWindow)
        self.act_add_genre.setObjectName(u"act_add_genre")
        self.act_add_song = QAction(MainWindow)
        self.act_add_song.setObjectName(u"act_add_song")
        self.act_edit_category = QAction(MainWindow)
        self.act_edit_category.setObjectName(u"act_edit_category")
        self.act_edit_genre = QAction(MainWindow)
        self.act_edit_genre.setObjectName(u"act_edit_genre")
        self.act_edit_song = QAction(MainWindow)
        self.act_edit_song.setObjectName(u"act_edit_song")
        self.act_delete_category = QAction(MainWindow)
        self.act_delete_category.setObjectName(u"act_delete_category")
        self.act_delete_genre = QAction(MainWindow)
        self.act_delete_genre.setObjectName(u"act_delete_genre")
        self.act_delete_song = QAction(MainWindow)
        self.act_delete_song.setObjectName(u"act_delete_song")
        self.act_clear_db = QAction(MainWindow)
        self.act_clear_db.setObjectName(u"act_clear_db")
        self.act_abput_program = QAction(MainWindow)
        self.act_abput_program.setObjectName(u"act_abput_program")
        self.act_about_author = QAction(MainWindow)
        self.act_about_author.setObjectName(u"act_about_author")
        self.act_about_qt = QAction(MainWindow)
        self.act_about_qt.setObjectName(u"act_about_qt")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.splitter_3 = QSplitter(self.centralwidget)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Orientation.Vertical)
        self.splitter_2 = QSplitter(self.splitter_3)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Horizontal)
        self.widget = QWidget(self.splitter_2)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_categories = QLabel(self.widget)
        self.lbl_categories.setObjectName(u"lbl_categories")
        self.lbl_categories.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_categories)

        self.lw_categories = QListWidget(self.widget)
        QListWidgetItem(self.lw_categories)
        QListWidgetItem(self.lw_categories)
        QListWidgetItem(self.lw_categories)
        QListWidgetItem(self.lw_categories)
        self.lw_categories.setObjectName(u"lw_categories")
        self.lw_categories.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.lw_categories.setSelectionRectVisible(True)

        self.verticalLayout.addWidget(self.lw_categories)

        self.splitter_2.addWidget(self.widget)
        self.widget1 = QWidget(self.splitter_2)
        self.widget1.setObjectName(u"widget1")
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbl_genrs = QLabel(self.widget1)
        self.lbl_genrs.setObjectName(u"lbl_genrs")
        self.lbl_genrs.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_genrs)

        self.lw_genres = QListWidget(self.widget1)
        QListWidgetItem(self.lw_genres)
        QListWidgetItem(self.lw_genres)
        QListWidgetItem(self.lw_genres)
        QListWidgetItem(self.lw_genres)
        self.lw_genres.setObjectName(u"lw_genres")
        self.lw_genres.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.lw_genres.setSelectionRectVisible(True)

        self.verticalLayout_2.addWidget(self.lw_genres)

        self.splitter_2.addWidget(self.widget1)
        self.widget2 = QWidget(self.splitter_2)
        self.widget2.setObjectName(u"widget2")
        self.verticalLayout_3 = QVBoxLayout(self.widget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lbl_sort = QLabel(self.widget2)
        self.lbl_sort.setObjectName(u"lbl_sort")
        self.lbl_sort.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.lbl_sort)

        self.cb_sort = QComboBox(self.widget2)
        self.cb_sort.addItem("")
        self.cb_sort.addItem("")
        self.cb_sort.addItem("")
        self.cb_sort.setObjectName(u"cb_sort")

        self.verticalLayout_3.addWidget(self.cb_sort)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.splitter_2.addWidget(self.widget2)
        self.splitter_3.addWidget(self.splitter_2)
        self.splitter = QSplitter(self.splitter_3)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.widget3 = QWidget(self.splitter)
        self.widget3.setObjectName(u"widget3")
        self.verticalLayout_4 = QVBoxLayout(self.widget3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lbl_songs = QLabel(self.widget3)
        self.lbl_songs.setObjectName(u"lbl_songs")
        self.lbl_songs.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbl_songs)

        self.llw_songs = QListWidget(self.widget3)
        QListWidgetItem(self.llw_songs)
        QListWidgetItem(self.llw_songs)
        QListWidgetItem(self.llw_songs)
        QListWidgetItem(self.llw_songs)
        self.llw_songs.setObjectName(u"llw_songs")
        self.llw_songs.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.llw_songs.setSelectionRectVisible(True)

        self.verticalLayout_4.addWidget(self.llw_songs)

        self.splitter.addWidget(self.widget3)
        self.widget4 = QWidget(self.splitter)
        self.widget4.setObjectName(u"widget4")
        self.verticalLayout_5 = QVBoxLayout(self.widget4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lbl_song_image_2 = QLabel(self.widget4)
        self.lbl_song_image_2.setObjectName(u"lbl_song_image_2")
        self.lbl_song_image_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.lbl_song_image_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.lbl_song_image = QLabel(self.widget4)
        self.lbl_song_image.setObjectName(u"lbl_song_image")
        self.lbl_song_image.setPixmap(QPixmap(u"song_image_test.png"))
        self.lbl_song_image.setScaledContents(True)
        self.lbl_song_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.lbl_song_image)

        self.splitter.addWidget(self.widget4)
        self.widget5 = QWidget(self.splitter)
        self.widget5.setObjectName(u"widget5")
        self.verticalLayout_6 = QVBoxLayout(self.widget5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lbl_song_text = QLabel(self.widget5)
        self.lbl_song_text.setObjectName(u"lbl_song_text")
        self.lbl_song_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.lbl_song_text)

        self.te_song_text = QTextEdit(self.widget5)
        self.te_song_text.setObjectName(u"te_song_text")

        self.verticalLayout_6.addWidget(self.te_song_text)

        self.splitter.addWidget(self.widget5)
        self.splitter_3.addWidget(self.splitter)
        self.le_search = QLineEdit(self.splitter_3)
        self.le_search.setObjectName(u"le_search")
        self.splitter_3.addWidget(self.le_search)

        self.verticalLayout_7.addWidget(self.splitter_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 904, 19))
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

        self.llw_songs.setCurrentRow(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.act_add_category.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
        self.act_add_genre.setText(QCoreApplication.translate("MainWindow", u"\u0416\u0430\u043d\u0440", None))
        self.act_add_song.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0441\u043d\u044e", None))
        self.act_edit_category.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
        self.act_edit_genre.setText(QCoreApplication.translate("MainWindow", u"\u0416\u0430\u043d\u0440", None))
        self.act_edit_song.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0441\u043d\u044e", None))
        self.act_delete_category.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
        self.act_delete_genre.setText(QCoreApplication.translate("MainWindow", u"\u0416\u0430\u043d\u0440", None))
        self.act_delete_song.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0441\u043d\u044e", None))
        self.act_clear_db.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.act_abput_program.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.act_about_author.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431 \u0430\u0432\u0442\u043e\u0440\u0435", None))
        self.act_about_qt.setText(QCoreApplication.translate("MainWindow", u"\u041e Qt", None))
        self.lbl_categories.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438:", None))

        __sortingEnabled = self.lw_categories.isSortingEnabled()
        self.lw_categories.setSortingEnabled(False)
        ___qlistwidgetitem = self.lw_categories.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435", None));
        ___qlistwidgetitem1 = self.lw_categories.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0411\u044b\u0441\u0442\u0440\u044b\u0435", None));
        ___qlistwidgetitem2 = self.lw_categories.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0438\u0435", None));
        ___qlistwidgetitem3 = self.lw_categories.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0434\u043b\u0435\u043d\u043d\u044b\u0435", None));
        self.lw_categories.setSortingEnabled(__sortingEnabled)

        self.lbl_genrs.setText(QCoreApplication.translate("MainWindow", u"\u0416\u0430\u043d\u0440\u044b:", None))

        __sortingEnabled1 = self.lw_genres.isSortingEnabled()
        self.lw_genres.setSortingEnabled(False)
        ___qlistwidgetitem4 = self.lw_genres.item(0)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435", None));
        ___qlistwidgetitem5 = self.lw_genres.item(1)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437 \u043f\u0435\u0441\u0435\u043d\u043d\u0438\u043a\u0430", None));
        ___qlistwidgetitem6 = self.lw_genres.item(2)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0435", None));
        ___qlistwidgetitem7 = self.lw_genres.item(3)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430 \u0425\u043b\u0435\u0431\u043e\u043f\u0440\u0435\u043b\u043e\u043c\u043b\u0435\u043d\u0438\u0435", None));
        self.lw_genres.setSortingEnabled(__sortingEnabled1)

        self.lbl_sort.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c:", None))
        self.cb_sort.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044e", None))
        self.cb_sort.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0434\u0430\u0442\u0435 \u0438\u0441\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None))
        self.cb_sort.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0434\u0430\u0432\u043d\u043e \u0438\u0441\u043f\u043e\u043b\u043d\u044f\u0432\u0448\u0438\u0435\u0441\u044f", None))

        self.lbl_songs.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0441\u043d\u0438:", None))

        __sortingEnabled2 = self.llw_songs.isSortingEnabled()
        self.llw_songs.setSortingEnabled(False)
        ___qlistwidgetitem8 = self.llw_songs.item(0)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem9 = self.llw_songs.item(1)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem10 = self.llw_songs.item(2)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem11 = self.llw_songs.item(3)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        self.llw_songs.setSortingEnabled(__sortingEnabled2)

        self.lbl_song_image_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442-\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.lbl_song_image.setText("")
        self.lbl_song_text.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442 \u043f\u0435\u0441\u043d\u0438", None))
        self.le_search.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a...", None))
        self.menu_add.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.menu_edit.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.menu_delete.setTitle(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
    # retranslateUi

