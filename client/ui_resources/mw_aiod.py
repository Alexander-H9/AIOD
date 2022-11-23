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
        self.pb_upload.setGeometry(QtCore.QRect(400, 300, 280, 60))
        self.pb_upload.setStyleSheet("font: 20px;\n"
"border: 1px solid #999999;\n"
"color: #ffffff;\n"
"border-radius: 3px;")
        self.pb_upload.setObjectName("pb_upload")
        self.pb_select = QtWidgets.QPushButton(self.centralwidget)
        self.pb_select.setGeometry(QtCore.QRect(40, 40, 280, 60))
        self.pb_select.setStyleSheet("font: 20px;\n"
"border: 1px solid #999999;\n"
"color: #ffffff;\n"
"border-radius: 3px;")
        self.pb_select.setObjectName("pb_select")
        self.label_filename = QtWidgets.QLabel(self.centralwidget)
        self.label_filename.setGeometry(QtCore.QRect(40, 408, 280, 30))
        self.label_filename.setStyleSheet("font: 15px;\n"
"color: #ffffff;\n"
"border-bottom: 1px solid #999999;")
        self.label_filename.setText("")
        self.label_filename.setObjectName("label_filename")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(400, 380, 280, 60))
        self.label_result.setStyleSheet("font: 20px;\n"
"border-top: 1px solid #999999;\n"
"border-bottom: 1px solid #999999;\n"
"color: #ffffff;\n"
"border-radius: 3px;")
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setObjectName("label_result")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(400, 40, 280, 60))
        self.comboBox.setStyleSheet("font: 20px;\n"
"color: #ffffff;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(360, 30, 2, 420))
        self.line_2.setStyleSheet("border: 5px solid #666666;")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_preview = QtWidgets.QLabel(self.centralwidget)
        self.label_preview.setGeometry(QtCore.QRect(40, 120, 280, 280))
        self.label_preview.setScaledContents(False)
        self.label_preview.setAlignment(QtCore.Qt.AlignCenter)
        self.label_preview.setObjectName("label_preview")
        self.label_bg = QtWidgets.QLabel(self.centralwidget)
        self.label_bg.setGeometry(QtCore.QRect(460, 120, 160, 160))
        self.label_bg.setStyleSheet("background: rgba(0,0,0,0)")
        self.label_bg.setScaledContents(True)
        self.label_bg.setObjectName("label_bg")
        self.label_bg_loader = QtWidgets.QLabel(self.centralwidget)
        self.label_bg_loader.setGeometry(QtCore.QRect(460, 120, 160, 160))
        self.label_bg_loader.setScaledContents(True)
        self.label_bg_loader.setObjectName("label_bg_loader")
        self.label_bg_loader.raise_()
        self.pb_upload.raise_()
        self.pb_select.raise_()
        self.label_filename.raise_()
        self.label_result.raise_()
        self.comboBox.raise_()
        self.line_2.raise_()
        self.label_preview.raise_()
        self.label_bg.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AIOD"))
        self.pb_upload.setText(_translate("MainWindow", "Upload"))
        self.pb_select.setText(_translate("MainWindow", "Select file"))
        self.label_result.setText(_translate("MainWindow", "99% Objekt"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Objekterkennung"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Texterkennung"))
        self.label_preview.setText(_translate("MainWindow", "TextLabel"))
        self.label_bg.setText(_translate("MainWindow", "TextLabel"))
        self.label_bg_loader.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
