#!/usr/bin/env python3

#-*- coding:utf-8 -*-

import os, sys
import paho.mqtt.client as mqtt

from PyQt5.QtWidgets import QDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

from ui_resources import dlg_login
from ui_resources import mw_aiod
from publish_img import on_connect

# for imports from parent dir
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from config import settings

ICON_PATH = "./client/ui_resources/icons/"

# supported file formats
IMG_FE = (".jpg", ".png", ".bmp", ".jpeg")
VID_FE = (".mp4", ".mkv", ".avi", ".flv", ".mov", ".mpeg", ".wmv")

# disallowed characters for password
SPECIAL_CHARACTERS = '!@#$%&()-_[]{};:"./<>?'

# mqtt client
client = mqtt.Client()
client.on_connect = on_connect


class UI_LogIn(QDialog):
    def __init__(self):
        super().__init__()

        # Create an instance of the GUI
        self.ui = dlg_login.Ui_Dialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.show_pw = False

        self.ui.label_invalid_user.hide()
        self.ui.label_invalid_pw.hide()

        self.loadIcons()
        self.setupButtons()
    
    def loadIcons(self):
        """loads all icons of ui elements

        Args:
            -
        Returns:
            -
        Last changed: 16.10.2022, AF
            created
        """
        self.ui.label_logo.setPixmap(QPixmap(ICON_PATH+"logo.png"))

        self.ui.label_user.setPixmap(QPixmap(ICON_PATH+"user.png"))
        self.ui.label_pw.setPixmap(QPixmap(ICON_PATH+"pw.png"))
        
        self.ui.pb_eyes.setIcon(QIcon(ICON_PATH+"eye.png"))

    def setupButtons(self):
        """connects all buttons with functions

        Args:
            -
        Returns:
            -
        Last changed: 16.10.2022, AF
            created
        """
        self.ui.pb_close.clicked.connect(self.close)

        self.ui.pb_eyes.clicked.connect(self.showPassword)
        self.ui.pb_submit.clicked.connect(self.submitCredentials)
    
    def showPassword(self):
        """connects all buttons with functions

        Args:
            -
        Returns:
            -
        Last changed: 24.10.2022, AF
            created
        """
        if not self.show_pw:
            self.ui.le_pw.setEchoMode(QLineEdit.Normal)
            self.show_pw = True
            self.ui.pb_eyes.setIcon(QIcon(ICON_PATH+"eye_n.png"))
        else:
            self.ui.le_pw.setEchoMode(QLineEdit.Password)
            self.show_pw = False
            self.ui.pb_eyes.setIcon(QIcon(ICON_PATH+"eye.png"))
    
    def submitCredentials(self):
        """check credentials

        Args:
            -
        Returns:
            -
        Last changed: 16.10.2022, AF
            created
        """
        user = str(self.ui.le_user.text())
        pw = str(self.ui.le_pw.text())

        client.username_pw_set(username=user, password=pw)

        if client.connect("127.0.0.1", 1883, 60) != 0: 
            print("Could not connect to MQTT Broker!")
            sys.exit(-1)

        
        if user == "" or any(map(lambda x: x in user, SPECIAL_CHARACTERS)):
            self.ui.label_invalid_user.show()
            return

        if pw == "":
            self.ui.label_invalid_pw.show()
            return
        
        suc = True
        # do stuff
        if suc:
            self.accept()
        else:
            self.close()

class UI_Main:
    def __init__(self):
        # build gui
        self.app = mw_aiod.QtWidgets.QApplication(sys.argv) # create application

        self.mainwindow = mw_aiod.QtWidgets.QMainWindow() # create window

        self.ui = mw_aiod.Ui_MainWindow() # load ui in window
        self.ui.setupUi(self.mainwindow) # setup ui

        self.mainwindow.setWindowFlags(Qt.FramelessWindowHint)

        # setup gui and windows
        self.setStyle() # set style
        self.loadIcons() # load all icons
        self.setupButtons() # setup buttons with logical functions
    
    def setStyle(self):
        """changes stylesheet

        Args:
            -
        Returns:
            -
        Last changed: 16.10.2022, AF
            created
        """
        pass
    
    def loadIcons(self):
        """loads all icons of ui elements

        Args:
            -
        Returns:
            -
        Last changed: 16.10.2022, AF
            created
        """
        pass

    def setupButtons(self):
        """connects all buttons with functions

        Args:
            -
        Returns:
            -
        Last changed: 16.10.2022, AF
            created
        """
        self.ui.pb_close.clicked.connect(self.mainwindow.close)
        self.ui.pb_minimize.clicked.connect(self.mainwindow.showMinimized)

        self.ui.pb_select.clicked.connect(self.selectFile)
    
    def selectFile(self):
        """connects all buttons with functions

        Args:
            -
        Returns:
            -
        Last changed: 03.11.2022, AF
            created
        """
        src = QFileDialog.getOpenFileName(None, 'Select one file', os.path.expanduser("~"), " ".join(IMG_FE+VID_FE).replace(".", "*."))[0] # create dialog

    def show(self):
        """show window after init

        Args:
            -
        Returns:
            -
        Last changed: 16.10.2022, AF
            created
        """
        self.mainwindow.show() # display window with ui
        sys.exit(self.app.exec_())
    
if __name__ == "__main__":
    ui_main = UI_Main()
    dlg = UI_LogIn()
    ret = dlg.exec()
    if ret:
        ui_main.show()