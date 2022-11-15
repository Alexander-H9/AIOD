# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlg_login.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 600)
        Dialog.setStyleSheet("background-color: #000000;")
        self.le_user = QtWidgets.QLineEdit(Dialog)
        self.le_user.setGeometry(QtCore.QRect(90, 220, 240, 50))
        self.le_user.setStyleSheet("font: 20px;\n"
"color: #ffffff;\n"
"border: none;")
        self.le_user.setMaxLength(32)
        self.le_user.setObjectName("le_user")
        self.le_pw = QtWidgets.QLineEdit(Dialog)
        self.le_pw.setGeometry(QtCore.QRect(90, 340, 240, 50))
        self.le_pw.setStyleSheet("font: 20px;\n"
"color: #ffffff;\n"
"border: none;")
        self.le_pw.setMaxLength(32)
        self.le_pw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_pw.setObjectName("le_pw")
        self.pb_submit = QtWidgets.QPushButton(Dialog)
        self.pb_submit.setGeometry(QtCore.QRect(30, 470, 300, 60))
        self.pb_submit.setStyleSheet("font: 20px;\n"
"border: 1px solid #999999;\n"
"color: #ffffff;\n"
"border-radius: 3px;")
        self.pb_submit.setObjectName("pb_submit")
        self.label_user = QtWidgets.QLabel(Dialog)
        self.label_user.setGeometry(QtCore.QRect(30, 220, 50, 50))
        self.label_user.setText("")
        self.label_user.setScaledContents(True)
        self.label_user.setObjectName("label_user")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(30, 280, 300, 2))
        self.line.setStyleSheet("border: 5px solid #666666;")
        self.line.setLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(30, 400, 300, 2))
        self.line_2.setStyleSheet("border: 5px solid #666666;")
        self.line_2.setLineWidth(0)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_pw = QtWidgets.QLabel(Dialog)
        self.label_pw.setGeometry(QtCore.QRect(30, 340, 50, 50))
        self.label_pw.setText("")
        self.label_pw.setScaledContents(True)
        self.label_pw.setObjectName("label_pw")
        self.label_logo = QtWidgets.QLabel(Dialog)
        self.label_logo.setGeometry(QtCore.QRect(120, 60, 120, 120))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        self.pb_eyes = QtWidgets.QPushButton(Dialog)
        self.pb_eyes.setGeometry(QtCore.QRect(300, 350, 30, 30))
        self.pb_eyes.setStyleSheet("color: white;")
        self.pb_eyes.setText("")
        self.pb_eyes.setObjectName("pb_eyes")
        self.label_invalid_user = QtWidgets.QLabel(Dialog)
        self.label_invalid_user.setEnabled(True)
        self.label_invalid_user.setGeometry(QtCore.QRect(90, 290, 240, 15))
        self.label_invalid_user.setStyleSheet("font: 12px;\n"
"color: #f50537;")
        self.label_invalid_user.setText("")
        self.label_invalid_user.setObjectName("label_invalid_user")
        self.label_invalid_pw = QtWidgets.QLabel(Dialog)
        self.label_invalid_pw.setGeometry(QtCore.QRect(90, 410, 240, 15))
        self.label_invalid_pw.setStyleSheet("font: 12px;\n"
"color: #f50537;")
        self.label_invalid_pw.setText("")
        self.label_invalid_pw.setObjectName("label_invalid_pw")
        self.label_invalid_login = QtWidgets.QLabel(Dialog)
        self.label_invalid_login.setGeometry(QtCore.QRect(30, 530, 300, 15))
        self.label_invalid_login.setStyleSheet("font: 12px;\n"
"color: #f50537;")
        self.label_invalid_login.setText("")
        self.label_invalid_login.setObjectName("label_invalid_login")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AIOD - Login"))
        self.le_user.setPlaceholderText(_translate("Dialog", "User"))
        self.le_pw.setPlaceholderText(_translate("Dialog", "Password"))
        self.pb_submit.setText(_translate("Dialog", "Sign In"))
        self.label_logo.setText(_translate("Dialog", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
