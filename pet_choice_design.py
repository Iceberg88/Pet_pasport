# Form implementation generated from reading ui file 'pet_choice01.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtWidgets


class Ui_Dialog_choice(object):
    def setupUi(self, Dialog_choice):
        Dialog_choice.setObjectName("Dialog_choice")
        Dialog_choice.resize(400, 300)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Dialog_choice)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(parent=self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=Dialog_choice)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(90, 250, 163, 26))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.formLayout = QtWidgets.QFormLayout(self.verticalLayoutWidget_2)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.create_pet_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.create_pet_button.setObjectName("create_pet_button")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.create_pet_button)
        self.select_pet_button = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.select_pet_button.setObjectName("select_pet_button")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.select_pet_button)
        self.delete_pet_button = QtWidgets.QPushButton(parent=Dialog_choice)
        self.delete_pet_button.setGeometry(QtCore.QRect(310, 250, 75, 24))
        self.delete_pet_button.setObjectName("delete_pet_button")
        self.error_label = QtWidgets.QLabel(parent=Dialog_choice)
        self.error_label.setGeometry(QtCore.QRect(20, 220, 351, 16))
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")

        self.retranslateUi(Dialog_choice)
        QtCore.QMetaObject.connectSlotsByName(Dialog_choice)

    def retranslateUi(self, Dialog_choice):
        _translate = QtCore.QCoreApplication.translate
        Dialog_choice.setWindowTitle(_translate("Dialog_choice", "Выбор питомца"))
        self.create_pet_button.setText(_translate("Dialog_choice", "Создать..."))
        self.select_pet_button.setText(_translate("Dialog_choice", "Выбрать"))
        self.delete_pet_button.setText(_translate("Dialog_choice", "Удалить"))
