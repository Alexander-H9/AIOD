# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg_login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(360, 720)
        Dialog.setStyleSheet(u"background-color: #000000;")
        self.le_user = QLineEdit(Dialog)
        self.le_user.setObjectName(u"le_user")
        self.le_user.setGeometry(QRect(89, 220, 241, 50))
        self.le_user.setStyleSheet(u"font: 20px;\n"
"color: #ffffff;\n"
"border: none;")
        self.le_user.setMaxLength(32)
        self.le_pw = QLineEdit(Dialog)
        self.le_pw.setObjectName(u"le_pw")
        self.le_pw.setGeometry(QRect(90, 400, 240, 50))
        self.le_pw.setStyleSheet(u"font: 20px;\n"
"color: #ffffff;\n"
"border: none;")
        self.le_pw.setMaxLength(32)
        self.le_pw.setEchoMode(QLineEdit.Password)
        self.pb_submit = QPushButton(Dialog)
        self.pb_submit.setObjectName(u"pb_submit")
        self.pb_submit.setGeometry(QRect(30, 510, 300, 60))
        self.pb_submit.setStyleSheet(u"font: 20px;\n"
"border: 1px solid #999999;\n"
"color: #ffffff;\n"
"border-radius: 3px;")
        self.label_user = QLabel(Dialog)
        self.label_user.setObjectName(u"label_user")
        self.label_user.setGeometry(QRect(30, 220, 50, 50))
        self.label_user.setScaledContents(True)
        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(30, 280, 300, 2))
        self.line.setStyleSheet(u"border: 5px solid #666666;")
        self.line.setLineWidth(0)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(Dialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(30, 460, 300, 2))
        self.line_2.setStyleSheet(u"border: 5px solid #666666;")
        self.line_2.setLineWidth(0)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label_pw = QLabel(Dialog)
        self.label_pw.setObjectName(u"label_pw")
        self.label_pw.setGeometry(QRect(30, 400, 50, 50))
        self.label_pw.setScaledContents(True)
        self.line_3 = QFrame(Dialog)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(30, 370, 300, 2))
        self.line_3.setStyleSheet(u"border: 5px solid #666666;")
        self.line_3.setLineWidth(0)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.label_mail = QLabel(Dialog)
        self.label_mail.setObjectName(u"label_mail")
        self.label_mail.setGeometry(QRect(30, 310, 50, 50))
        self.label_mail.setScaledContents(True)
        self.le_mail = QLineEdit(Dialog)
        self.le_mail.setObjectName(u"le_mail")
        self.le_mail.setGeometry(QRect(90, 310, 240, 50))
        self.le_mail.setStyleSheet(u"font: 20px;\n"
"color: #ffffff;\n"
"border: none;")
        self.le_mail.setMaxLength(32)
        self.le_mail.setEchoMode(QLineEdit.Normal)
        self.label_logo = QLabel(Dialog)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setGeometry(QRect(120, 60, 120, 120))
        self.label_logo.setScaledContents(True)
        self.pb_close = QPushButton(Dialog)
        self.pb_close.setObjectName(u"pb_close")
        self.pb_close.setGeometry(QRect(320, 0, 40, 30))
        self.pb_close.setStyleSheet(u"border: 1px solid #999999;\n"
"font: 20px;\n"
"color: #ffffff;\n"
"border-radius: 3px;")
        self.pb_eyes = QPushButton(Dialog)
        self.pb_eyes.setObjectName(u"pb_eyes")
        self.pb_eyes.setGeometry(QRect(300, 410, 30, 30))
        self.pb_eyes.setStyleSheet(u"color: white;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Login", None))
        self.le_user.setPlaceholderText(QCoreApplication.translate("Dialog", u"User", None))
        self.le_pw.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.pb_submit.setText(QCoreApplication.translate("Dialog", u"Sign In", None))
        self.label_user.setText("")
        self.label_pw.setText("")
        self.label_mail.setText("")
        self.le_mail.setPlaceholderText(QCoreApplication.translate("Dialog", u"Mail", None))
        self.label_logo.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.pb_close.setText(QCoreApplication.translate("Dialog", u"X", None))
        self.pb_eyes.setText("")
    # retranslateUi

