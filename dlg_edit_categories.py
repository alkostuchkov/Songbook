# -*- coding: utf-8 -*-
""" Dialog edit categories """
from sqlite3 import DatabaseError
from PySide6.QtWidgets import (
    QDialog,
    QMessageBox,
)
from PySide6.QtCore import Slot
from my_classes.songbook import Songbook
from gui import dlg_edit_categories_ui


class DlgEditCategory(QDialog):
    """ Class DlgEditCategory. """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = dlg_edit_categories_ui.Ui_dlg_edit_categories()
        self.ui.setupUi(self)

        # for updating category in the DB.
        # for reason to get acces to its from all methods.
        self._current_category: str = ""

        self._do_connections()

    def _do_connections(self):
        """ Do connections. """
        self.ui.btn_finish_and_save.clicked.connect(
            self.btn_finish_and_save_clicked
        )
        self.ui.btn_cancel.clicked.connect(self.close)

    @Slot(str)
    def get_current_category(self, current_category):
        """
        Slot to get current_category and fill in le_category
        from Signal edit_category_called in main.py.
        """
        self.ui.le_category.setText(current_category)
        self._current_category = current_category

    def btn_finish_and_save_clicked(self):
        """ Save added categories into DB. """
        new_category: str = self.ui.le_category.text().strip()
        # replace ' to " if entered. For sql requests.
        if "'" in new_category:
            new_category = new_category.replace("'", '"')
        if new_category == "":
            QMessageBox.warning(
                self,
                "Редактирование категории",
                "Необходимо ввести категорию.")
            self.ui.le_category.setFocus()
        # check if the category was changed.
        elif new_category == self._current_category:
            QMessageBox.information(
                self,
                "Редактирование категории",
                "Название категории не именилось.")
            self.ui.le_category.setFocus()
        else:  # new_category != current_category
            try:  # Create my_songbook INSTANCE and load data from the db.
                my_songbook: Songbook = Songbook()
                current_categories: list = my_songbook.get_categories_from_db()
            except DatabaseError:
                QMessageBox.critical(
                    self,
                    "Открытие базы данных",
                    "Ошибка при обращении к базе данных.")
            else:
                # to avoid duplicates of categories in the different case such
                # as Category_1 and category_1.
                is_category_exists: bool = False
                checking_category: str = ""  # for QMessageBox
                for current_category in current_categories:
                    if new_category.lower() == current_category.lower():
                        is_category_exists = True
                        checking_category = new_category
                        break
                if is_category_exists:
                    QMessageBox.warning(
                        self,
                        "Редактирование категории",
                        f"Категория '{checking_category}' уже есть в базе данных.")
                else:  # category is not in DB
                    try:
                        my_songbook.update_categories(
                            self._current_category, new_category)
                    except DatabaseError:
                        QMessageBox.critical(
                            self,
                            "Редактирование категории",
                            "Ошибка при добавлении категории.")
                    else:
                        QMessageBox.information(
                            self,
                            "Редактирование категории",
                            "Категория успешно отредактирована.")
                        self.ui.le_category.clear()
                        self.close()
