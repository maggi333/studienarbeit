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
        Dialog.resize(533, 330)
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
        self.pingLabel.setGeometry(QtCore.QRect(180, 250, 67, 17))
        self.pingLabel.setObjectName("pingLabel")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(220, 50, 113, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 80, 113, 27))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 110, 113, 27))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(220, 140, 113, 27))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(110, 50, 91, 17))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 80, 111, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(110, 110, 91, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(110, 140, 91, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(340, 50, 41, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(340, 80, 16, 17))
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 210, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 190, 541, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 250, 171, 17))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(270, 250, 171, 17))
        self.label_8.setObjectName("label_8")
        self.msg_lostLabel = QtWidgets.QLabel(Dialog)
        self.msg_lostLabel.setGeometry(QtCore.QRect(430, 250, 67, 17))
        self.msg_lostLabel.setObjectName("msg_lostLabel")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(10, 270, 171, 17))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(10, 290, 171, 17))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(10, 310, 171, 17))
        self.label_11.setObjectName("label_11")
        self.minLabel = QtWidgets.QLabel(Dialog)
        self.minLabel.setGeometry(QtCore.QRect(180, 270, 67, 17))
        self.minLabel.setObjectName("minLabel")
        self.maxLabel = QtWidgets.QLabel(Dialog)
        self.maxLabel.setGeometry(QtCore.QRect(180, 290, 67, 17))
        self.maxLabel.setObjectName("maxLabel")
        self.standardLabel = QtWidgets.QLabel(Dialog)
        self.standardLabel.setGeometry(QtCore.QRect(180, 310, 67, 17))
        self.standardLabel.setObjectName("standardLabel")
        self.extra_clientCheckBox = QtWidgets.QCheckBox(Dialog)
        self.extra_clientCheckBox.setGeometry(QtCore.QRect(110, 170, 111, 22))
        self.extra_clientCheckBox.setObjectName("extra_clientCheckBox")

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
        self.label_1.setText(_translate("Dialog", "Packetgröße:"))
        self.label_2.setText(_translate("Dialog", "Sendeintervall:"))
        self.label_3.setText(_translate("Dialog", "Anzahl:"))
        self.label_4.setText(_translate("Dialog", "QoS (MQTT):"))
        self.label_5.setText(_translate("Dialog", "bytes"))
        self.label_6.setText(_translate("Dialog", "s"))
        self.label.setText(_translate("Dialog", "Auswertung"))
        self.label_7.setText(_translate("Dialog", "Durschsnittliche Latenz:"))
        self.label_8.setText(_translate("Dialog", "Nachrichten Verlust:"))
        self.msg_lostLabel.setText(_translate("Dialog", "TextLabel"))
        self.label_9.setText(_translate("Dialog", "Minium Latenz:"))
        self.label_10.setText(_translate("Dialog", "Maximum Latenz:"))
        self.label_11.setText(_translate("Dialog", "Standardabweichung:"))
        self.minLabel.setText(_translate("Dialog", "TextLabel"))
        self.maxLabel.setText(_translate("Dialog", "TextLabel"))
        self.standardLabel.setText(_translate("Dialog", "TextLabel"))
        self.extra_clientCheckBox.setText(_translate("Dialog", "Extra Client"))

