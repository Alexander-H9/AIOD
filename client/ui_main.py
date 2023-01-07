#!/usr/bin/env python3

#-*- coding:utf-8 -*-

import os, sys, time
import paho.mqtt.client as mqtt

from PyQt5.QtWidgets import QDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QPixmap, QIcon, QMovie
from PyQt5.QtCore import Qt

from ui_resources import dlg_login
from ui_resources import mw_aiod
from publish_img import authenticate, on_connect, get_picture_as_bytearray
from subscribe_img import start_connection


# for imports from parent dir
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from config import settings

ICON_PATH = "./client/ui_resources/icons/"

# supported file formats
IMG_FE = (".jpg", ".png", ".bmp", ".jpeg")
VID_FE = (".mp4", ".mkv", ".avi", ".flv", ".mov", ".mpeg", ".wmv", ".gif")

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

        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowFlags(self.windowFlags()
                    ^ Qt.WindowContextHelpButtonHint)

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
        # mov = QMovie(ICON_PATH+"loader.gif")
        # self.ui.label_logo.setMovie(mov)
        # mov.start()

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
        Last changed: 16.11.2022, AH
            created
        """
        flag = True
        self.ui.label_invalid_login.hide()

        # get text input
        self.user = str(self.ui.le_user.text())
        self.pw = str(self.ui.le_pw.text())

        # check for wrong input text
        if self.user == "" or any(map(lambda x: x in self.user, SPECIAL_CHARACTERS)):
            self.ui.label_invalid_user.setText("Invalid user")
            self.ui.label_invalid_user.show()
            flag = False
        else:
            self.ui.label_invalid_user.hide()

        if self.pw == "":
            self.ui.label_invalid_pw.setText("Invalid entry")
            self.ui.label_invalid_pw.show()
            flag = False
        else:
            self.ui.label_invalid_pw.hide()
        
        # mqtt client
        client = mqtt.Client()
        client.on_connect = on_connect
        client.connected_flag = False
        
        # init client credentials
        client.username_pw_set(username=self.user, password=self.pw)

        # connect client to broker
        global port
        status, port = authenticate(client) 
        if port == -1: 
            status = False
            print("The server is not up")
        print("status: ", status)
        print("port: ", port)
        if not status:
            self.ui.label_invalid_login.setText("Unable to connect")
            flag = False
        
        # check for errors
        if flag:
            self.accept()
        else:
            self.ui.label_invalid_login.show()


class UI_Main:
    def __init__(self):
        # build gui
        self.app = mw_aiod.QtWidgets.QApplication(sys.argv) # create application

        self.mainwindow = mw_aiod.QtWidgets.QMainWindow() # create window

        self.ui = mw_aiod.Ui_MainWindow() # load ui in window
        self.ui.setupUi(self.mainwindow) # setup ui

        self.mainwindow.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint) # disable maximize button

        self.app.aboutToQuit.connect(self.exitWindow) # run function before closing

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
        # self.ui.label_bg.setPixmap(QPixmap(ICON_PATH+"logo.png"))
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
        self.ui.pb_select.clicked.connect(self.selectFile)
        self.ui.pb_upload.clicked.connect(self.upload)
    
    def selectFile(self):
        """connects all buttons with functions

        Args:
            -
        Returns:
            -
        Last changed: 03.11.2022, AF
            created
        """
        self.src = QFileDialog.getOpenFileName(None, 'Select one file', os.path.expanduser("~"), " ".join(IMG_FE).replace(".", "*."))[0] # create dialog
        self.ui.label_preview.setPixmap(QPixmap(self.src).scaled(280, 260, Qt.KeepAspectRatio))
        self.ui.label_filename.setText(self.src.split("/")[-1])
    
    def upload(self):
        """connects all buttons with functions

        Args:
            -
        Returns:
            -
        Last changed: 23.11.2022, AF
            created
        """
        media_type = self.src.split(".")[-1]
        byte_img = get_picture_as_bytearray(self.src)
        client = mqtt.Client()
        client.username_pw_set(username=self.dlg.user, password=self.dlg.pw)

        if client.connect(settings.adress.lokal_broker, 1883, 60) != 0: 
            print("Could not connect to MQTT Broker!")
            sys.exit(-1)
        print("listen and publish with port: ", port)
        result = start_connection(self.dlg.user, self.dlg.pw, port, media_type, byte_img)
        self.ui.label_result.setText(result)


    def show(self):
        """show window after init

        Args:
            -
        Returns:
            -
        Last changed: 16.10.2022, AF
            created
        """
        self.dlg = UI_LogIn()
        ret = self.dlg.exec()

        if ret:
            self.mainwindow.show() # display window with ui
            sys.exit(self.app.exec_())
    
    def exitWindow(self):
        """execute before closing via red x-button

        Args:
            -
        Returns:
            -
        Last changed: 15.11.2022, AF
            created
        """
        start_connection(self.dlg.user, self.dlg.pw, port, 0, 0)
        print("Disconnected from broker")
        sys.exit(0)
    
if __name__ == "__main__":
    ui_main = UI_Main()
    ui_main.show()