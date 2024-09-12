# -*- coding: utf-8 -*-
""" Dialog add categories """
from sqlite3 import DatabaseError
from PySide6.QtWidgets import (
    QDialog,
    QMessageBox,
)
from my_classes.songs import Songs
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
        # Getting the category from le_ and check it.
        category = self.ui.le_category.text().strip()
        # replace ' to " if entered. For sql requests.
        if "'" in category:
            category = category.replace("'", '"')
        if category == "":
            QMessageBox.information(
                self,
                "Добавление записи",
                "Необходимо ввести категорию.")
            self.ui.le_category.setFocus()
        else:  # add the category to the lw_adding_categiries
            # check if the adding category exists in the lw_adding_categiries.
            is_category_exists = False
            for i in range(total_categories):
                self.ui.lw_adding_categiries.setCurrentRow(i)
                if self.ui.lw_adding_categiries.currentItem().text() == category:
                    is_category_exists = True
                    QMessageBox.warning(
                        self,
                        "Добавление записи",
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
                "Добавление записи",
                "Нечего удалять.\nСписок добавляемых категорий пуст.")
            self.ui.le_category.setFocus()
        elif self.ui.lw_adding_categiries.currentRow() == -1:  #  or no selection.
            QMessageBox.warning(
                self,
                "Добавление записи",
                "Для удаления выберите категорию в списке.")
        else:  # not empty.
            for item in self.ui.lw_adding_categiries.selectedItems():
                self.ui.lw_adding_categiries.takeItem(
                    self.ui.lw_adding_categiries.row(item))
                # item = None

    def btn_finish_and_save_clicked(self):
        """ Save added categories into DB. """
        # Create my_songs INSTANCE and load data from the db.
        my_songs: Songs = Songs()
        try:  # open db and get dict.
            my_songs.open_db_and_get_dict()
            my_categories: list = my_songs.get_categories_from_db()
        except DatabaseError:
            QMessageBox.critical(
                self,
                "Открытие базы данных",
                "Ошибка при обращении к базе данных.")
        else:
            # Getting the category and check it.
            category = self.ui.le_category.text().strip()
            # replace ' to " if entered. For sql requests.
            if "'" in category:
                category = category.replace("'", '"')
            if category == "":
                QMessageBox.warning(
                    self,
                    "Добавление записи",
                    "Необходимо ввести категорию.")
                self.ui.le_category.setFocus()
            else:  # != ""
                # to avoid duplicates of categories in the different case such
                # as Category_1 and category_1.
                is_category_equal = False
                for category_db in my_categories:
                    if category.lower() == category_db.lower():
                        is_category_equal = True
                        break
                if is_category_equal:
                    QMessageBox.warning(
                        self,
                        "Добавление записи",
                        f"Категория '{category}' уже есть в базе данных.\n"
                        "Для редактирования нажмите 'Отмена'\nи"
                        " выберите в главном окне "
                        "'Редактировать категорию'.")
                else:  # category not in DB
                    categories = []  # list of adding categories to pass to the DB.
                    # Checking if the lw_adding_categiries is not empty.
                    total_categories = self.ui.lw_adding_categiries.count()
                    if total_categories == 0:
                        QMessageBox.warning(
                            self,
                            "Добавление записи",
                            "Список добавляемых категорий пуст.\n"
                            "Добавьте хотя бы одину категорию.")
                        self.ui.le_category.setFocus()
                    else:  # not empty.
                        for idx in range(total_categories):
                            categories.append(
                                self.ui.lw_adding_categiries.item(idx).text())
                        try:
                            my_songs.insert_categories_into_db(categories)
                        except DatabaseError:
                            QMessageBox.critical(
                                self,
                                "Добавление записи",
                                "Ошибка при добавлении записи.")
                        else:
                            QMessageBox.information(
                                self,
                                "Добавление записи",
                                "Категории успешно добалены в песенник.")
                            self.ui.lw_adding_categiries.clear()
                            self.ui.le_category.clear()
                            self.ui.le_category.setFocus()
