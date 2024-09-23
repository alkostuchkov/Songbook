# -*- coding: utf-8 -*-
""" Main window """
import os
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
    Signal,
    Slot,
)
from PySide6.QtGui import (
    QFont,
    QPixmap,
)
from gui import main_ui
from dlg_add_categories import DlgAddCategory
from dlg_edit_categories import DlgEditCategory
from dlg_add_genres import DlgAddGenre
from dlg_edit_genres import DlgEditGenre
from dlg_add_songs import DlgAddSong
from dlg_edit_songs import DlgEditSong
from my_classes.songbook import Songbook


class MainWindow(QMainWindow):
    """ Class MainWindow. """
    # my SIGNALs when act_edit_(category, genre) tiggered
    # to pass current (category, genre).
    edit_category_called = Signal(str)
    edit_genre_called = Signal(str)
    edit_song_called = Signal(str)

    # # my SIGNALs when lblZoomIn and lblZoomOut clicked.
    # lblZoomInClicked = QtCore.pyqtSignal()
    # lblZoomOutClicked = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = main_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        self.path_to_images: str = f"{os.path.abspath(".")}{os.path.sep}images{os.path.sep}"
        # self.path_to_texts: str = f"{os.path.abspath(".")}{os.path.sep}texts{os.path.sep}"

        # to get access to Songbook's dict
        # and not to create an instance of Songbook 
        # every click on lw_songs_item_clicked.
        self.songs_dict: dict = {}
        self.title: str = ""

        self.font_size = 14
        self.font_family = self.ui.lw_genres.font().family()  # Lucida Console

        self.total_records: int = 0
        self.str_total_records = " Количество записей: "
        self.selected_records: int = 0
        self.str_selected_records = " Выбрано: "
        self.found_records: int = 0
        self.str_found_records = " Найдено: "
        # self.isLedSearchConnected = False

        self.create_statusbar()
        self.do_connections()

        self.fill_in_genres()
        self.fill_in_categories()
        self.show_songs()

    def do_connections(self) -> None:
        """ Do connections. """
        self.btn_close.clicked.connect(self.close)
        self.ui.act_add_category.triggered.connect(self.act_add_category_triggered)
        self.ui.act_add_genre.triggered.connect(self.act_add_genre_triggered)
        self.ui.act_add_song.triggered.connect(self.act_add_song_triggered)
        self.ui.act_delete_category.triggered.connect(
            self.act_delete_category_triggered)
        self.ui.act_delete_genre.triggered.connect(
            self.act_delete_genre_triggered)
        self.ui.act_delete_song.triggered.connect(
            self.act_delete_song_triggered)
        self.ui.act_edit_category.triggered.connect(
            self.act_edit_category_triggered)
        self.ui.act_edit_genre.triggered.connect(
            self.act_edit_genre_triggered)
        self.ui.act_edit_song.triggered.connect(
            self.act_edit_song_triggered)
        self.ui.lw_songs.currentRowChanged.connect(
            self.lw_songs_currentrow_changed)
        self.ui.act_about_qt.triggered.connect(lambda: QMessageBox.aboutQt(self))

    def create_statusbar(self) -> None:
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

    def fill_in_categories(self) -> None:
        """ Fill in lw_categories from DB. """
        try:
            my_songbook: Songbook = Songbook()  # Create Songbook INSTANCE.
            categories: list = my_songbook.get_categories_from_db()
        except DatabaseError:
            QMessageBox.critical(
                self,
                "Открытие базы данных", 
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
                    self.ui.lw_categories.addItem(category)

    def fill_in_genres(self) -> None:
        """ Fill in lw_genres from DB. """
        try:
            my_songbook: Songbook = Songbook()
            genres: list = my_songbook.get_genres_from_db()
        except DatabaseError:
            QMessageBox.critical(
                self, "Открытие базы данных", 
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
                    self.ui.lw_genres.addItem(genre)

    @Slot()
    def lw_songs_currentrow_changed(self) -> None:
        """ Change te_song_text widget text when the item clicked. """
        # get current song's title.
        if self.ui.lw_songs.currentRow() != -1:  # avoid empty self.title (= "").
            text = self.ui.lw_songs.currentItem().text()
            i = text.find(":\n")  # SongName:\n
            self.title = text[:i]

        self.ui.te_song_text.setPlainText(
            self.songs_dict[self.title]["song_text"])

        song_image: str = self.songs_dict[self.title]["song_image"]
        if song_image == "":
            self.ui.lbl_song_image.setText("Нет картинки")
        else:
            self.ui.lbl_song_image.setPixmap(QPixmap(song_image))

    def show_songs(self) -> None:
        """ Show all songs records. """
        try:
            # Create Songbook INSTANCE and load data from the db.
            my_songbook: Songbook = Songbook()
            my_songbook_dict: dict = my_songbook.get_data_as_dict()
            # to get access to Songbook's dict
            # and not to create an instance of Songbook 
            # every click on lw_songs_item_clicked.
            self.songs_dict = my_songbook_dict
        except DatabaseError:
            QMessageBox.critical(
                self,
                "Открытие базы данных", 
                "Ошибка при обращении к базе данных.")
        else:
            self.total_records = len(my_songbook_dict)
            self.lbl_total_records.setText(
                f"{self.str_total_records}{str(self.total_records)}")
            self.found_records = 0
            self.lbl_found_records.setText(
                f"{self.str_found_records}{str(self.found_records)}")
            # check if the my_songbook.songbook is empty.
            if len(my_songbook_dict) == 0:
                QMessageBox.warning(
                    self,
                    "Показать все записи",
                    "Ваш песенник пуст.\n"
                    "Выберите 'Добавить песню' в главном окне.")
            else:
                self.ui.lw_songs.clear()
                output_str: str = ""
                for key in sorted(my_songbook_dict):
                    desc_str: str = ""
                    output_str = str(key) + ":\n"
                    genres_str: str = ", ".join(my_songbook_dict[key]["genres"])
                    desc_str = " " * (len(output_str) - 1) + genres_str + "\n"
                    desc_str += " " * (len(output_str) - 1) + my_songbook_dict[key]["category"] + "\n"
                    desc_str += " " * (len(output_str) - 1) + my_songbook_dict[key]["last_performed"] + "\n"
                    desc_str += " " * (len(output_str) - 1) + my_songbook_dict[key]["comment"]
                    output_str += desc_str  # [:-1]  # Delete last "\n"
                    current_item: QListWidgetItem = QListWidgetItem(output_str)
                    self.ui.lw_songs.addItem(current_item)
                    if my_songbook_dict[key]["is_recently"] == 1:
                        current_item.setCheckState(Qt.CheckState.Checked)
                    else:
                        current_item.setCheckState(Qt.CheckState.Unchecked)
                    self.ui.lw_songs.clearSelection()
        self.ui.lw_songs.setCurrentRow(0)  # 

    @Slot()
    def act_add_category_triggered(self) -> None:
        """  Create the instance of DlgAddCategory Class and show it. """
        dlg_add_category: DlgAddCategory = DlgAddCategory()
        dlg_add_category.exec()
        self.fill_in_categories()

    @Slot()
    def act_add_genre_triggered(self) -> None:
        """  Create the instance of DlgAddGenre Class and show it. """
        dlg_add_genre: DlgAddGenre = DlgAddGenre()
        dlg_add_genre.exec()
        self.fill_in_genres()

    @Slot()
    def act_add_song_triggered(self) -> None:
        """  Create the instance of DlgAddSong Class and show it. """
        dlg_add_song: DlgAddSong = DlgAddSong()
# BUG: check showMaximized on other OS
# dlg_add_song.setModal(True)
# dlg_add_song.showMaximized()
        dlg_add_song.exec()
        self.fill_in_categories()
        self.fill_in_genres()
        self.show_songs()

    @Slot()
    def act_delete_category_triggered(self) -> None:
        """ Delete category(ies). """
        total_categories = self.ui.lw_genres.count()
        categories: list = []
        if total_categories == 0:  # lw_categories is empty.
            QMessageBox.warning(
                self,
                "Удаление категории(ий)",
                "Нечего удалять.\nСписок категорий пуст.")
        elif self.ui.lw_genres.currentRow() == -1:  #  or no selection.
            QMessageBox.warning(
                self,
                "Удаление категории(й)",
                "Для удаления выберите категорию(ии) в списке.")
        else:  # not empty.
            btn_reply = QMessageBox.critical(
                self,
                "Удаление категории(ий)",
                "Данное действие удалит выбранные КАТЕГОРИИ и\n"
                "ПЕСНИ с данными категориями из песенника безвозвратно.\n"
                "Вы точно уверены, что хотите этого?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No)
            if btn_reply == QMessageBox.Yes:
                for item in self.ui.lw_genres.selectedItems():
                    categories.append(
                        self.ui.lw_genres.takeItem(
                            self.ui.lw_genres.row(item)).text())
                try:
                    # Create Songbook INSTANCE and load data from the db.
                    my_songbook: Songbook = Songbook()
                    my_songbook.delete_categories_from_db(categories)
                except DatabaseError:
                    QMessageBox.critical(
                        self,
                        "Открытие базы данных", 
                        "Ошибка при обращении к базе данных.")
                else:
                    QMessageBox.information(
                        self,
                        "Удаление категории(ий)",
                        "Категории успешно удалены из песенника.")

                    self.fill_in_categories()
                    self.show_songs()

    @Slot()
    def act_delete_genre_triggered(self) -> None:
        """ Delete genre(s). """
        total_genres = self.ui.lw_genres.count()
        genres: list = []
        if total_genres == 0:  # lw_categories is empty.
            QMessageBox.warning(
                self,
                "Удаление жанра(ов)",
                "Нечего удалять.\nСписок жанров пуст.")
        elif self.ui.lw_genres.currentRow() == -1:  #  or no selection.
            QMessageBox.warning(
                self,
                "Удаление жанра(ов)",
                "Для удаления выберите жанр(ы) в списке.")
        else:  # not empty.
            btn_reply = QMessageBox.critical(
                self,
                "Удаление жанра(ов)",
                "Данное действие удалит выбранные ЖАНРЫ и\n"
                "ПЕСНИ с данными жанрами из песенника безвозвратно.\n"
                "Вы точно уверены, что хотите этого?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No)
            if btn_reply == QMessageBox.Yes:
                for item in self.ui.lw_genres.selectedItems():
                    genres.append(
                        self.ui.lw_genres.takeItem(
                            self.ui.lw_genres.row(item)).text())
                try:
                    # Create Songbook INSTANCE and load data from the db.
                    my_songbook: Songbook = Songbook()
                    my_songbook.delete_genres_from_db(genres)
                except DatabaseError:
                    QMessageBox.critical(
                        self,
                        "Открытие базы данных", 
                        "Ошибка при обращении к базе данных.")
                else:
                    QMessageBox.information(
                        self,
                        "Удаление жанра(ов)",
                        "Жанры успешно удалены из песенника.")

                    self.fill_in_genres()
                    self.show_songs()


    @Slot()
    def act_delete_song_triggered(self) -> None:
        """ Delete song(s). """
# TODO: implementation

    @Slot()
    def act_edit_category_triggered(self) -> None:
        """ Edit category. """
        # check if there is multiselection in the lw_categories
        if len(self.ui.lw_categories.selectedItems()) > 1:
            QMessageBox.warning(
                self,
                "Редактирование категории",
                "Вы не можете редактировать несколько категорий одновременно.\n"
                "Выберите одну категорию.")
        else:
            total_categories = self.ui.lw_categories.count()
            if total_categories == 0:  # lw_categories is empty.
                QMessageBox.warning(
                    self,
                    "Редактирование категории",
                    "Нечего редактировать\n"
                    "Список категорий пуст.")
            elif self.ui.lw_categories.currentRow() == -1:  # or no selection.
                QMessageBox.warning(
                    self,
                    "Редактирование категории",
                    "Нечего редактировать.\n"
                    "Для редактирования выберите категорию в списке.")
                self.ui.lw_categories.setFocus()
            else:  # is selected.
                # create instance of DlgEditCategory.
                dlg_edit_category = DlgEditCategory()
                # connect edit_category_called (my SIGNAL).
                self.edit_category_called.connect(dlg_edit_category.get_current_category)
                # emit SIGNAL edit_category_called (pass: current category).
                self.edit_category_called.emit(
                    self.ui.lw_categories.currentItem().text())
                dlg_edit_category.exec()
                # update categories and songs in the MainWindow.
                self.fill_in_categories()
                self.show_songs()

    @Slot()
    def act_edit_genre_triggered(self) -> None:
        """ Edit genre. """
        # check if there is multiselection in the lw_genres
        if len(self.ui.lw_genres.selectedItems()) > 1:
            QMessageBox.warning(
                self,
                "Редактирование жанра",
                "Вы не можете редактировать несколько жанров одновременно.\n"
                "Выберите один жанр.")
        else:
            total_genres = self.ui.lw_genres.count()
            if total_genres == 0:  # lw_genres is empty.
                QMessageBox.warning(
                    self,
                    "Редактирование жанра",
                    "Нечего редактировать\n"
                    "Список жанров пуст.")
            elif self.ui.lw_genres.currentRow() == -1:  # or no selection.
                QMessageBox.warning(
                    self,
                    "Редактирование жанра",
                    "Нечего редактировать.\n"
                    "Для редактирования выберите жанр в списке.")
                self.ui.lw_genres.setFocus()
            else:  # is selected.
                # create instance of DlgEditGenre.
                dlg_edit_genre: DlgEditGenre = DlgEditGenre()
                # connect edit_genre_called (my SIGNAL).
                self.edit_genre_called.connect(dlg_edit_genre.get_current_genre)
                # emit SIGNAL edit_genre_called (pass: current genre).
                self.edit_genre_called.emit(
                    self.ui.lw_genres.currentItem().text())
                dlg_edit_genre.exec()
                # update genres and songs in the MainWindow.
                self.fill_in_genres()
                self.show_songs()

    @Slot()
    def act_edit_song_triggered(self) -> None:
        """  Edit selected song. """
        # check if there is multiselection in the lw_songs
        if len(self.ui.lw_songs.selectedItems()) > 1:
            QMessageBox.warning(
                self,
                "Редактирование песни",
                "Вы не можете редактировать несколько песен одновременно.\n"
                "Выберите одну песню.")
        else:
            total_songs = self.ui.lw_songs.count()
            if total_songs == 0:  # lw_songs is empty.
                QMessageBox.warning(
                    self,
                    "Редактирование песни",
                    "Нечего редактировать\n"
                    "Список песен пуст.")
            elif self.ui.lw_songs.currentRow() == -1:  # or no selection.
                QMessageBox.warning(
                    self,
                    "Редактирование песни",
                    "Нечего редактировать.\n"
                    "Для редактирования выберите песню в списке.")
                self.ui.lw_songs.setFocus()
            else:  # is selected.
                # create instance of DlgEditSong.
                dlg_edit_song: DlgEditSong = DlgEditSong()
                # connect edit_song_called (my SIGNAL).
                self.edit_song_called.connect(dlg_edit_song.get_current_song)
                # emit SIGNAL edit_song_called (pass: current song as dict).
                self.edit_song_called.emit(self.title)
# BUG: check showMaximized on other OS
# dlg_add_song.setModal(True)
# dlg_add_song.showMaximized()
                dlg_edit_song.exec()
                self.fill_in_categories()
                self.fill_in_genres()
                self.show_songs()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    window = MainWindow()
    window.showMaximized()

    sys.exit(app.exec())
