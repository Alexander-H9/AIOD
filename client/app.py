#!/usr/bin/env python3

from flask import Flask, render_template, Response, request
from waitress import serve
import capture_img

app = Flask(__name__)

global camActive
camActive=False

@app.route("/")
def index():
    """Loading index page"""
    return render_template("index.html")


@app.route("/home")
def home():
    """Loading home page"""
    return render_template("home.html")

@app.route("/tabs")
def tabs():
    if request.form.get('active_cam_tab'):
        camActive=True
    else:
        camActive=False


@app.route("/camera")
def camera():
    if camActive==True:
        return Response(capture_img.frames(), \
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        return render_template("home.html")


@app.route("/capture")
def capture():
    capture_img.capture = 1
    return render_template("home.html")


@app.route("/upload")
def upload():
    #TODO
    return render_template("home.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    if __debug__:
        app.run(debug=True, host='0.0.0.0')
    else:
        serve(app, host='0.0.0.0', port=80)