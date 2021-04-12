from datetime import datetime

from flask import Flask, render_template, request

from . import app


@app.route("/")
def home():
    """Render Home Page"""
    return render_template("home.html")

@app.route("/about/")
def about():
    """Render About Page"""
    return render_template("about.html")

@app.route("/contact")
def contact():
    """Render Contact Page"""
    return render_template("contact.html")

@app.route("/user")
@app.route("/user/<name>")
def user(name = None):
    """
    Render hello_there Page
    args : name
    """
    return render_template(
        "user_name.html",
        name = name,
        date = datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
