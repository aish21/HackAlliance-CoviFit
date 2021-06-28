from app import app
from flask import render_template, Response, request
import ML.src.s5_test
import cv2

OPENCV_VIDEOIO_DEBUG = 1
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)


def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

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
    return Response(ML.src.s5_test.gen(), mimetype='multipart/x-mixed-replace; boundary=frame')
