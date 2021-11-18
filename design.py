# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.Port = QtWidgets.QComboBox(Form)
        self.Port.setGeometry(QtCore.QRect(50, 30, 141, 32))
        self.Port.setObjectName("Port")
        self.Speed = QtWidgets.QComboBox(Form)
        self.Speed.setGeometry(QtCore.QRect(50, 100, 141, 32))
        self.Speed.setObjectName("Speed")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 10, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(170, 70, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.ConnectButton = QtWidgets.QPushButton(Form)
        self.ConnectButton.setGeometry(QtCore.QRect(210, 100, 125, 35))
        self.ConnectButton.setObjectName("ConnectButton")
        self.EnableBtn = QtWidgets.QPushButton(Form)
        self.EnableBtn.setGeometry(QtCore.QRect(100, 170, 100, 81))
        self.EnableBtn.setObjectName("EnableBtn")

        self.EnableBtn2 = QtWidgets.QPushButton(Form)
        self.EnableBtn2.setGeometry(QtCore.QRect(210, 170, 100, 81))
        self.EnableBtn2.setObjectName("EnableBtn2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Управление Arduino через ПК"))
        self.label.setText(_translate("Form", "Порт"))
        self.label_2.setText(_translate("Form", "Скорость"))
        self.ConnectButton.setText(_translate("Form", "Подключиться"))
        self.EnableBtn.setText(_translate("Form", "Включить"))
        self.EnableBtn2.setText(_translate("Form", "Выключить"))