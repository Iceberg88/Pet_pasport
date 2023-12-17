import random
import sqlite3
import string

from PIL import Image
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QFileDialog, QTableWidgetItem

import deworming_window
import ectoparasites_window
import new_record
import new_record_deworming
import new_record_ectoparasites
import new_record_othervac
import othervac_window
import pet01_design
import rabies_window


def path_photo():
    file_filter = 'Image File (*.png *.jpg)'
    image_path, _ = QFileDialog.getOpenFileName(filter=file_filter)

    return image_path


def generate_unique_id():
    characters = string.digits
    return ''.join([characters[random.randint(0, len(characters) - 1)] for _ in range(10)])


class MainInformation(QtWidgets.QMainWindow, pet01_design.Ui_MainWindow):

    def open_new_record(self):
        self.record.show()
        if not self.record.tableWidget_rabies_add.rowCount():
            self.record.tableWidget_rabies_add.insertRow(0)
            self.record.tableWidget_rabies_add.setItem(0, 0, QTableWidgetItem(''))

    def db_connect_rabies(self):
        self.db_connection = sqlite3.connect("data/database/Vaccines_rabies.db")
        self.db_cursor = self.db_connection.cursor()

    def create_db_rabies(self):
        self.db_connect_rabies()

        self.db_cursor.execute(f'''
                                CREATE TABLE IF NOT EXISTS {self.pet_name.text()} (
                                preparat TEXT NOT NULL,
                                date TEXT NOT NULL,
                                date_until TEXT NOT NULL,
                                number_serial TEXT NOT NULL,
                                doctor TEXT NOT NULL,
                                id INTEGER NOT NULL
                                )
                                ''')

        self.db_cursor.close()
        self.db_connection.close()

    def save_data_rabies(self):
        if self.record.tableWidget_rabies_add.item(0, 0).text() != '':

            self.record.error_label.setText('')
            self.db_connect_rabies()

            rows = self.record.tableWidget_rabies_add.rowCount()
            cols = self.record.tableWidget_rabies_add.columnCount()
            data = []
            for row in range(rows):
                tmp = []
                for col in range(cols):
                    try:
                        tmp.append(self.record.tableWidget_rabies_add.item(row, col).text())

                    except:
                        tmp.append('')
                data.append(tmp)
                data[0].append(generate_unique_id())

            self.db_cursor.executemany(
                f'INSERT INTO {self.pet_name.text()} (preparat, date, date_until, number_serial, '
                f'doctor, id) VALUES (?, ?, ?, ?, ?, ?)', data)

            self.db_connection.commit()
            self.record.tableWidget_rabies_add.setRowCount(0)  # очистка таблицы
            self.db_cursor.close()
            self.db_connection.close()
            self.record.exit()
            self.load_data_rabies()
            self.rabies.tableWidget_rabies.selectionModel().clearCurrentIndex()
        else:
            self.record.error_label.setText('Поле "Препарат" обязательно к заполнению')

    def load_data_rabies(self):
        self.db_connect_rabies()
        rowcount = self.db_cursor.execute(f'''SELECT COUNT(*) FROM {self.pet_name.text()}''').fetchone()[0]
        self.rabies.tableWidget_rabies.setRowCount(rowcount)
        self.db_cursor.execute(f'''SELECT * FROM {self.pet_name.text()}''')
        for row, form in enumerate(self.db_cursor):
            for column, item in enumerate(form):
                self.rabies.tableWidget_rabies.setItem(row, column, QTableWidgetItem(str(item)))

        self.db_cursor.close()
        self.db_connection.close()
        self.rabies.show()

    def delete_db_rabies(self):
        self.db_connect_rabies()

        if self.rabies.tableWidget_rabies.selectedIndexes():
            self.rabies.error_label.setText('')
            curr_row = self.rabies.tableWidget_rabies.currentRow()
            row = self.rabies.tableWidget_rabies.item(curr_row, 5).text()
            self.db_cursor.execute(f'DELETE FROM {self.pet_name.text()} WHERE id ="{row}"')

            self.db_connection.commit()
            self.db_cursor.close()
            self.db_connection.close()
        else:
            self.rabies.error_label.setText('Ошибка, ничего не выбрано')

    # __________________________сверху работа с бешенством__________________________


    def open_new_record_ecto(self):
        self.ecto_record.show()
        if not self.ecto_record.tableWidget_ectoparasites_add.rowCount():
            self.ecto_record.tableWidget_ectoparasites_add.insertRow(0)
            self.ecto_record.tableWidget_ectoparasites_add.setItem(0, 0, QTableWidgetItem(''))

    def db_connect_ecto(self):
        self.db_connection = sqlite3.connect("data/database/Vaccines_ectoparasites.db")
        self.db_cursor = self.db_connection.cursor()

    def create_db_ecto(self):
        self.db_connect_ecto()

        self.db_cursor.execute(f'''
                                CREATE TABLE IF NOT EXISTS {self.pet_name.text()} (
                                preparat TEXT NOT NULL,
                                date TEXT NOT NULL,
                                date_until TEXT NOT NULL,
                                doctor TEXT NOT NULL,
                                id INTEGER NOT NULL
                                )
                                ''')

        self.db_cursor.close()
        self.db_connection.close()

    def save_data_ecto(self):
        if self.ecto_record.tableWidget_ectoparasites_add.item(0, 0).text() != '':

            self.ecto_record.error_label.setText('')
            self.db_connect_ecto()

            rows = self.ecto_record.tableWidget_ectoparasites_add.rowCount()
            cols = self.ecto_record.tableWidget_ectoparasites_add.columnCount()
            data = []
            for row in range(rows):
                tmp = []
                for col in range(cols):
                    try:
                        tmp.append(self.ecto_record.tableWidget_ectoparasites_add.item(row, col).text())

                    except:
                        tmp.append('')
                data.append(tmp)
                data[0].append(generate_unique_id())

            self.db_cursor.executemany(f'INSERT INTO {self.pet_name.text()} (preparat, date, date_until, '
                                       f'doctor, id) VALUES (?, ?, ?, ?, ?)', data)

            self.db_connection.commit()
            self.ecto_record.tableWidget_ectoparasites_add.setRowCount(0)  # очистка таблицы
            self.db_cursor.close()
            self.db_connection.close()
            self.ecto_record.exit()
            self.load_data_ecto()
            self.ecto_record.tableWidget_ectoparasites_add.selectionModel().clearCurrentIndex()
        else:
            self.ecto_record.error_label.setText('Поле "Препарат" обязательно к заполнению')

    def load_data_ecto(self):
        self.db_connect_ecto()
        rowcount = self.db_cursor.execute(f'''SELECT COUNT(*) FROM {self.pet_name.text()}''').fetchone()[0]
        self.ecto.tableWidget_ectoparasites.setRowCount(rowcount)
        self.db_cursor.execute(f'''SELECT * FROM {self.pet_name.text()}''')
        for row, form in enumerate(self.db_cursor):
            for column, item in enumerate(form):
                self.ecto.tableWidget_ectoparasites.setItem(row, column, QTableWidgetItem(str(item)))

        self.db_cursor.close()
        self.db_connection.close()
        self.ecto.show()

    def delete_db_ecto(self):
        self.db_connect_ecto()

        if self.ecto.tableWidget_ectoparasites.selectedIndexes():
            self.ecto.error_label.setText('')
            curr_row = self.ecto.tableWidget_ectoparasites.currentRow()
            row = self.ecto.tableWidget_ectoparasites.item(curr_row, 4).text()
            self.db_cursor.execute(f'DELETE FROM {self.pet_name.text()} WHERE id ="{row}"')

            self.db_connection.commit()
            self.db_cursor.close()
            self.db_connection.close()
        else:
            self.ecto.error_label.setText('Ошибка, ничего не выбрано')

    # __________________________сверху работа с эктопаразитами__________________________


    def open_new_record_deworming(self):
        self.deworming_record.show()
        if not self.deworming_record.tableWidget_ectoparasites_add.rowCount():
            self.deworming_record.tableWidget_ectoparasites_add.insertRow(0)
            self.deworming_record.tableWidget_ectoparasites_add.setItem(0, 0, QTableWidgetItem(''))

    def db_connect_deworming(self):
        self.db_connection = sqlite3.connect("data/database/Vaccines_deworming.db")
        self.db_cursor = self.db_connection.cursor()

    def create_db_deworming(self):
        self.db_connect_deworming()

        self.db_cursor.execute(f'''
                                CREATE TABLE IF NOT EXISTS {self.pet_name.text()} (
                                preparat TEXT NOT NULL,
                                date TEXT NOT NULL,
                                date_until TEXT NOT NULL,
                                doctor TEXT NOT NULL,
                                id INTEGER NOT NULL
                                )
                                ''')

        self.db_cursor.close()
        self.db_connection.close()

    def save_data_deworming(self):
        if self.deworming_record.tableWidget_ectoparasites_add.item(0, 0).text() != '':

            self.deworming_record.error_label.setText('')
            self.db_connect_deworming()

            rows = self.deworming_record.tableWidget_ectoparasites_add.rowCount()
            cols = self.deworming_record.tableWidget_ectoparasites_add.columnCount()
            data = []
            for row in range(rows):
                tmp = []
                for col in range(cols):
                    try:
                        tmp.append(self.deworming_record.tableWidget_ectoparasites_add.item(row, col).text())

                    except:
                        tmp.append('')
                data.append(tmp)
                data[0].append(generate_unique_id())

            self.db_cursor.executemany(f'INSERT INTO {self.pet_name.text()} (preparat, date, date_until, '
                                       f'doctor, id) VALUES (?, ?, ?, ?, ?)', data)

            self.db_connection.commit()
            self.deworming_record.tableWidget_ectoparasites_add.setRowCount(0)  # очистка таблицы
            self.db_cursor.close()
            self.db_connection.close()
            self.deworming_record.exit()
            self.load_data_deworming()
            self.deworming_record.tableWidget_ectoparasites_add.selectionModel().clearCurrentIndex()
        else:
            self.deworming_record.error_label.setText('Поле "Препарат" обязательно к заполнению')

    def load_data_deworming(self):
        self.db_connect_deworming()
        rowcount = self.db_cursor.execute(f'''SELECT COUNT(*) FROM {self.pet_name.text()}''').fetchone()[0]
        self.deworming.tableWidget_ectoparasites.setRowCount(rowcount)
        self.db_cursor.execute(f'''SELECT * FROM {self.pet_name.text()}''')
        for row, form in enumerate(self.db_cursor):
            for column, item in enumerate(form):
                self.deworming.tableWidget_ectoparasites.setItem(row, column, QTableWidgetItem(str(item)))

        self.db_cursor.close()
        self.db_connection.close()
        self.deworming.name_table.setText('Вакцинация против глистов')
        self.deworming.show()

    def delete_db_deworming(self):
        self.db_connect_deworming()

        if self.deworming.tableWidget_ectoparasites.selectedIndexes():
            self.deworming.error_label.setText('')
            curr_row = self.deworming.tableWidget_ectoparasites.currentRow()
            row = self.deworming.tableWidget_ectoparasites.item(curr_row, 4).text()
            self.db_cursor.execute(f'DELETE FROM {self.pet_name.text()} WHERE id ="{row}"')

            self.db_connection.commit()
            self.db_cursor.close()
            self.db_connection.close()
        else:
            self.deworming.error_label.setText('Ошибка, ничего не выбрано')

    # __________________________сверху работа с глистами(дизайн от эктопаразитов)__________________________


    def open_new_record_other(self):
        self.other_record.show()
        if not self.other_record.tableWidget_ectoparasites_add.rowCount():
            self.other_record.tableWidget_ectoparasites_add.insertRow(0)
            self.other_record.tableWidget_ectoparasites_add.setItem(0, 0, QTableWidgetItem(''))

    def db_connect_other(self):
        self.db_connection = sqlite3.connect("data/database/Vaccines_other.db")
        self.db_cursor = self.db_connection.cursor()

    def create_db_other(self):
        self.db_connect_other()

        self.db_cursor.execute(f'''
                                CREATE TABLE IF NOT EXISTS {self.pet_name.text()} (
                                preparat TEXT NOT NULL,
                                date TEXT NOT NULL,
                                date_until TEXT NOT NULL,
                                doctor TEXT NOT NULL,
                                id INTEGER NOT NULL
                                )
                                ''')

        self.db_cursor.close()
        self.db_connection.close()

    def save_data_other(self):
        if self.other_record.tableWidget_ectoparasites_add.item(0, 0).text() != '':

            self.other_record.error_label.setText('')
            self.db_connect_other()

            rows = self.other_record.tableWidget_ectoparasites_add.rowCount()
            cols = self.other_record.tableWidget_ectoparasites_add.columnCount()
            data = []
            for row in range(rows):
                tmp = []
                for col in range(cols):
                    try:
                        tmp.append(self.other_record.tableWidget_ectoparasites_add.item(row, col).text())

                    except:
                        tmp.append('')
                data.append(tmp)
                data[0].append(generate_unique_id())

            self.db_cursor.executemany(f'INSERT INTO {self.pet_name.text()} (preparat, date, date_until, '
                                       f'doctor, id) VALUES (?, ?, ?, ?, ?)', data)

            self.db_connection.commit()
            self.other_record.tableWidget_ectoparasites_add.setRowCount(0)  # очистка таблицы
            self.db_cursor.close()
            self.db_connection.close()
            self.other_record.exit()
            self.load_data_other()
            self.other_record.tableWidget_ectoparasites_add.selectionModel().clearCurrentIndex()
        else:
            self.other_record.error_label.setText('Поле "Препарат" обязательно к заполнению')

    def load_data_other(self):
        self.db_connect_other()
        rowcount = self.db_cursor.execute(f'''SELECT COUNT(*) FROM {self.pet_name.text()}''').fetchone()[0]
        self.other.tableWidget_ectoparasites.setRowCount(rowcount)
        self.db_cursor.execute(f'''SELECT * FROM {self.pet_name.text()}''')
        for row, form in enumerate(self.db_cursor):
            for column, item in enumerate(form):
                self.other.tableWidget_ectoparasites.setItem(row, column, QTableWidgetItem(str(item)))

        self.db_cursor.close()
        self.db_connection.close()
        self.other.name_table.setText('Другие вакцинации')
        self.other.show()

    def delete_db_other(self):
        self.db_connect_other()

        if self.other.tableWidget_ectoparasites.selectedIndexes():
            self.other.error_label.setText('')
            curr_row = self.other.tableWidget_ectoparasites.currentRow()
            row = self.other.tableWidget_ectoparasites.item(curr_row, 4).text()
            self.db_cursor.execute(f'DELETE FROM {self.pet_name.text()} WHERE id ="{row}"')

            self.db_connection.commit()
            self.db_cursor.close()
            self.db_connection.close()
        else:
            self.other.error_label.setText('Ошибка, ничего не выбрано')

    # __________________________сверху работа с другими вакцинациями(дизайн от эктопаразитов)__________________________

    def open_photo(self):  # Функция для переворота изображения по данным из EXIF
        image_path = path_photo()
        if image_path == '':
            return
        image = Image.open(image_path)
        exif_data = image.getexif()
        orientation = 1

        if exif_data:
            orientation = exif_data.get(0x112, 1)
        if orientation in (2, 4, 5, 7):
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
        if orientation in (3, 4):
            image = image.transpose(Image.ROTATE_180)
        if orientation in (5, 6):
            image = image.transpose(Image.ROTATE_270)
        if orientation in (7, 8):
            image = image.transpose(Image.ROTATE_90)
        image.save(image_path)

        pixmap = QPixmap(image_path).scaled(2000, 2000, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
        self.label.setPixmap(pixmap)

        text16 = image_path
        self.db_connection = sqlite3.connect("data/database/PetPassport.db")
        self.db_cursor = self.db_connection.cursor()

        self.db_cursor.execute(
            f'UPDATE {self.pet_name.text()} SET path_photo = "{text16}" WHERE path_photo != "{text16}"')

        self.db_connection.commit()

        self.db_cursor.close()
        self.db_connection.close()

    def __init__(self):
        super().__init__()
        self.oldPos = None  # атрибут перемещения окна
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.rabies = rabies_window.RabiesWindow()
        self.record = new_record.NewRecord()

        self.ecto = ectoparasites_window.EctoparasitesWindow()
        self.ecto_record = new_record_ectoparasites.NewRecordEcto()

        self.deworming = deworming_window.DewormingWindow()
        self.deworming_record = new_record_deworming.NewRecordDeworming()

        self.other = othervac_window.OtherWindow()
        self.other_record = new_record_othervac.NewRecordOther()

        self.add_photo_button.clicked.connect(self.open_photo)

        self.rabies.pushButton_add.clicked.connect(self.open_new_record)
        self.beshenstvo_button.clicked.connect(self.create_db_rabies)
        self.beshenstvo_button.clicked.connect(self.load_data_rabies)
        self.record.pushButton_save_add.clicked.connect(self.save_data_rabies)
        self.rabies.pushButton_delete.clicked.connect(self.delete_db_rabies)
        self.rabies.pushButton_delete.clicked.connect(self.rabies.delete_row)

        self.ecto.pushButton_add.clicked.connect(self.open_new_record_ecto)
        self.paraziti_button.clicked.connect(self.create_db_ecto)
        self.paraziti_button.clicked.connect(self.load_data_ecto)
        self.ecto_record.pushButton_save_add.clicked.connect(self.save_data_ecto)
        self.ecto.pushButton_delete.clicked.connect(self.delete_db_ecto)
        self.ecto.pushButton_delete.clicked.connect(self.ecto.delete_row)

        self.deworming.pushButton_add.clicked.connect(self.open_new_record_deworming)
        self.glisti_button.clicked.connect(self.create_db_deworming)
        self.glisti_button.clicked.connect(self.load_data_deworming)
        self.deworming_record.pushButton_save_add.clicked.connect(self.save_data_deworming)
        self.deworming.pushButton_delete.clicked.connect(self.delete_db_deworming)
        self.deworming.pushButton_delete.clicked.connect(self.deworming.delete_row)

        self.other.pushButton_add.clicked.connect(self.open_new_record_other)
        self.other_vakcin_button.clicked.connect(self.create_db_other)
        self.other_vakcin_button.clicked.connect(self.load_data_other)
        self.other_record.pushButton_save_add.clicked.connect(self.save_data_other)
        self.other.pushButton_delete.clicked.connect(self.delete_db_other)
        self.other.pushButton_delete.clicked.connect(self.other.delete_row)
