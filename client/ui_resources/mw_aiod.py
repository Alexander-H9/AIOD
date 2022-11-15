# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mw_aiod.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 480)
        MainWindow.setStyleSheet("background-color: #000000;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pb_upload = QtWidgets.QPushButton(self.centralwidget)
        self.pb_upload.setGeometry(QtCore.QRect(230, 40, 160, 60))
        self.pb_upload.setStyleSheet("font: 20px;\n"
"border: 1px solid #999999;\n"
"color: #ffffff;\n"
"border-radius: 3px;")
        self.pb_upload.setObjectName("pb_upload")
        self.pb_select = QtWidgets.QPushButton(self.centralwidget)
        self.pb_select.setGeometry(QtCore.QRect(40, 40, 160, 60))
        self.pb_select.setStyleSheet("font: 20px;\n"
"border: 1px solid #999999;\n"
"color: #ffffff;\n"
"border-radius: 3px;")
        self.pb_select.setObjectName("pb_select")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 120, 161, 41))
        self.label.setStyleSheet("font: 15px;\n"
"color: #ffffff;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 410, 720, 70))
        self.label_2.setStyleSheet("font: 20px;\n"
"color: #ffffff;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(420, 40, 241, 60))
        self.comboBox.setStyleSheet("font: 20px;\n"
"color: #ffffff;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 410, 720, 2))
        self.line.setStyleSheet("border: 5px solid #666666;")
        self.line.setLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AIOD"))
        self.pb_upload.setText(_translate("MainWindow", "Upload"))
        self.pb_select.setText(_translate("MainWindow", "Select file"))
        self.label.setText(_translate("MainWindow", "Filename.jpg"))
        self.label_2.setText(_translate("MainWindow", "99% Objekt"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Objekterkennung"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Texterkennung"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
