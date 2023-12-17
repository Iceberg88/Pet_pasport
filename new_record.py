from PyQt6 import QtWidgets

import new_record_design


class NewRecord(QtWidgets.QMainWindow, new_record_design.Ui_record_rabies):

    def exit(self):
        self.close()
        self.error_label.setText('')

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_cancel_add.clicked.connect(self.exit)
