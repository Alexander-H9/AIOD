#!/usr/bin/env python3

from flask import Flask, render_template, Response, request, jsonify, redirect
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

@app.route("/login", methods=["POST"])
def login():
    username = request.args.get("username", type=str)
    password = request.args.get("password", type=str)
    print(username, password)

    # mqtt client
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connected_flag = False
    
    # init client credentials
    client.username_pw_set(username=username, password=password)
    flag = True
    # connect client to broker
    global port
    status, port = authenticate(client) 
    if port == -1: 
        status = False
        print("The server is not up")
    print("status: ", status)
    print("port: ", port)
    if not status:
        flag = False

    if flag:
        return redirect("/home"), 302
    else:
        return ""

@app.route("/upload", methods=["POST"])
def upload():
    flag = 0
    status = ""

    f = request.files["image"]
    f_name = f.filename

    func = request.args.get("functionality", type=str)
    print(f_name, func)

    if not f_name.endswith(IMG_FE):
        pass
    
    else:
        flag, status = 1, "invalid file type"
    return jsonify([flag, status])

@app.route("/home")
def home():
    """Loading home page"""
    return render_template("home.html")

# ===============================
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
# ===============================

if __name__ == "__main__":
    if __debug__:
        app.run(debug=True, host='0.0.0.0')
    else:
        serve(app, host='0.0.0.0', port=80)