#!/usr/bin/env python3

from flask import Flask, render_template, Response, request, jsonify, redirect, url_for
from waitress import serve
import capture_img

import paho.mqtt.client as mqtt
from publish_img import authenticate, on_connect, get_picture_as_bytearray
from subscribe_img import start_connection

IMG_FE = (".jpg", ".png", ".bmp", ".jpeg")

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    """Loading index page"""
    return render_template("index.html")

@app.route("/home")
def home():
    """Loading home page"""
    return render_template("home.html")

# ===========================================

@app.route("/account/login", methods=["POST"])
def account_login():
    flag = 0
    status = ""

    print(request.form)
    username = request.form.get("username", type=str)
    password = request.form.get("password", type=str)
    
    if request.method == "POST":
        print(request.method)

    # # mqtt client
    # client = mqtt.Client()
    # client.on_connect = on_connect
    # client.connected_flag = False
    
    # # init client credentials
    # client.username_pw_set(username=username, password=password)
    # flag = True
    # # connect client to broker
    # global port
    # status, port = authenticate(client) 
    # if port == -1: 
    #     status = False
    #     print("The server is not up")
    # print("status: ", status)
    # print("port: ", port)
    # if not status:
    if username == "admin" and password == "admin":
        pass
    else:
        flag = 1
        status = "not registered"
    return jsonify([flag, status])

# ===========================================

@app.route("/media/upload", methods=["POST"])
def upload_media():
    flag = 0
    status = ""

    f = request.files["image"]
    f_name = f.filename

    func = request.form.get("functionality", type=str)
    print(f_name, func)

    if f_name.endswith(IMG_FE):
        if f_name == "pfanne.jpg":
            status = "99% Bratpfanne"
    
    else:
        flag, status = 1, "invalid file type"
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