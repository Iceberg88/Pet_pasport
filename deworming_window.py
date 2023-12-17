from PyQt6 import QtWidgets

import ectoparasites_design


class DewormingWindow(QtWidgets.QMainWindow, ectoparasites_design.Ui_ectoparasites_table_window):
    def exit(self):
        self.close()
        if self.error_label.text() != '':
            self.error_label.setText('')

    def delete_row(self):
        current_row = self.tableWidget_ectoparasites.currentRow()

        if current_row > -1:  # Если есть выделенная строка/элемент
            self.tableWidget_ectoparasites.removeRow(current_row)
            self.tableWidget_ectoparasites.selectionModel().clearCurrentIndex()

    def __init__(self):
        super().__init__()
        self.oldPos = None  # атрибут перемещения окна
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton_exit.clicked.connect(self.exit)
        self.tableWidget_ectoparasites.horizontalHeader().setSectionHidden(4, True)
