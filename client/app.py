#!/usr/bin/env python3

from flask import Flask, render_template, Response, request, jsonify, redirect, url_for
from waitress import serve
import capture_img
import os
import sys

import paho.mqtt.client as mqtt
from publish_img import authenticate, on_connect, get_picture_as_bytearray
from subscribe_img import start_connection

# for imports from parent dir
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from config import settings

IMG_FE = (".jpg", ".png", ".bmp", ".jpeg")

app = Flask(__name__)
app.is_logged_in = False

@app.route("/")
@app.route("/index")
def index():
    """Loading index page"""
    return render_template("index.html")

@app.route("/home")
def home():
    if app.is_logged_in == True:
        return render_template("home.html")
    else:
        return redirect(url_for(".index"))

# ===========================================

@app.route("/account/login", methods=["POST"])
def account_login():
    flag = False
    status = ""

    print(request.form)
    global username
    global password
    username = request.form.get("username", type=str)
    password = request.form.get("password", type=str)

    # mqtt client
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connected_flag = False
    
    # init client credentials
    client.username_pw_set(username=username, password=password)
    flag = True
    # connect client to broker
    global port
    print("start auth")
    status, port = authenticate(client) 

    if port == -1: 
        status = False
        print("The server is not up")
    print("status: ", status)
    print("port: ", port)

    if flag == True:
        app.is_logged_in = True

    return jsonify([flag, status])

# ===========================================

@app.route("/media/upload", methods=["POST"])
def upload_media():
    flag = False
    status = ""

    f = request.files["image"] 
    byte_img = request.files["image"].read()
    f_name = f.filename

    func = request.form.get("functionality", type=str)
    print(f_name, func)

    if f_name.endswith(IMG_FE):

        media_type = f_name.split(".")[-1]
        # byte_img = get_picture_as_bytearray(f)
        client = mqtt.Client()
        client.username_pw_set(username=username, password=password)

        if client.connect(settings.adress.broker) != 0:     # , 1883, 60
            print("Could not connect to MQTT Broker!")
            sys.exit(-1)
        print("listen and publish with port: ", port)
        status = start_connection(username, password, port, media_type, byte_img)

    
    else:
        flag, status = False, "invalid file type"
    return jsonify([flag, status])

# ===========================================

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# ===========================================

if __name__ == "__main__":
    if __debug__:
        app.run(debug=True, host='0.0.0.0')
    else:
        serve(app, host='0.0.0.0', port=80)