# -*- coding: utf-8 -*-
""" Dialog add songs """
import os
from sqlite3 import DatabaseError
from PySide6.QtWidgets import (
    QDialog,
    QMessageBox,
    QFileDialog,
)
from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap
from my_classes.songbook import Songbook
from gui import dlg_add_songs_ui


class DlgAddSong(QDialog):
    """ Class DlgAddSong. """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = dlg_add_songs_ui.Ui_dlg_add_songs()
        self.ui.setupUi(self)

        self.path_to_src_image: str = ""
        self.src_image_ext: str = ""
        self.path_to_images: str = f"{os.path.abspath(".")}{os.path.sep}images{os.path.sep}"
        # self.path_to_texts: str = f"{os.path.abspath(".")}{os.path.sep}texts{os.path.sep}"
        self.new_song: dict = {}
        self.title: str = ""
        self.genres: list[str] = []
        self.category: str = ""
        self.song_image: str = ""
        self.song_text: str = ""
        self.last_performed: str = ""
        self.is_recently: int = 0
        self.comment: str = ""

        self.do_connections()
        self.fill_in_genres()
        self.fill_in_categories()
        self.ui.le_song.setFocus()

    def do_connections(self):
        """ Do connections. """
        self.ui.btn_add_song.clicked.connect(
            self.btn_add_song_clicked)
        self.ui.btn_choose_image_file.clicked.connect(
            self.btn_choose_image_file_clicked)
        self.ui.btn_cancel.clicked.connect(self.close)

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
            self.ui.lw_genres.setCurrentRow(-1)

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
            self.ui.cb_categories.setCurrentIndex(-1)

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

        self.path_to_src_image = image_file_tuple[0]
        src_image_basename: str = os.path.basename(self.path_to_src_image)
        self.src_image_ext = src_image_basename.split(".")[-1:][0]
        # preview an image
        self.ui.lbl_song_image.setPixmap(QPixmap(self.path_to_src_image))

    def save_image(self, new_image_name: str) -> str:
        """ Save chosen image into images dir. """
        if self.path_to_src_image != "":
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
        else:
            return ""
        return path_to_dst_image
    
    @Slot()
    def btn_add_song_clicked(self) -> None:
        """ Save song into DB. """
        # Getting the song from le_song and check it.
        self.title = self.ui.le_song.text().strip()
        # replace ' to " if entered. For sql requests.
        if "'" in self.title:
            self.title = self.title.replace("'", '"')
        if self.title == "":
            QMessageBox.information(
                self,
                "Добавление песни",
                "Необходимо ввести название песни.")
            self.ui.le_song.setFocus()
        elif self.ui.lw_genres.currentRow() == -1:  # no one genre is chosen.
            QMessageBox.warning(
                self,
                "Добавление песни",
                "Выберите жанр(ы) в списке.")
        elif self.ui.cb_categories.currentIndex() == -1:  # no chosen category.
            QMessageBox.warning(
                self,
                "Добавление песни",
                "Выберите категорию.")
        else:
            try:
                # Create my_songbook INSTANCE and load data from the db.
                my_songbook: Songbook = Songbook()
                current_titles: list = my_songbook.get_titles_from_db()
            except DatabaseError:
                QMessageBox.critical(
                    self,
                    "Открытие базы данных",
                    "Ошибка при обращении к базе данных.")
            else:
                # to avoid duplicates of titles in the different case such
                # as Song_1 and song_1.
                is_song_exists: bool = False
                for current_title in current_titles:
                    if self.title.lower() == current_title.lower():
                        is_song_exists = True
                        break
                if is_song_exists:
                    QMessageBox.warning(
                        self,
                        "Добавление песни",
                        f"Песня '{self.title}' уже есть в базе данных.")
                    self.ui.le_song.setFocus()
                else:  # new_title is not in DB
                    # get other fields to add the song to DB.
                    for item in self.ui.lw_genres.selectedItems():
                        self.genres.append(item.text())

                    self.category = self.ui.cb_categories.currentText()
                    self.song_image = self.save_image(self.title)
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
                        my_songbook.insert_song_into_db(self.new_song)
                    except DatabaseError:
                        QMessageBox.critical(
                            self,
                            "Добавление песни",
                            "Ошибка при добавлении песни.")
                    else:
                        QMessageBox.information(
                            self,
                            "Добавление песни",
                            "Песня успешно добалена в песенник.")
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
