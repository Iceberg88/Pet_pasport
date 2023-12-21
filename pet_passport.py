# Декстопное ГУИ приложение для контроля за питомцами начал примерно 01.11.2023
import os
import sqlite3
import sys

from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

import create_menu
import main_information
import pet_choice_design


def create_folders(folders):
    for folder in folders:
        path = os.path.join(os.getcwd(), folder)
        if not os.path.exists(path):
            os.makedirs(path)


folders_to_create = ['C:/ProgramData/Pet passport/data',
                     'C:/ProgramData/Pet passport/data/images',
                     'C:/ProgramData/Pet passport/data/database']
create_folders(folders_to_create)


class PetApp(QtWidgets.QMainWindow, pet_choice_design.Ui_Dialog_choice):

    def open_window_create(self):
        self.w.show()

    def open_main_information_window(self):
        self.m_i.show()

    def check_used_name(self):
        items = []
        items_text = []
        for index in range(self.listWidget.count()):
            items.append(self.listWidget.item(index))
        for item in items:
            items_text.append(item.text())
        return items_text

    def save_choice_name(self):
        if self.w.lineEdit_pet_name.text() in self.check_used_name():
            self.w.error_label.setText('Упс, такая кличка уже в базе')
        else:
            if self.w.lineEdit_pet_name.text() != '':
                self.w.error_label.setText('')
                self.pet_name = self.w.lineEdit_pet_name.text()
                self.pet_vid = self.w.lineEdit_pet_type.text()
                self.listWidget.addItem(self.pet_name)
                self.w.close()
                self.listWidget.clearSelection()
            else:
                self.w.error_label.setText('Ошибка, кличка питомца обязательна')

    def db_connect(self):
        self.db_connection = sqlite3.connect("C:/ProgramData/Pet passport/data/database/PetPassport.db")
        self.db_cursor = self.db_connection.cursor()

    def clean_after_close(self):
        if self.w.isActiveWindow():
            pass
        else:
            self.w.lineEdit_fio_vladeltsa.clear()
            self.w.lineEdit_adres_vladeltsa.clear()
            self.w.lineEdit_nomer_vladeltsa.clear()
            self.w.lineEdit_pet_name.clear()
            self.w.lineEdit_pet_type.clear()
            self.w.lineEdit_pet_poroda.clear()
            self.w.lineEdit_pet_color.clear()
            self.w.lineEdit_pet_birthday.clear()
            self.w.lineEdit_pet_sex.clear()
            self.w.lineEdit_chip_number.clear()
            self.w.lineEdit_chip_date.clear()
            self.w.lineEdit_chip_place.clear()
            self.w.lineEdit_kleymo_nomer.clear()
            self.w.lineEdit_kleymo_date.clear()
            self.w.lineEdit_special_mark.clear()

    def create_db(self):
        self.db_connect()

        self.db_cursor.execute(f'''
                                CREATE TABLE IF NOT EXISTS {self.pet_name} (
                                fio_vladeltsa TEXT NOT NULL,
                                adres_vladeltsa TEXT NOT NULL,
                                nomer_vladeltsa TEXT NOT NULL,
                                pet_name TEXT NOT NULL UNIQUE,
                                pet_type TEXT NOT NULL,
                                pet_poroda TEXT NOT NULL,
                                pet_color TEXT NOT NULL,
                                pet_birthday TEXT NOT NULL,
                                pet_sex TEXT NOT NULL,
                                chip_number TEXT NOT NULL,
                                chip_date TEXT NOT NULL,
                                chip_place TEXT NOT NULL,
                                kleymo_nomer TEXT NOT NULL,
                                kleymo_date TEXT NOT NULL,
                                special_mark TEXT NOT NULL,
                                path_photo TEXT NOT NULL
                                )
                                ''')
        self.db_connection.commit()
        self.db_cursor.close()
        self.db_connection.close()

    def save_db_data(self):
        self.db_connect()
        if self.w.lineEdit_pet_name.text() != '':
            text1 = self.w.lineEdit_fio_vladeltsa.text()
            text2 = self.w.lineEdit_adres_vladeltsa.text()
            text3 = self.w.lineEdit_nomer_vladeltsa.text()
            text4 = self.w.lineEdit_pet_name.text()
            text5 = self.w.lineEdit_pet_type.text()
            text6 = self.w.lineEdit_pet_poroda.text()
            text7 = self.w.lineEdit_pet_color.text()
            text8 = self.w.lineEdit_pet_birthday.text()
            text9 = self.w.lineEdit_pet_sex.text()
            text10 = self.w.lineEdit_chip_number.text()
            text11 = self.w.lineEdit_chip_date.text()
            text12 = self.w.lineEdit_chip_place.text()
            text13 = self.w.lineEdit_kleymo_nomer.text()
            text14 = self.w.lineEdit_kleymo_date.text()
            text15 = self.w.lineEdit_special_mark.text()
            text16 = 's'

            try:
                self.db_cursor.execute(f'INSERT INTO {self.pet_name} (fio_vladeltsa,\
                                        adres_vladeltsa,\
                                        nomer_vladeltsa,\
                                        pet_name,\
                                        pet_type,\
                                        pet_poroda,\
                                        pet_color,\
                                        pet_birthday,\
                                        pet_sex,\
                                        chip_number,\
                                        chip_date,\
                                        chip_place,\
                                        kleymo_nomer,\
                                        kleymo_date,\
                                        special_mark,\
                                        path_photo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                       (f'{text1}', f'{text2}', f'{text3}', f'{text4}', f'{text5}', f'{text6}', f'{text7}',
                                        f'{text8}', f'{text9}', f'{text10}', f'{text11}', f'{text12}', f'{text13}',
                                        f'{text14}',
                                        f'{text15}', f'{text16}',))

                self.db_connection.commit()
            except sqlite3.IntegrityError:   # Обработка ошибки при создании уникального имени
                pass
            finally:
                self.clean_after_close()
                self.db_cursor.close()
                self.db_connection.close()

    def load_pet_db(self):
        if self.listWidget.selectedIndexes():
            self.error_label.setText('')
            self.db_connect()
            self.db_cursor.execute(f"SELECT * FROM {self.listWidget.currentItem().text()}")
            data = self.db_cursor.fetchall()

            for task in data:
                self.m_i.fio_vladeltsa.setText(task[0])
                self.m_i.adres_vladeltsa.setText(task[1])
                self.m_i.nomer_vladeltsa.setText(task[2])
                self.m_i.pet_name.setText(task[3])
                self.m_i.pet_type.setText(task[4])
                self.m_i.pet_poroda.setText(task[5])
                self.m_i.pet_color.setText(task[6])
                self.m_i.pet_birthday.setText(task[7])
                self.m_i.pet_sex.setText(task[8])
                self.m_i.chip_number.setText(task[9])
                self.m_i.chip_date.setText(task[10])
                self.m_i.chip_place.setText(task[11])
                self.m_i.kleymo_nomer.setText(task[12])
                self.m_i.kleymo_date.setText(task[13])
                self.m_i.special_mark.setText(task[14])
                if task[15] == 's':
                    if os.path.isfile("C:/ProgramData/Pet passport/data/images/no_photo.png"):
                        self.m_i.label.setPixmap(QPixmap("C:/ProgramData/Pet passport/data/images/no_photo.png"))
                    else:
                        self.m_i.label.setText('            Изображение не найдено')
                else:
                    pixmap = QPixmap(f'{task[15]}').scaled(2000, 2000,
                                                           aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
                    self.m_i.label.setPixmap(pixmap)
                self.m_i.show()
                self.close()

                self.db_cursor.close()
                self.db_connection.close()
        else:
            self.error_label.setText('Ошибка, не выбран питомец')

    def save_all_names(self):  # Функция для создания файла со списком имен, который появляется при старте в listwidget
        items = []
        items_text = []
        for index in range(self.listWidget.count()):
            items.append(self.listWidget.item(index))
        for item in items:
            items_text.append(item.text())
        with open("C:/ProgramData/Pet passport/data/database/All_pets.txt", "w") as file:
            for i in items_text:
                file.write(i + '\n')

    def delete_pet(self):
        if self.listWidget.selectedIndexes():
            self.error_label.setText('')
            current_name = self.listWidget.currentItem().text()
            self.db_connection = sqlite3.connect("C:/ProgramData/Pet passport/data/database/PetPassport.db")
            self.db_cursor = self.db_connection.cursor()

            self.db_cursor.execute(f'DROP TABLE IF EXISTS {current_name}')

            self.db_connection.commit()
            self.db_cursor.close()
            self.db_connection.close()
            ###########################################################################

            self.db_connection2 = sqlite3.connect("C:/ProgramData/Pet passport/data/database/Vaccines_rabies.db")
            self.db_cursor2 = self.db_connection2.cursor()

            self.db_cursor2.execute(f'DROP TABLE IF EXISTS {current_name}')

            self.db_connection2.commit()
            self.db_cursor2.close()
            self.db_connection2.close()
            ###########################################################################

            self.db_connection3 = sqlite3.connect("C:/ProgramData/Pet passport/data/database/Vaccines_ectoparasites.db")
            self.db_cursor3 = self.db_connection3.cursor()

            self.db_cursor3.execute(f'DROP TABLE IF EXISTS {current_name}')

            self.db_connection3.commit()
            self.db_cursor3.close()
            self.db_connection3.close()
            ###########################################################################

            self.db_connection4 = sqlite3.connect("C:/ProgramData/Pet passport/data/database/Vaccines_deworming.db")
            self.db_cursor4 = self.db_connection4.cursor()

            self.db_cursor4.execute(f'DROP TABLE IF EXISTS {current_name}')

            self.db_connection4.commit()
            self.db_cursor4.close()
            self.db_connection4.close()
            ###########################################################################

            self.db_connection5 = sqlite3.connect("C:/ProgramData/Pet passport/data/database/Vaccines_other.db")
            self.db_cursor5 = self.db_connection5.cursor()

            self.db_cursor5.execute(f'DROP TABLE IF EXISTS {current_name}')

            self.db_connection5.commit()
            self.db_cursor5.close()
            self.db_connection5.close()
            ###########################################################################

            filename = "C:/ProgramData/Pet passport/data/database/All_pets.txt"  # Читает из файла все имена чтобы удалить выбранный
            if self.listWidget.selectedIndexes():
                if os.path.isfile(filename):
                    with open(filename, 'r') as file:
                        data = file.readlines()
                        new_data = []
                        for item in data:
                            item = item.replace('\n', '')
                            new_data.append(item)
                        for i, line in enumerate(new_data):
                            if line == current_name:
                                del data[i]
                                break

                    with open(filename, 'w') as file:
                        file.writelines(data)
            ###########################################################################

            index = self.listWidget.currentIndex()
            if self.listWidget.selectedIndexes():
                if index.isValid():
                    self.listWidget.takeItem(index.row())
                    self.listWidget.clearSelection()
        else:
            self.error_label.setText('Ошибка, не выбран питомец')

    def toolbar_action(self):
        self.m_i.close()
        self.show()

    def __init__(self):
        super(PetApp, self).__init__()
        self.pet_name = None
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        filename = "C:/ProgramData/Pet passport/data/database/All_pets.txt"  # Читает из файла все имена чтобы их выбрать потом
        if os.path.isfile(filename):
            with open(filename, 'r') as file:
                for i in file:
                    self.listWidget.addItem(i.strip())

        self.w = create_menu.CreateMenu()
        self.m_i = main_information.MainInformation()
        self.oldPos = None  # атрибут перемещения окна

        self.create_pet_button.clicked.connect(self.open_window_create)
        self.select_pet_button.clicked.connect(self.load_pet_db)
        self.delete_pet_button.clicked.connect(self.delete_pet)
        self.w.save_pet_button.clicked.connect(self.save_choice_name)
        self.w.save_pet_button.clicked.connect(self.create_db)
        self.w.save_pet_button.clicked.connect(self.save_db_data)
        self.w.save_pet_button.clicked.connect(self.save_all_names)

        toolbar = self.m_i.toolBar.addAction('Сменить питомца')
        toolbar.triggered.connect(self.toolbar_action)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = PetApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
