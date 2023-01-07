#!/usr/bin/env python3

from flask import Flask, render_template
from waitress import serve

app = Flask(__name__)

@app.route("/")
def index():
    """Loading index page"""
    return render_template("index.html")

@app.route("/home")
def home():
    """Loading home page"""
    return render_template("home.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    if __debug__:
        app.run(debug=True, host='0.0.0.0')
    else:
        serve(app, host='0.0.0.0', port=80)