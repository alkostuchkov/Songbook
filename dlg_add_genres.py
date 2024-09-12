# -*- coding: utf-8 -*-
""" Dialog add genres """
from sqlite3 import DatabaseError
from PySide6.QtWidgets import (
    QDialog,
    QMessageBox,
)
from my_classes.songs import Songs
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
                "Добавление записи",
                "Необходимо ввести жанр.")
            self.ui.le_genre.setFocus()
        else:  # add the genre to the lw_adding_genres
            # check if the adding genre exists in the lw_adding_genres.
            is_genre_exists = False
            for i in range(total_genres):
                self.ui.lw_adding_genres.setCurrentRow(i)
                if self.ui.lw_adding_genres.currentItem().text() == genre:
                    is_genre_exists = True
                    QMessageBox.warning(
                        self,
                        "Добавление записи",
                        f"Жанр '{genre}' уже есть в списке.")
                    self.ui.le_genre.setFocus()
                    break
            if not is_genre_exists:
                self.ui.lw_adding_genres.addItem(genre)
                self.ui.lw_adding_genres.clearSelection()
                self.ui.le_genre.setFocus()

    def btn_del_genre_from_list_clicked(self):
        """ Deleting a wrong genre from lw_adding_categiries. """
        total_genres = self.ui.lw_adding_genres.count()
        if total_genres == 0:  # lw_adding_genres is empty.
            QMessageBox.warning(
                self,
                "Добавление записи",
                "Нечего удалять.\nСписок добавляемых жанров пуст.")
            self.ui.le_genre.setFocus()
        elif self.ui.lw_adding_genres.currentRow() == -1:  #  or no selection.
            QMessageBox.warning(
                self,
                "Добавление записи",
                "Для удаления выберите жанр в списке.")
        else:  # not empty.
            for item in self.ui.lw_adding_genres.selectedItems():
                self.ui.lw_adding_genres.takeItem(
                    self.ui.lw_adding_genres.row(item))
                # item = None

    def btn_finish_and_save_clicked(self):
        """ Save added genres into DB. """
        # Create my_songs INSTANCE and load data from the db.
        my_songs: Songs = Songs()
        try:  # open db and get dict.
            my_songs.open_db_and_get_dict()
            my_genres: list = my_songs.get_genres_from_db()
        except DatabaseError:
            QMessageBox.critical(
                self,
                "Открытие базы данных",
                "Ошибка при обращении к базе данных.")
        else:
            # Getting the genre and check it.
            genre = self.ui.le_genre.text().strip()
            # replace ' to " if entered. For sql requests.
            if "'" in genre:
                genre = genre.replace("'", '"')
            if genre == "":
                QMessageBox.warning(
                    self,
                    "Добавление записи",
                    "Необходимо ввести жанр.")
                self.ui.le_genre.setFocus()
            else:  # != ""
                # to avoid duplicates of genres in the different case such
                # as genre_1 and genre_1.
                is_genre_equal = False
                for genre_db in my_genres:
                    if genre.lower() == genre_db.lower():
                        is_genre_equal = True
                        break
                if is_genre_equal:
                    QMessageBox.warning(
                        self,
                        "Добавление записи",
                        f"Жанр '{genre}' уже есть в базе данных.\n"
                        "Для редактирования нажмите 'Отмена'\nи"
                        " выберите в главном окне "
                        "'Редактировать жанр'.")
                else:  # genre not in DB
                    genres = []  # list of adding genres to pass to the DB.
                    # Checking if the lw_adding_genres is not empty.
                    total_genres = self.ui.lw_adding_genres.count()
                    if total_genres == 0:
                        QMessageBox.warning(
                            self,
                            "Добавление записи",
                            "Список добавляемых жанров пуст.\n"
                            "Добавьте хотя бы один жанр.")
                        self.ui.le_genre.setFocus()
                    else:  # not empty.
                        for idx in range(total_genres):
                            genres.append(
                                self.ui.lw_adding_genres.item(idx).text())
                        try:
                            my_songs.insert_genres_into_db(genres)
                        except DatabaseError:
                            QMessageBox.critical(
                                self,
                                "Добавление записи",
                                "Ошибка при добавлении записи.")
                        else:
                            QMessageBox.information(
                                self,
                                "Добавление записи",
                                "Жанры успешно добалены в справочник.")
                            self.ui.lw_adding_genres.clear()
                            self.ui.le_genre.clear()
                            self.ui.le_genre.setFocus()
