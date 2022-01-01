from datetime import datetime

from flask import Flask, render_template

from . import app

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/catalog/")
def catalog():
    return render_template("catalog.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

