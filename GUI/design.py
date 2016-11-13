# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(533, 298)
        self.startButton = QtWidgets.QPushButton(Dialog)
        self.startButton.setGeometry(QtCore.QRect(390, 40, 99, 27))
        self.startButton.setObjectName("startButton")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(380, 90, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.stopButton = QtWidgets.QPushButton(Dialog)
        self.stopButton.setGeometry(QtCore.QRect(390, 140, 99, 27))
        self.stopButton.setObjectName("stopButton")
        self.mqttButton = QtWidgets.QRadioButton(Dialog)
        self.mqttButton.setGeometry(QtCore.QRect(10, 50, 117, 22))
        self.mqttButton.setObjectName("mqttButton")
        self.coapButton = QtWidgets.QRadioButton(Dialog)
        self.coapButton.setGeometry(QtCore.QRect(10, 80, 117, 22))
        self.coapButton.setObjectName("coapButton")
        self.pingLabel = QtWidgets.QLabel(Dialog)
        self.pingLabel.setGeometry(QtCore.QRect(440, 200, 67, 17))
        self.pingLabel.setObjectName("pingLabel")
        self.testList = QtWidgets.QListWidget(Dialog)
        self.testList.setGeometry(QtCore.QRect(100, 30, 256, 192))
        self.testList.setObjectName("testList")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(370, 200, 67, 17))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.startButton.setText(_translate("Dialog", "Start Test"))
        self.stopButton.setText(_translate("Dialog", "Stop"))
        self.mqttButton.setText(_translate("Dialog", "MQTT"))
        self.coapButton.setText(_translate("Dialog", "CoAP"))
        self.pingLabel.setText(_translate("Dialog", "TextLabel"))
        self.label.setText(_translate("Dialog", "Ping:"))

