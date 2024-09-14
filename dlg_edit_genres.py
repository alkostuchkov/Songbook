# -*- coding: utf-8 -*-
""" Dialog edit genres """
from sqlite3 import DatabaseError
from PySide6.QtWidgets import (
    QDialog,
    QMessageBox,
)
from PySide6.QtCore import Slot
from my_classes.songbook import Songbook
from gui import dlg_edit_genres_ui


class DlgEditGenre(QDialog):
    """ Class DlgEditGenre. """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = dlg_edit_genres_ui.Ui_dlg_edit_genres()
        self.ui.setupUi(self)

        # for updating genre in the DB.
        # for reason to get acces to its from all methods.
        self._current_genre: str = ""

        self._do_connections()

    def _do_connections(self):
        """ Do connections. """
        self.ui.btn_finish_and_save.clicked.connect(
            self.btn_finish_and_save_clicked
        )
        self.ui.btn_cancel.clicked.connect(self.close)

    @Slot(str)
    def get_current_genre(self, current_genre):
        """
        Slot to get current_genre and fill in le_genre
        from Signal edit_genre_called in main.py.
        """
        self.ui.le_genre.setText(current_genre)
        self._current_genre = current_genre

    def btn_finish_and_save_clicked(self):
        """ Save added genres into DB. """
        new_genre: str = self.ui.le_genre.text().strip()
        # replace ' to " if entered. For sql requests.
        if "'" in new_genre:
            new_genre = new_genre.replace("'", '"')
        if new_genre == "":
            QMessageBox.warning(
                self,
                "Редактирование жанра",
                "Необходимо ввести жанр.")
            self.ui.le_genre.setFocus()
        # check if the genre was changed.
        elif new_genre == self._current_genre:
            QMessageBox.information(
                self,
                "Редактирование жанра",
                "Название жанра не именилось.")
            self.ui.le_genre.setFocus()
        else:  # new_genre != current_genre
            try:  # Create my_songbook INSTANCE and load data from the db.
                my_songbook: Songbook = Songbook()
                current_genres: list = my_songbook.get_genres_from_db()
            except DatabaseError:
                QMessageBox.critical(
                    self,
                    "Открытие базы данных",
                    "Ошибка при обращении к базе данных.")
            else:
                # to avoid duplicates of genres in the different case such
                # as Genre_1 and genre_1.
                is_genre_exists: bool = False
                checking_genre: str = ""  # for QMessageBox
                for current_genre in current_genres:
                    if new_genre.lower() == current_genre.lower():
                        is_genre_exists = True
                        checking_genre = new_genre
                        break
                if is_genre_exists:
                    QMessageBox.warning(
                        self,
                        "Редактирование жанра",
                        f"Жанр '{checking_genre}' уже есть в базе данных.")
                else:  # genre is not in DB
                    try:
                        my_songbook.update_genres(self._current_genre, new_genre)
                    except DatabaseError:
                        QMessageBox.critical(
                            self,
                            "Редактирование жанра",
                            "Ошибка при добавлении жанра.")
                    else:
                        QMessageBox.information(
                            self,
                            "Редактирование жанра",
                            "Жанр успешно отредактирован.")
                        self.ui.le_genre.clear()
                        self.close()

