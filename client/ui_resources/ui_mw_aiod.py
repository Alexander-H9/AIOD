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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(230, 40, 161, 60))
        self.pushButton.setStyleSheet(u"font: 20px;")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(40, 40, 120, 60))
        self.pushButton_2.setStyleSheet(u"font: 20px;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 120, 161, 41))
        self.label.setStyleSheet(u"font: 15px;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(260, 390, 261, 71))
        self.label_2.setStyleSheet(u"font: 20px;")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(420, 40, 241, 60))
        self.comboBox.setStyleSheet(u"font: 20px;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Select file", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Filename.jpg", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Detected: 99% Basketball", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Objekterkennung", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Texterkennung", None))

    # retranslateUi

