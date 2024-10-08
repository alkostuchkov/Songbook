# -*- coding: utf-8 -*-
""" Dialog add genres """
from sqlite3 import DatabaseError
from PySide6.QtWidgets import (
    QDialog,
    QMessageBox,
)
from my_classes.songbook import Songbook
from gui import dlg_add_genres_ui


class DlgAddGenre(QDialog):
    """ Class DlgAddGenre. """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = dlg_add_genres_ui.Ui_dlg_add_genres()
        self.ui.setupUi(self)

        self.do_connections()

    def do_connections(self):
        """ Do connections. """
        self.ui.btn_add_genre_to_list.clicked.connect(
            self.btn_add_genre_to_list_clicked
        )
        self.ui.btn_del_genre_from_list.clicked.connect(
            self.btn_del_genre_from_list_clicked
        )
        self.ui.btn_finish_and_save.clicked.connect(
            self.btn_finish_and_save_clicked
        )
        self.ui.btn_cancel.clicked.connect(self.close)

    def btn_add_genre_to_list_clicked(self):
        """ Add genre to list. """
        total_genres = self.ui.lw_adding_genres.count()
        # Getting the genre from le_genre and check it.
        genre = self.ui.le_genre.text().strip()
        # replace ' to " if entered. For sql requests.
        if "'" in genre:
            genre = genre.replace("'", '"')
        if genre == "":
            QMessageBox.information(
                self,
                "Добавление жанра",
                "Необходимо ввести жанр.")
            self.ui.le_genre.setFocus()
        else:  # add the genre to the lw_adding_genres
            # check if the adding genre exists in the lw_adding_genres.
            is_genre_exists = False
            for i in range(total_genres):
                self.ui.lw_adding_genres.setCurrentRow(i)
                if (self.ui.lw_adding_genres.currentItem().text().lower() ==
                        genre.lower()):
                    is_genre_exists = True
                    QMessageBox.warning(
                        self,
                        "Добавление жанра",
                        f"Жанр '{genre}' уже есть в списке.")
                    self.ui.le_genre.setFocus()
                    break
            if not is_genre_exists:
                self.ui.lw_adding_genres.addItem(genre)
                self.ui.lw_adding_genres.clearSelection()
                self.ui.le_genre.setFocus()

    def btn_del_genre_from_list_clicked(self):
        """ Deleting a wrong genre from lw_adding_genres. """
        total_genres = self.ui.lw_adding_genres.count()
        if total_genres == 0:  # lw_adding_genres is empty.
            QMessageBox.warning(
                self,
                "Добавление жанра",
                "Нечего удалять.\nСписок добавляемых жанров пуст.")
            self.ui.le_genre.setFocus()
        elif self.ui.lw_adding_genres.currentRow() == -1:  #  or no selection.
            QMessageBox.warning(
                self,
                "Добавление жанра",
                "Для удаления выберите жанр в списке.")
        else:  # not empty.
            for item in self.ui.lw_adding_genres.selectedItems():
                self.ui.lw_adding_genres.takeItem(
                    self.ui.lw_adding_genres.row(item))
                # item = None

    def btn_finish_and_save_clicked(self):
        """ Save added genres into DB. """
        try:
            # Create my_songbook INSTANCE and load data from the db.
            my_songbook: Songbook = Songbook()
            current_genres: list = my_songbook.get_genres_from_db()
        except DatabaseError:
            QMessageBox.critical(
                self,
                "Открытие базы данных",
                "Ошибка при обращении к базе данных.")
        else:
            new_genres: list[str] = []  # list of adding genres to pass to the DB.
            # Checking if the lw_adding_genres is not empty.
            total_genres = self.ui.lw_adding_genres.count()
            if total_genres == 0:
                QMessageBox.warning(
                    self,
                    "Добавление жанра",
                    "Список добавляемых жанров пуст.\n"
                    "Добавьте хотя бы один жанр.")
                self.ui.le_genre.setFocus()
            else:  # not empty.
                for idx in range(total_genres):
                    new_genres.append(
                        self.ui.lw_adding_genres.item(idx).text())
                # to avoid duplicates of genres in the different case such
                # as Genre_1 and genre_1.
                is_genre_exists: bool = False
                checking_genre: str = ""  # for QMessageBox
                for new_genre in new_genres:
                    for current_genre in current_genres:
                        if new_genre.lower() == current_genre.lower():
                            is_genre_exists = True
                            checking_genre = new_genre
                            break
                    if is_genre_exists:
                        break
                if is_genre_exists:
                    QMessageBox.warning(
                        self,
                        "Добавление жанра",
                        f"Жанр '{checking_genre}' уже есть в базе данных.")
                else:  # category not in DB
                    try:
                        my_songbook.insert_genres_into_db(new_genres)
                    except DatabaseError:
                        QMessageBox.critical(
                            self,
                            "Добавление жанра",
                            "Ошибка при добавлении жанра.")
                    else:
                        QMessageBox.information(
                            self,
                            "Добавление жанра",
                            "Жанры успешно добалены в песенник.")
                        self.ui.lw_adding_genres.clear()
                        self.ui.le_genre.clear()
                        self.ui.le_genre.setFocus()
