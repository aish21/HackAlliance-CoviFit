from app import app
from flask import render_template, Response, request
import ML.src.s5_test
import cv2

camera = cv2.VideoCapture(0)

@app.route("/")
def login():
    return render_template("loginpage.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/intro")
def introduction():
    return render_template("intro.html")


@app.route("/tutordashboard")
def tutordashboard():
    return render_template("recordnew_tutor.html")


@app.route("/lesson")
def lesson():
    return render_template("video.html")


@app.route('/video_feed')
def video_feed():
    return Response(ML.src.s5_test.main(), mimetype='multipart/x-mixed-replace; boundary=frame')
