# -*- coding: utf-8 -*-
""" Dialog edit songs """
import os
from sqlite3 import DatabaseError
from PySide6.QtWidgets import (
    QDialog,
    QMessageBox,
    QFileDialog,
)
from PySide6.QtCore import Slot, QDate
from PySide6.QtGui import QPixmap
from my_classes.songbook import Songbook
from gui import dlg_edit_songs_ui


class DlgEditSong(QDialog):
    """ Class DlgEditSong. """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = dlg_edit_songs_ui.Ui_dlg_edit_songs()
        self.ui.setupUi(self)

        # for updating song in the DB.
        # for reason to get acces to its from all methods.
        self._current_title: str = ""
        self._current_song_dict: dict = {}

        self.path_to_src_image: str = ""
        self.is_image_chosen: bool = False

        self.src_image_ext: str = ""
        self.path_to_images: str = f"{os.path.abspath(".")}{os.path.sep}images{os.path.sep}"
        self.new_song: dict = {}
        self.title: str = ""
        self.genres: list[str] = []
        self.category: str = ""
        self.song_image: str = ""
        self.song_text: str = ""
        self.last_performed: str = ""
        self.is_recently: int = 0
        self.comment: str = ""

        self.is_image_deleted: bool = False

        self.do_connections()
        # self.fill_in_categories()
        self.ui.le_song.setFocus()

    def do_connections(self):
        """ Do connections. """
        self.ui.btn_finish_and_save.clicked.connect(
            self.btn_finish_and_save_clicked)
        self.ui.btn_choose_image_file.clicked.connect(
            self.btn_choose_image_file_clicked)
        self.ui.btn_delete_image_file.clicked.connect(
            self.btn_delete_image_file_clicked)
        self.ui.btn_cancel.clicked.connect(self.close)

    @Slot(str)
    def get_current_song(self, current_title):
        """
        Slot to get current_title and fill in le_songs
        from Signal edit_song_called in main.py.
        """
        self._current_title = current_title
        try:
            my_songbook: Songbook = Songbook()  # Create Songbook INSTANCE.
            self._current_song_dict = my_songbook.get_the_song_as_dict(current_title)
        except DatabaseError:
            QMessageBox.critical(
                self,
                "Открытие базы данных", 
                "Ошибка при чтении жанров из базы данных.")
        else:
            self.fill_in_genres()
            self.fill_in_categories()
            self.ui.le_song.setText(self._current_title)
            if self._current_song_dict[self._current_title]["is_recently"] == 1:
                self.ui.chb_last_performed.setChecked(True)
            else:
                self.ui.chb_last_performed.setChecked(False)
            self.ui.de_last_performed.setDate(
                QDate.fromString(
                    self._current_song_dict[self._current_title]["last_performed"],
                    "dd MMMM yyyy"))
            self.ui.te_song_text.setText(
                self._current_song_dict[self._current_title]["song_text"])
            self.ui.te_comment.setText(
                self._current_song_dict[self._current_title]["comment"])
            self.song_image = self._current_song_dict[self._current_title]["song_image"]
            if self.song_image != "":
                self.ui.btn_delete_image_file.setEnabled(True)
                self.ui.lbl_song_image.setPixmap(QPixmap(self.song_image))
            else:
                self.ui.btn_delete_image_file.setEnabled(False)
                self.ui.lbl_song_image.setText("Нет картинки")

    def fill_in_genres(self):
        """ Get genres from DB and fill in lw_genres. """
        try:
            my_songbook: Songbook = Songbook()  # Create Songbook INSTANCE.
            genres: list = my_songbook.get_genres_from_db()
        except DatabaseError:
            QMessageBox.critical(
                self,
                "Открытие базы данных",
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
                # set selected genres for current song in lw_genres.
                for i in range(self.ui.lw_genres.count()):
                    if self.ui.lw_genres.item(i).text() in self._current_song_dict[self._current_title]["genres"]:
                        self.ui.lw_genres.item(i).setSelected(True)

    def fill_in_categories(self):
        """ Get categories from DB and fill in cb_categories. """
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
                self.ui.cb_categories.clear()
                for category in categories:
                    self.ui.cb_categories.addItem(category)
                # set category for current song in cb_categories.
                self.ui.cb_categories.setCurrentText(self._current_song_dict[self._current_title]["category"])

    @Slot()
    def btn_delete_image_file_clicked(self):
        """ Delete image file. """
        btn_reply = QMessageBox.critical(
            self,
            "Редактирование песни",
            "Удалить изображение?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if btn_reply == QMessageBox.Yes:
            self.ui.lbl_song_image.setText("Нет картинки")
            self.ui.btn_delete_image_file.setEnabled(False)
            self.is_image_deleted = True

    def delete_image_permanently(self) -> str:
        """
        Delete the song image file (before update data in DB)
        if it was chosen in btn_delete_image_file_clicked.
        """
        if (os.path.exists(self.song_image) and
                os.path.isfile(self.song_image)):
            try:
                os.remove(self.song_image)
            except FileNotFoundError:
                QMessageBox.critical(
                    self,
                    "Редактирование песни",
                    f"{self.song_image} не найден!")
        return ""

    @Slot()
    def btn_choose_image_file_clicked(self) -> None:
        """
        Choose an image file and get:
        path_to_src_image: str,
        src_image_basename: str,
        src_image_dirname: str,
        src_image_ext: str
        """
        image_file_tuple: tuple = QFileDialog.getOpenFileName(
            caption="Открыть файл",
            filter="Images (*.png *.jpg)")

        # self.path_to_src_image = image_file_tuple[0]
        # if self.path_to_src_image != "":
        if image_file_tuple[0] != "":
            self.path_to_src_image = image_file_tuple[0]
            src_image_basename: str = os.path.basename(self.path_to_src_image)
            self.src_image_ext = src_image_basename.split(".")[-1:][0]
            # preview an image
            self.ui.lbl_song_image.setPixmap(QPixmap(self.path_to_src_image))
            self.is_image_chosen = True
            self.ui.btn_delete_image_file.setEnabled(True)
        else:
            self.is_image_chosen = False

    def save_image_file(self, new_image_name: str) -> str:
        """ Save chosen image into images dir. """
        if self.is_image_chosen or self.path_to_src_image != "":
            if (not os.path.exists(self.path_to_images) or
                    not os.path.isdir(self.path_to_images)):
                os.makedirs(self.path_to_images)
            if " " in new_image_name:
                new_image_name = new_image_name.replace(" ", "_")
            path_to_dst_image: str = f"{self.path_to_images}{new_image_name}.{self.src_image_ext}"
            with open(self.path_to_src_image, "rb") as f:
                src_image = f.read()
                with open(path_to_dst_image, "wb") as f:
                    f.write(src_image)

            return path_to_dst_image
        # return the current path (not changed) to song_image
        return self._current_song_dict[self._current_title]["song_image"]

    @Slot()
    def btn_finish_and_save_clicked(self) -> None:
        """ Save song into DB. """
        # Getting the song from le_song and check it.
        self.title = self.ui.le_song.text().strip()
        # replace ' to " if entered. For sql requests.
        if "'" in self.title:
            self.title = self.title.replace("'", '"')
        if self.title == "":
            QMessageBox.information(
                self,
                "Редактирование песни",
                "Необходимо ввести название песни.")
            self.ui.le_song.setFocus()
        elif len(self.ui.lw_genres.selectedItems()) == 0:  # no one genre is chosen.
            QMessageBox.warning(
                self,
                "Редактирование песни",
                "Выберите жанр(ы) в списке.")
        elif self.ui.cb_categories.currentIndex() == -1:  # no chosen category.
            QMessageBox.warning(
                self,
                "Редактирование песни",
                "Выберите категорию.")
        else:
            try:
                # Create my_songbook INSTANCE and load data from the db.
                my_songbook: Songbook = Songbook()
            except DatabaseError:
                QMessageBox.critical(
                    self,
                    "Открытие базы данных",
                    "Ошибка при обращении к базе данных.")
            else:
                for item in self.ui.lw_genres.selectedItems():
                    self.genres.append(item.text())

                self.category = self.ui.cb_categories.currentText()

                if self.is_image_deleted:
                    self.song_image = self.delete_image_permanently()
                else:
                    self.song_image = self.save_image_file(self.title)

                self.song_text = self.ui.te_song_text.toPlainText()
                self.last_performed = self.ui.de_last_performed.date().toString(
                    "dd MMMM yyyy")
                self.is_recently = 1 if self.ui.chb_last_performed.isChecked() else 0
                self.comment = self.ui.te_comment.toPlainText()

                self.new_song = {
                    "title": self.title,
                    "genres": self.genres,
                    "category": self.category,
                    "song_image": self.song_image,
                    "song_text": self.song_text,
                    "last_performed": self.last_performed,
                    "is_recently": self.is_recently,
                    "comment": self.comment,
                }
                try:
                    my_songbook.update_song(
                                    self._current_title,
                                    self.new_song)
                except DatabaseError as e:
                    QMessageBox.critical(
                        self,
                        "Редактирование песни",
                        f"Ошибка при редактировании песни.{e}")
                else:
                    QMessageBox.information(
                        self,
                        "Редактирование песни",
                        "Песня успешно отредактирована.")
                    self.ui.lw_genres.setCurrentRow(-1)
                    self.ui.cb_categories.setCurrentIndex(-1)
                    self.ui.chb_last_performed.setChecked(False)
                    self.ui.te_song_text.clear()
                    self.ui.te_comment.clear()
                    self.ui.lbl_song_image.clear()
                    self.ui.le_song.clear()
                    self.ui.le_song.setFocus()
                    # for save_image method to check if an image is chosen.
                    self.path_to_src_image = ""
                    self.close()
