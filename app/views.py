from app import app
from flask import render_template


@app.route("/")
def login():
    return render_template("loginpage.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/introduction")
def introduction():
    return render_template("intro.html")


@app.route("/tutordashboard")
def tutorDashboard():
    return render_template("recordnew_tutor.html")


@app.route("/class/")
def videoLesson():
    return render_template("video.html")
