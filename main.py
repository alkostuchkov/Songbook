# -*- coding: utf-8 -*-
""" Main window """
from sqlite3 import DatabaseError
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QMessageBox,
    QWidget,
    QSpacerItem,
    QSizePolicy,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QListWidgetItem,
)
from PySide6.QtCore import (
    Qt,
    QDate,
    Signal,
    Slot,
)
from PySide6.QtGui import QFont
from my_classes.songs import Songs
import main_ui


class MainWindow(QMainWindow):
    """ Class MainWindow. """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = main_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        self.font_size = 14
        self.font_family = self.ui.lw_genres.font().family()

        self.total_records: int = 0
        self.selected_records: int = 0
        self.found_records: int = 0
        # self.__isLedSearchConnected = False

        self.create_statusbar()
        self.do_connections()

        self.fill_in_genres()
        self.fill_in_categories()
        self.show_records()


    def do_connections(self):
        """ Do connections. """

        self.btn_close.clicked.connect(self.close)
        self.ui.act_add_category.triggered.connect(self.act_add_category_triggered)
        self.ui.act_add_genre.triggered.connect(self.act_add_genre_triggered)
        self.ui.act_add_song.triggered.connect(self.act_add_song_triggered)

    def create_statusbar(self):
        """ Creates statusbar and components for its. """

        self.stbar = self.ui.statusbar
        self.lbl_total_records = QLabel(" Количество записей: ")
        self.lbl_total_records.setFont(QFont(self.font_family, self.font_size))
        self.lbl_selected_records = QLabel(" Выбрано: ")
        self.lbl_selected_records.setFont(QFont(self.font_family, self.font_size))
        self.lbl_found_records = QLabel(" Найдено: ")
        self.lbl_found_records.setFont(QFont(self.font_family, self.font_size))
        self.btn_close = QPushButton("Закрыть")
        self.btn_close.setFont(QFont(self.font_family, self.font_size))

        widget = QWidget(self)
        widget.setLayout(QHBoxLayout())
        spacer_item = QSpacerItem(20, 40, QSizePolicy.Policy.Preferred)
        widget.layout().addWidget(self.lbl_total_records)
        widget.layout().addItem(spacer_item)
        widget.layout().addWidget(self.lbl_selected_records)
        widget.layout().addWidget(self.lbl_found_records)

        # add widget with 3 labels and ui.btnExit into the statusBar.
        self.stbar.addPermanentWidget(widget, 3)
        self.stbar.addPermanentWidget(self.btn_close, 1)

    def fill_in_categories(self):
        """ Fill in lw_categories from DB. """
        # Create Songs INSTANCE and load data from the db.
        my_songs: Songs = Songs()
        try:
            categories: list = my_songs.get_categories_from_db()
        except DatabaseError:
            QMessageBox.critical(self, "Открытие базы данных", 
                                 "Ошибка при чтении категорий из базы данных.")
        else:
            if len(categories) == 0:
                QMessageBox.warning(
                    self,
                    "Заполнить список категорий",
                    "Ваш список категорий пуст.\n"
                    "Выберите 'Добавить категорию' в главном окне.")
            else:
                self.ui.lw_categories.clear()
                for category in categories:
                    self.ui.lw_categories.addItems(category)

    def fill_in_genres(self):
        """ Fill in lw_genres from DB. """
        # Create Songs INSTANCE and load data from the db.
        my_songs: Songs = Songs()
        try:
            genres: list = my_songs.get_genres_from_db()
        except DatabaseError:
            QMessageBox.critical(self, "Открытие базы данных", 
                                 "Ошибка при чтении жанров из базы данных.")
        else:
            if len(genres) == 0:
                QMessageBox.warning(
                    self,
                    "Заполнить список жанров",
                    "Ваш список жанров пуст.\n"
                    "Выберите 'Добавить жанр' в главном окне.")
            else:
                self.ui.lw_genres.clear()
                for genre in genres:
                    self.ui.lw_genres.addItems(genre)

    def show_records(self):
        """ Show all records. """
        # Create Songs INSTANCE and load data from the db.
        my_songs: Songs = Songs()
        try:
            my_songs.open_db_and_get_dict()
        except DatabaseError:
            QMessageBox.critical(self, "Открытие базы данных", 
                                 "Ошибка при обращении к базе данных.")
        else:
            self.total_records = len(my_songs.songs)
            self.lbl_total_records.setText(
                f"{self.lbl_total_records.text()}{str(self.total_records)}")
            self.found_records = 0
            self.lbl_found_records.setText(
                f"{self.lbl_found_records.text()}{str(self.found_records)}")
            # check if the my_songs.songs is empty.
            if len(my_songs.songs) == 0:
                QMessageBox.warning(
                    self,
                    "Показать все записи",
                    "Ваш песенник пуст.\n"
                    "Выберите 'Добавить песню' в главном окне.")
            else:
                self.ui.lw_songs.clear()
                current_row: int = 0
                output_str: str = ""
                for key in sorted(my_songs.songs):
                    desc_str: str = ""
                    output_str = str(key) + ":\n"
                    genres_str: str = ", ".join(my_songs.songs[key]["genres"])
                    desc_str = " " * (len(output_str) + 1) + genres_str + "\n"
                    desc_str += " " * (len(output_str) + 1) + my_songs.songs[key]["category"] + "\n"
                    desc_str += " " * (len(output_str) + 1) + my_songs.songs[key]["last_performed"] + "\n"
                    desc_str += " " * (len(output_str) + 1) + my_songs.songs[key]["comment"]
                    output_str += desc_str  # [:-1]  # Delete last "\n"
                    self.ui.lw_songs.addItem(output_str)

                    self.ui.lw_songs.setCurrentRow(current_row)
                    if my_songs.songs[key]["is_recently"] == 1:
                        self.ui.lw_songs.currentItem().setCheckState(Qt.CheckState.Checked)
                    else:
                        self.ui.lw_songs.currentItem().setCheckState(Qt.CheckState.Unchecked)
                    current_row += 1
                    self.ui.lw_songs.clearSelection()
            # The INSTANCE of my_songs, created in the beginning
            # of this method is destroying here!!!

    @Slot()
    def act_add_category_triggered(self):
        """ Add category. """

    @Slot()
    def act_add_genre_triggered(self):
        """ Add genre. """

    @Slot()
    def act_add_song_triggered(self):
        """ Add song. """

    @Slot()
    def act_edit_category_triggered(self):
        """ Edit category. """

    @Slot()
    def act_edit_genre_triggered(self):
        """ Edit genre. """


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    window = MainWindow()
    window.showMaximized()

    sys.exit(app.exec())
