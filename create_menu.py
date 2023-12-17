from PyQt6 import QtWidgets

import pet_create_design


class CreateMenu(QtWidgets.QMainWindow, pet_create_design.Ui_Dialog_create_new_pet):

    def cancel_hide(self):
        self.close()

    def __init__(self):
        super().__init__()
        self.oldPos = None  # атрибут перемещения окна
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.cancel_save_button.clicked.connect(self.cancel_hide)
