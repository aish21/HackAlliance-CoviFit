from app import app
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, abort
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant

load_dotenv()
twilio_account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
twilio_api_key_sid = os.environ.get('TWILIO_API_KEY_SID')
twilio_api_key_secret = os.environ.get('TWILIO_API_KEY_SECRET')


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


@app.route('/callstarted', methods=['POST'])
def callstarted():
    username = request.get_json(force=True).get('username')
    if not username:
        abort(401)

    token = AccessToken(twilio_account_sid, twilio_api_key_sid,
                        twilio_api_key_secret, identity=username)
    token.add_grant(VideoGrant(room='My Room'))

    return {'token': token.to_jwt().decode()}
