from flask import Flask, render_template, Response, request
import cv2

app = Flask(__name__)
global camera

camera = cv2.VideoCapture(0)

from app import views