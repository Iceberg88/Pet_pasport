from PyQt6 import QtWidgets

import rabies_design


class RabiesWindow(QtWidgets.QMainWindow, rabies_design.Ui_rabies_table_window):
    def exit(self):
        self.close()
        if self.error_label.text() != '':
            self.error_label.setText('')

    def delete_row(self):
        current_row = self.tableWidget_rabies.currentRow()

        if current_row > -1:  # Если есть выделенная строка/элемент
            self.tableWidget_rabies.removeRow(current_row)
            self.tableWidget_rabies.selectionModel().clearCurrentIndex()

    def __init__(self):
        super().__init__()
        self.oldPos = None  # атрибут перемещения окна
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton_exit.clicked.connect(self.exit)
        self.tableWidget_rabies.horizontalHeader().setSectionHidden(5, True)
