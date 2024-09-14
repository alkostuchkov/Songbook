# -*- coding: utf-8 -*-
""" Dialog add categories """
from sqlite3 import DatabaseError
from PySide6.QtWidgets import (
    QDialog,
    QMessageBox,
)
from my_classes.songbook import Songbook
from gui import dlg_add_categories_ui


class DlgAddCategory(QDialog):
    """ Class DlgAddCategory. """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = dlg_add_categories_ui.Ui_dlg_add_categories()
        self.ui.setupUi(self)

        self.do_connections()

    def do_connections(self):
        """ Do connections. """
        self.ui.btn_add_category_to_list.clicked.connect(
            self.btn_add_category_to_list_clicked
        )
        self.ui.btn_del_category_from_list.clicked.connect(
            self.btn_del_category_from_list_clicked
        )
        self.ui.btn_finish_and_save.clicked.connect(
            self.btn_finish_and_save_clicked
        )
        self.ui.btn_cancel.clicked.connect(self.close)

    def btn_add_category_to_list_clicked(self):
        """ Add category to list. """
        total_categories = self.ui.lw_adding_categiries.count()
        # Getting the category from le_category and check it.
        category = self.ui.le_category.text().strip()
        # replace ' to " if entered. For sql requests.
        if "'" in category:
            category = category.replace("'", '"')
        if category == "":
            QMessageBox.information(
                self,
                "Добавление категории",
                "Необходимо ввести категорию.")
            self.ui.le_category.setFocus()
        else:  # add the category to the lw_adding_categiries
            # check if the adding category exists in the lw_adding_categiries.
            is_category_exists = False
            for i in range(total_categories):
                self.ui.lw_adding_categiries.setCurrentRow(i)
                if (self.ui.lw_adding_categiries.currentItem().text().lower()
                        == category.lower()):
                    is_category_exists = True
                    QMessageBox.warning(
                        self,
                        "Добавление категории",
                        f"Категория '{category}' уже есть в списке.")
                    self.ui.le_category.setFocus()
                    break
            if not is_category_exists:
                self.ui.lw_adding_categiries.addItem(category)
                self.ui.lw_adding_categiries.clearSelection()
                self.ui.le_category.setFocus()

    def btn_del_category_from_list_clicked(self):
        """ Deleting a wrong category from lw_adding_categiries. """
        total_categories = self.ui.lw_adding_categiries.count()
        if total_categories == 0:  # lw_adding_categiries is empty.
            QMessageBox.warning(
                self,
                "Добавление категории",
                "Нечего удалять.\nСписок добавляемых категорий пуст.")
            self.ui.le_category.setFocus()
        elif self.ui.lw_adding_categiries.currentRow() == -1:  #  or no selection.
            QMessageBox.warning(
                self,
                "Добавление категории",
                "Для удаления выберите категорию в списке.")
        else:  # not empty.
            for item in self.ui.lw_adding_categiries.selectedItems():
                self.ui.lw_adding_categiries.takeItem(
                    self.ui.lw_adding_categiries.row(item))
                # item = None

    def btn_finish_and_save_clicked(self):
        """ Save added categories into DB. """
        # Create my_songbook INSTANCE and load data from the db.
        my_songbook: Songbook = Songbook()
        try:
            current_categories: list = my_songbook.get_categories_from_db()
        except DatabaseError:
            QMessageBox.critical(
                self,
                "Открытие базы данных",
                "Ошибка при обращении к базе данных.")
        else:
            new_categories: list[str] = []  # list of adding categories to pass to the DB.
            # Checking if the lw_adding_categiries is not empty.
            total_categories = self.ui.lw_adding_categiries.count()
            if total_categories == 0:
                QMessageBox.warning(
                    self,
                    "Добавление категории",
                    "Список добавляемых категорий пуст.\n"
                    "Добавьте хотя бы одину категорию.")
                self.ui.le_category.setFocus()
            else:  # not empty.
                for idx in range(total_categories):
                    new_categories.append(
                        self.ui.lw_adding_categiries.item(idx).text())
                # to avoid duplicates of categories in the different case such
                # as Category_1 and category_1.
                is_category_exists: bool = False
                checking_category: str = ""  # for QMessageBox
                for new_category in new_categories:
                    for current_category in current_categories:
                        if new_category.lower() == current_category.lower():
                            is_category_exists = True
                            checking_category = new_category
                            break
                    if is_category_exists:
                        break
                if is_category_exists:
                    QMessageBox.warning(
                        self,
                        "Добавление категории",
                        f"Категория '{checking_category}' уже есть в базе данных.")
                else:  # category not in DB
                    try:
                        my_songbook.insert_categories_into_db(new_categories)
                    except DatabaseError:
                        QMessageBox.critical(
                            self,
                            "Добавление категории",
                            "Ошибка при добавлении категории.")
                    else:
                        QMessageBox.information(
                            self,
                            "Добавление категории",
                            "Категории успешно добалены в песенник.")
                        self.ui.lw_adding_categiries.clear()
                        self.ui.le_category.clear()
                        self.ui.le_category.setFocus()
