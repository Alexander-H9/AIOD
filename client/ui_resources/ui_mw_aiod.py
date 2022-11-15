# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mw_aiod.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(720, 480)
        MainWindow.setStyleSheet(u"background-color: #000000;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pb_upload = QPushButton(self.centralwidget)
        self.pb_upload.setObjectName(u"pb_upload")
        self.pb_upload.setGeometry(QRect(230, 40, 160, 60))
        self.pb_upload.setStyleSheet(u"font: 20px;\n"
"border: 1px solid #999999;\n"
"color: #ffffff;\n"
"border-radius: 3px;")
        self.pb_select = QPushButton(self.centralwidget)
        self.pb_select.setObjectName(u"pb_select")
        self.pb_select.setGeometry(QRect(40, 40, 160, 60))
        self.pb_select.setStyleSheet(u"font: 20px;\n"
"border: 1px solid #999999;\n"
"color: #ffffff;\n"
"border-radius: 3px;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 120, 161, 41))
        self.label.setStyleSheet(u"font: 15px;\n"
"color: #ffffff;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 410, 720, 70))
        self.label_2.setStyleSheet(u"font: 20px;\n"
"color: #ffffff;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(420, 40, 241, 60))
        self.comboBox.setStyleSheet(u"font: 20px;\n"
"color: #ffffff;")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 410, 720, 2))
        self.line.setStyleSheet(u"border: 5px solid #666666;")
        self.line.setLineWidth(0)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AIOD", None))
        self.pb_upload.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.pb_select.setText(QCoreApplication.translate("MainWindow", u"Select file", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Filename.jpg", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"99% Objekt", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Objekterkennung", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Texterkennung", None))

    # retranslateUi

